'use strict';

// Host diagnostic: inspect literal local CommonJS interfaces without loading them.
const fs = require('node:fs');
const path = require('node:path');
const ts = require('../../../../atlas-web/node_modules/typescript');
const root = path.resolve(process.argv[2]);
const output = path.resolve(process.argv[3]);
const modules = new Map();
function walk(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const file = path.join(directory, entry.name);
    if (entry.isDirectory()) walk(file);
    else if (entry.isFile() && file.endsWith('.cjs')) {
      const text = fs.readFileSync(file, 'utf8');
      const ast = ts.createSourceFile(file, text, ts.ScriptTarget.Latest, true, ts.ScriptKind.JS);
      if (ast.parseDiagnostics.length) throw new Error('Parser diagnostics: ' + file);
      let names = null;
      function exports(node) {
        if (ts.isBinaryExpression(node) && node.operatorToken.kind === ts.SyntaxKind.EqualsToken && node.left.getText(ast) === 'module.exports' && ts.isObjectLiteralExpression(node.right)) {
          names = new Set();
          for (const property of node.right.properties) {
            if (ts.isSpreadAssignment(property) || !property.name) { names = null; break; }
            names.add(ts.isIdentifier(property.name) || ts.isStringLiteral(property.name) ? property.name.text : property.name.getText(ast));
          }
        }
        ts.forEachChild(node, exports);
      }
      exports(ast);
      modules.set(file, { ast, names });
    }
  }
}
walk(root);
const findings = [];
const unsupported = [];
for (const [file, { ast }] of modules) {
  const namespaces = new Map();
  function check(module, name, node, kind) {
    const target = modules.get(module);
    if (!target || !target.names) {
      unsupported.push({ file: path.relative(root, file), module: path.relative(root, module), kind });
    } else if (!target.names.has(name)) {
      const location = ast.getLineAndCharacterOfPosition(node.getStart(ast));
      findings.push({ file: path.relative(root, file), line: location.line + 1, module: path.relative(root, module), missing_export: name, kind });
    }
  }
  function imports(node) {
    if (ts.isVariableDeclaration(node) && node.initializer && ts.isCallExpression(node.initializer) && node.initializer.expression.getText(ast) === 'require' && node.initializer.arguments.length === 1 && ts.isStringLiteral(node.initializer.arguments[0])) {
      const specifier = node.initializer.arguments[0].text;
      if (specifier.startsWith('.')) {
        const candidate = path.resolve(path.dirname(file), specifier);
        const target = modules.has(candidate) ? candidate : candidate + '.cjs';
        if (ts.isObjectBindingPattern(node.name)) {
          for (const element of node.name.elements) {
            if (!element.dotDotDotToken) check(target, element.propertyName?.text ?? element.name.text, element, 'destructured-require');
          }
        } else if (ts.isIdentifier(node.name)) namespaces.set(node.name.text, target);
      }
    }
    ts.forEachChild(node, imports);
  }
  imports(ast);
  function accesses(node) {
    if (ts.isPropertyAccessExpression(node) && ts.isIdentifier(node.expression) && namespaces.has(node.expression.text)) {
      check(namespaces.get(node.expression.text), node.name.text, node, 'namespace-property');
    }
    ts.forEachChild(node, accesses);
  }
  accesses(ast);
}
const result = {
  typescript_version: ts.version,
  scope: 'Host AST inspection of literal local module.exports objects, destructured require bindings and direct namespace properties. No generated module loaded or executed. Dynamic exports, imported function signatures, nested object members and lexical shadowing need separate review; unsupported interfaces are reported, not passed.',
  checked_modules: modules.size,
  findings,
  unsupported_interfaces: unsupported,
};
fs.writeFileSync(output, JSON.stringify(result, null, 2) + '\n');
process.stdout.write(JSON.stringify(result) + '\n');
