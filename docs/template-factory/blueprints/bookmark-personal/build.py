"""Render this sample's documents from its single normative template.json."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
v = json.loads((ROOT / "template.json").read_text())

def save(name, content):
    (ROOT / name).write_text(content.rstrip() + "\n")

def table(headers, rows):
    def clean(value):
        return str(value).replace("|", " / ").replace("\n", " ")
    return "\n".join(["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"] + ["| " + " | ".join(clean(c) for c in row) + " |" for row in rows])

save("CATEGORY.md", "# 品类认知与来源\n\n查阅日期：2026-10-17。以下为来源事实及本样板推导，未运行这些第三方产品；不把单个产品的扩展当作品类必须具备的能力。\n\n" + "\n\n".join(f"## {s['id']} · {s['name']}\n\n[原始资料]({s['url']}) · {s['version']}\n\n事实：{s['facts']}\n\n许可证记录：{s['license']}" + (f" · [原文]({s['license_url']})" if s.get('license_url') else "") + f"\n\n选型判断：{s['reuse']}。" for s in v['sources']) + "\n\n## 复用、自建与待验证\n\n直接使用现成 SaaS 适合接受其账户/托管方式的人；自托管账户型需求可先评估 linkding，协作与网页副本需求可评估 Linkwarden。当前选择自建轻量本地库，是针对当前场景的默认，不是认定这些产品不好用。未复制任何上游源码；后续若复用，需先固定版本、核对具体文件及许可，不能根据仓库标题推断全部模块都可直接复制。\n\n本地 IndexedDB、JSON 可带走、URL 校验等选择是设计推导，不是上述产品均采用的共同架构。托管权限、计费、后台、审计与备份恢复均已进入能力地图，是否实现由场景和项目决策决定。")
s = v['scenario']
save("PRODUCT.md", "# 产品定义\n\n" + s['name'] + "\n\n目标用户：" + s['audience'] + "\n\n目标：" + s['objective'] + "\n\n## 核心流程\n\n" + "\n".join(f"{i+1}. {step}" for i, step in enumerate(s['workflow'])) + "\n\n## 场景原始验收\n\n" + "\n".join("- " + a for a in s['acceptance']) + "\n\n## 角色\n\n" + "\n".join(f"- {r['id']} {r['name']}：{r['responsibility']}" for r in v['roles']) + "\n\n## 从 MVP 到成熟能力地图\n\n" + table(["ID", "能力", "阶段", "适用性", "理由", "来源", "验收"], [[f['id'],f['name'],f['phase'] or '需另定范围',f['applicability'],f['reason'],','.join(f['sources']),','.join(f['acceptance']) or '不在当前路线图'] for f in v['features']]) + "\n\n## 首阶段异常与非功能要求\n\n输入可能是危险 URL 或带 HTML 的标题；存储可能不可用或写入失败；保存期间可能重复提交；搜索可能为空；外链会离开本应用。必须给可理解的错误与状态，失败不清空输入、不谎报成功、不破坏已有记录。默认不因保存而访问外站。键盘、标签、状态播报和窄屏首阶段就需要。当前没有真实容量/性能基准，不捏造 SLA；P1 前仅适合可接受本地存储风险的试用，不称为已具备完整备份恢复的成熟产品。")
save("ARCHITECTURE.md", "# 架构、数据与契约\n\n" + v['architecture_markdown'])
save("DECISIONS.md", "# 默认值与人工决策\n\n这些是可调整的样板默认；先尊重当前项目已经确认的决定。普通可逆选择按默认推进并记录，只有依赖核心取舍的阶段才停下来问人。\n\n" + "\n\n".join(f"## {d['id']} · {d['question']}\n\n默认：{d['default']}\n\n何时询问：{d['when_to_ask']}\n\n影响：{d['impact']}\n\n状态：{d['status']}" for d in v['decisions']))
save("ROADMAP.md", "# 阶段路线图与验收\n\n各阶段交付完整用户能力；P0 通过不等于 P1/P2 已实现。\n\n" + "\n\n".join(f"## {p['id']} · {p['title']}\n\n目标：{p['goal']}\n\n功能：{', '.join(p['features'])}\n\n验收命令：`node acceptance/run.cjs --base-url http://127.0.0.1:5220 --phase {p['id']} --out /tmp/bookmark-{p['id']}.json`\n\n" + table(["用例", "类型", "行为"],[[a['id'],a['type'],a['goal']] for a in v['acceptance'] if a['phase']==p['id']]) for p in v['phases']) + "\n\n## 阶段完成与停止\n\n每阶段先核对相关决定，记录实现版本和真实测试结果。未实现的下一阶段保持待实现；若尝试运行它的测试，不能把缺按钮和缺行为当作通过或静默跳过。失败先修复当前阶段，不顺便一次生成所有后期能力。")
save("README.md", "# " + v['title'] + "\n\n这是 Atlas 首份认知模板样板，不是已经完成全部功能的应用源码包，也尚未接入工厂的新产物发布流程。规范版本 " + v['version'] + "。\n\n## 从哪里开始\n\n1. 阅读 PRODUCT.md 和 DECISIONS.md，确认当前项目适用默认单人本地形态。\n2. 让 coding agent 阅读 AGENT.md、ARCHITECTURE.md 和 ROADMAP.md，只实现当前阶段。\n3. 按 acceptance/README.md 安装测试工具，运行真实目标的对应验收并保存结果。\n4. 用 template.json 核对需求和用例映射；更新决策与证据，不随意删除失败用例。\n\nCATEGORY.md 给出处和复用判断；references/ 中只有新编写的小模块，无第三方应用源码。实际验证与待执行事项见 VALIDATION.md，不能由文档存在推断应用已通过。\n\n## 样板校验与打包\n\n`python3 build.py` 根据 template.json 生成阅读文档；`python3 verify.py` 校验规范、映射、文件摘要。规范包含验收 ID 与阶段，测试程序需要逐项有对应执行器。\n\n## 交付边界\n\n" + "\n".join("- " + a for a in v['limits']) + "\n- 默认值、接口名称和阶段划分可以因项目改变，但必须同时更新决策、契约和验收，不可只改测试令其变绿。")
files = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*') if p.is_file() and p.name != 'integrity.json' and '__pycache__' not in p.parts and 'node_modules' not in p.parts}
(ROOT/'integrity.json').write_text(json.dumps({'template_version':v['version'],'sha256':files},ensure_ascii=False,indent=2)+'\n')
