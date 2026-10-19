"""OpenCode exact patch for the empirically faulty generated acceptance helper."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT/'application-atlas-production-pack'))
from template_factory.cognition import apply_file_response  # noqa: E402

module_spec=importlib.util.spec_from_file_location('pilot_produce',HERE/'produce.py')
production=importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(production)
PROMPT='''Repair only acceptance/common.cjs using exact unique substring replacements, not a full replacement file. Read input.json, source/PRIOR.cjs and source/DIAGNOSTIC.json fully. Return {"path":"acceptance/common.cjs","replacements":[{"old":"exact unique current substring","new":"replacement"}]}. Do not execute, browse, install, edit files or change exported helper signatures. No unrelated redesign, assertion removal or fixed fixture values.
A real two-loopback-origin browser probe confirmed Authorization escaped on target-origin HTTP302 to another origin, and network guard falsely reported no outbound traffic. Fix the actual transport, not only the message. Route-based filtering alone cannot prevent redirected requests in Playwright. All real browser connections must be constrained to the exact configured target origin including port; do not exempt every loopback host. External navigation attempts may be recorded/blocked for URL verification, never really sent. A small deny-by-default browser proxy that forwards ONLY the exact configured HTTP target, combined with Chromium loopback-proxy-bypass disabling, is acceptable. Do not bypass this proxy for localhost. Validate target URL without userinfo; reject unsupported target transport/auth mode explicitly before requests. HTTPS is not required by this local HTTP P0 trial; rejecting unsupported HTTPS infrastructure explicitly is preferable to insecure pretend support. Optional basic auth may be made explicitly unsupported before any requests if maintaining it safely would expand P0; do not silently accept credentials then skip them. No real credentials exist in this probe.
Record denied redirect/background attempts so A17 cannot falsely claim no attempted outbound. Ensure background HTTP/fetch/images are violations while explicitly tested document navigation can be observed as a blocked attempt. Keep cleanup: close the dedicated deny proxy when its owned browser closes, reject browser startup errors cleanly, avoid leaving listeners. Use existing Node builtins, no new packages or shell. Preserve meaningful UI/data assertions and default no-auth P0 behavior. Preserve all exports and current helper calling conventions so case modules need no changes. Do not change claimed test outcomes; runtime re-probe will happen outside this session.'''

def main():
    prior=json.loads((HERE/'production/blueprint-code-1/result.json').read_text())['content']
    stage=HERE/'production/blueprint-code-network-repair'
    result=production.call(stage,PROMPT,{'language':'zh','file':{'path':'acceptance/common.cjs'},'scope':'empirically confirmed helper transport fault; current no-auth HTTP P0 only'},
                           {'PRIOR.cjs':prior,'DIAGNOSTIC.json':json.loads((HERE/'diagnostics/network-result.json').read_text())})
    base=HERE/'diagnostics/prior'
    (base/'acceptance').mkdir(parents=True,exist_ok=True)
    (base/'acceptance/common.cjs').write_text(prior)
    fixed=apply_file_response(result,'acceptance/common.cjs',base)
    (HERE/'diagnostics/helper-fixed.cjs').write_text(fixed['content'])
    (HERE/'network-repair.json').write_text(json.dumps({
        'path':fixed['path'],'base_sha256':hashlib.sha256(prior.encode()).hexdigest(),
        'fixed_sha256':hashlib.sha256(fixed['content'].encode()).hexdigest(),
        'model':'commandcode/deepseek/deepseek-v4.1-flash','runtime_reprobe':'not_run',
    },indent=2)+'\n')
    print('exact helper patch materialized; runtime re-probe still required',flush=True)

if __name__=='__main__':
    main()
