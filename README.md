<div align="center">

# 大老王 Public-Safe Skill · 口播风格 Agent

**把公开口播内容蒸馏成可调用的 Agent Skill：学判断框架、表达节奏和场景化思路，不携带原始语料。**

`1508 条规范化语料记录` · `302 条候选观点审计` · `6 个核心模块` · `public-safe 公开版` · `无原始逐字稿` · `无私有证据包`

[![Stars](https://img.shields.io/github/stars/9-GETOVER-9/laowang-skill-public?style=for-the-badge&color=yellow&label=Stars)](https://github.com/9-GETOVER-9/laowang-skill-public/stargazers)
[![Version](https://img.shields.io/badge/version-v1.0.0-blue?style=for-the-badge)](https://github.com/9-GETOVER-9/laowang-skill-public)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![Public Safe](https://img.shields.io/badge/public--safe-ready-orange?style=for-the-badge)](NOTICE.md)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-ready-purple?style=for-the-badge)](SKILL.md)

</div>

---

> 核心不是复刻一个人的身份，而是把公开表达中反复出现的判断方式、叙事结构、问题分类和边界意识，整理成 Agent 可以稳定调用的 Skill。

## 一句话介绍

这是一个 public-safe 的“大老王口播风格” Agent Skill。它把公开口播材料蒸馏为人生决策、家庭教育、金融商业、玄学命运、表达风格和边界控制模块，让 AI 在回答相关问题时能学习一种“先看时代和空间，再看选择与行动”的口播式判断框架。

**直接激活词**：`大老王` / `老王视角` / `老王来了` / `老王会怎么看` / `大老王风格`

---

## 快速安装

<details open>
<summary><b>Codex / 本地 Skill 安装</b></summary>

```bash
git clone https://github.com/9-GETOVER-9/laowang-skill-public.git
mkdir -p ~/.codex/skills
cp -r laowang-skill-public ~/.codex/skills/laowang-skill-public
```

Windows PowerShell:

```powershell
git clone https://github.com/9-GETOVER-9/laowang-skill-public.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills"
Copy-Item -Recurse -Force .\laowang-skill-public "$env:USERPROFILE\.codex\skills\laowang-skill-public"
```

</details>

<details>
<summary><b>手动使用</b></summary>

把本仓库作为普通资料包使用时，优先阅读：

```text
SKILL.md
expression_style.md
modules/
references/research/
cases/
```

如果只是想了解项目结构，先看 `references/production-flow.md`。

</details>

---

## 功能矩阵

| 能力 | 覆盖 | 说明 |
|:---|:---:|:---|
| 核心世界观 | ✅ | 时代、空间、阶层、电梯、船、路径选择等高频判断框架 |
| 人生决策 | ✅ | 关键节点、行动优先级、换方向、提前准备和低调执行 |
| 表达 DNA | ✅ | 口播开场、类比、来信式讲述、强判断、重复强调与收束 |
| 家庭教育 | ✅ | 孩子松弛感、家庭迁移、同伴结构、父母投射与长期轨迹 |
| 金融商业 | ✅ | 市场规则、现金流、商业模式、杠杆、退出路径与风险边界 |
| 玄学命运 | ✅ | 命数边界、趋吉避凶、空间变量、时机变量与现实行动 |
| 边界控制 | ✅ | 不复读政治观点，不输出原始语料，不模仿攻击性表层语言 |
| 公开证据说明 | ✅ | 仅保留 public-safe 摘要，不包含 source registry、hash 或 provenance |
| 评测材料 | ✅ | 路由矩阵、smoke tests、pressure tests 和 public release check |

---

## 使用示例

### 人生选择

> **Q：** 我现在工作很累，但又怕换方向失败，老王视角会怎么看？  
> **A：** 先别急着谈你能不能吃苦，先看你是不是在一条对的船上。日常执行靠努力，关键节点靠选择。方向错了，越努力越像在原地消耗；方向对了，再谈一勇敌百谋。

### 家庭教育

> **Q：** 要不要为了孩子换城市或换学校？  
> **A：** 不只算学费和排名，要算孩子的眼神、同伴结构、家庭松弛度和十年后的轨迹。教育不是把父母没完成的阶级任务压给孩子，而是给孩子换一个更容易长出真实优势的空间。

### 金融商业

> **Q：** 一个项目看起来回报很高，可以冲吗？  
> **A：** 先看它有没有真实造血，不要只听故事。现金流、规则、杠杆、退出路径，这几个东西不清楚，就别把漂亮叙事当确定性。涉及投资时，本 Skill 只做思路分析，不构成投资建议。

### 玄学命运

> **Q：** 命是不是已经定了？  
> **A：** 它不是一根铁轨，更像主枝和旁枝。你改变不了所有底层条件，但你可以换空间、换圈层、换时机、换行动顺序。所谓趋吉避凶，最后还是要落到现实动作上。

---

## 核心工作流

```text
用户问题
  ↓
判断问题类型：选择 / 行动 / 空间 / 家庭教育 / 金融商业 / 命运 / 表达
  ↓
读取 SKILL.md 的 Kernel 路由
  ↓
按需读取 modules/ 与 references/research/
  ↓
输出一个主判断 + 一个类比 + 一条行动路径 + 必要边界
```

---

## 项目结构

```text
laowang-skill-public/
├── SKILL.md                         # Skill 入口、角色核心、路由和边界
├── expression_style.md              # 表达风格指南
├── modules/                         # 可调用领域模块
├── references/
│   ├── production-flow.md           # 从原始材料到 public-safe Skill 的流程
│   ├── evidence/
│   │   └── public_evidence_note.jsonl
│   └── research/                    # public-safe 研究摘要
├── cases/                           # 可复用公开案例
├── evaluations/                     # 路由矩阵与测试输出
├── NOTICE.md
└── LICENSE
```

---

## 与原始语料的关系

本仓库不靠运行时检索原始逐字稿回答用户。它使用的是已经蒸馏过的 finding、模块、表达规则和 public-safe 摘要。

也就是说，公开包缺少原始语料不会影响 Skill 的基础使用；影响的是后续深度审计、追溯证据、二次蒸馏和精修迭代。需要严肃复核某个观点来源时，应回到私有研究包，而不是在公开仓库里暴露原始材料。

---

## 不包含什么

- 原始音视频、字幕、逐字稿。
- 长段原文摘录。
- 可识别私人信息。
- 私有 source registry、hash/provenance 包或完整 canonical 语料。
- 政治观点复读模式。
- 攻击性、露骨或骚扰式表层语言模仿。

---

## 免责声明

This is an independent research/educational artifact. It is not an official project, endorsement, authorization, or representation of any real person. The Skill imitates distilled rhetorical structure and decision patterns, not identity, private facts, or harmful surface language.

金融、法律、医疗、移民等高风险问题只做思路分析，不替代专业意见，也不替用户做最终决策。

---

## License

MIT License. See [LICENSE](LICENSE).
