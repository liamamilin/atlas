'use strict';

// Host diagnostic: parse source text only. Never require or execute package code.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const ts = require('../../../../atlas-web/node_modules/typescript');

const source = path.resolve(process.argv[2]);
const output = path.resolve(process.argv[3]);
const files = [];
function walk(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const target = path.join(directory, entry.name);
    if (entry.isDirectory()) walk(target);
    else if (entry.isFile() && entry.name.endsWith('.cjs')) files.push(target);
  }
}
walk(source);
const findings = [];
const checked = [];
for (const file of files.sort()) {
  const text = fs.readFileSync(file, 'utf8');
  const ast = ts.createSourceFile(file, text, ts.ScriptTarget.Latest, true, ts.ScriptKind.JS);
  if (ast.parseDiagnostics.length) throw new Error('Parser diagnostics: ' + file);
  const asyncNames = new Set();
  function declarations(node) {
    if (ts.isFunctionDeclaration(node) && node.name && node.modifiers?.some(m => m.kind === ts.SyntaxKind.AsyncKeyword)) {
      asyncNames.add(node.name.text);
    }
    ts.forEachChild(node, declarations);
  }
  declarations(ast);
  function calls(node) {
    if (ts.isExpressionStatement(node) && ts.isCallExpression(node.expression) && ts.isIdentifier(node.expression.expression)) {
      const name = node.expression.expression.text;
      if (asyncNames.has(name)) {
        const location = ast.getLineAndCharacterOfPosition(node.getStart(ast));
        findings.push({ file: path.relative(source, file), line: location.line + 1, callee: name, source: node.getText(ast) });
      }
    }
    ts.forEachChild(node, calls);
  }
  calls(ast);
  checked.push({ file: path.relative(source, file), sha256: crypto.createHash('sha256').update(text).digest('hex'), local_async_names: [...asyncNames].sort() });
}
const result = {
  typescript_version: ts.version,
  scope: 'Host AST parsing only: direct bare expression calls to named locally declared async functions. No generated program executed. No inference about imported methods, async arrows, callbacks, promise chains or runtime outcomes; findings need source inspection.',
  checked,
  findings,
};
fs.writeFileSync(output, JSON.stringify(result, null, 2) + '\n');
process.stdout.write(JSON.stringify({ checked_files: checked.length, findings }) + '\n');
