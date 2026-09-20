# 个人 AI 学习仓库（gefrdrfygu2026）

> 一个<strong>可公开访问、可继续迭代</strong>的个人学习仓库，沉淀 AI Agent / 大模型相关的概念理解、复用型 Skill，以及可分享的学习资料。

## 仓库用途

本仓库用于：

1. 存放一个<strong>可复用的"概念学习资料生成"项目级 Skill</strong>，为任意新概念生成结构化 HTML 学习材料
2. 用该 Skill 生成并经人工核查的<strong>三份概念学习资料</strong>（Agent / 大模型的上下文 / Skill）
3. 一份<strong>概念关系说明</strong>，讲清三者如何协作
4. 后续课程项目可在此基础上继续添加新概念、新 Skill

> ⚠️ 仓库当前 GitHub 名称仍为占位符 `-`（注册时中文输入法未切换导致），后续可重命名为更有意义的名字，不影响内容。

## 目录结构

```
仓库根/
├── .workbuddy/
│   └── skills/
│       └── concept-learning-generator/
│           └── SKILL.md          # 项目级 Skill：概念学习资料生成器（可复用）
├── learning-materials/
│   ├── agent.html                # Agent 核心要点（1 分钟速成）
│   ├── llm-context.html          # 大模型的上下文 核心要点
│   ├── skill.html                # Skill（AI 技能）核心要点
│   └── concept-relationship.html # 三概念关系图与详细说明
├── README.md                     # 本文件
└── .gitignore                    # 排除敏感文件、临时文件、IDE 配置等
```

## 仓库内容一览

| 文件 | 类型 | 说明 |
|------|------|------|
| `.workbuddy/skills/concept-learning-generator/SKILL.md` | 项目级 Skill | 通用概念学习资料生成器，<strong>可复用于任何概念</strong>，不限于 Agent / 上下文 / Skill |
| `learning-materials/agent.html` | 学习资料 | Agent 概念的个人解释、核心机制、应用场景、边界、自测题 |
| `learning-materials/llm-context.html` | 学习资料 | 大模型上下文的完整解析 |
| `learning-materials/skill.html` | 学习资料 | Skill 概念本身 |
| `learning-materials/concept-relationship.html` | 关系说明 | 三概念关系图（自包含 SVG）+ 对比表 + 重点关系解读 |

## 如何在 WorkBuddy 中调用本仓库的 Skill

本仓库的 Skill 是<strong>项目级 Skill</strong>，需要在本仓库目录下打开 WorkBuddy 才能被自动识别。

**自动触发**（推荐）：
> 在 WorkBuddy 中打开本仓库后，对 AI 说：
> "用 concept-learning-generator 学习 XX 概念"
> 或
> "请按本仓库的 concept-learning-generator Skill，帮我学习 Transformer 的工作机制"

**手动调用**（任意 LLM 都可复用）：
> 复制 `.workbuddy/skills/concept-learning-generator/SKILL.md` 中的"生成步骤" + "输出结构" + "自检要求"段落，作为 system prompt 发给任意 LLM 即可复用本 Skill 的方法论。

**调用 Skill 后会得到**：
- 一份 `learning-materials/<概念名>.html` 自包含文件
- 包含：定义、核心机制、应用场景、边界、资料来源、自测题
- 可直接双击在浏览器打开，可分享、可打印

## 三份学习资料的内容结构

每份资料（`agent.html` / `llm-context.html` / `skill.html`）都遵循 Skill 中定义的固定输出结构：

1. **一句话定义**（同时说"是什么"和"不是什么"）
2. **核心机制**（2–4 个子卡片）
3. **一个具体应用场景**（含真实细节）
4. **容易混淆的问题与边界**（2–4 条）
5. **可核查的资料来源**（≥3 个真实链接）
6. **自测题**（3–5 道，可点开展示答案）

## AI 使用与人工核查说明

本仓库内容由本人使用 WorkBuddy（AI 助手）协助完成，<strong>本人对内容做了人工核查和修改</strong>，具体如下：

### AI 做了什么
- **Skill 设计**：由 AI 协助起草 `.workbuddy/skills/concept-learning-generator/SKILL.md` 的结构、字段、自检清单
- **资料生成**：用 AI 按照 Skill 流程，生成 3 份学习资料的初稿
- **概念关系图**：用 AI 协助梳理三者关系并设计 SVG 示意图
- **README 起草**：本 README 由 AI 协助起草，本人审阅修改

### 人工核查与修改（本人完成）
- ✅ **资料来源核查**：所有 arXiv 论文链接、官方文档链接<strong>已实际访问验证</strong>，未使用 AI 生成的任何无法验证的来源
- ✅ **概念准确性核查**：核心机制部分与权威资料对照，确保无 AI 幻觉/编造
- ✅ **结构调整**：将 AI 生成的散乱段落重新组织为 Skill 规定的固定区块
- ✅ **第一人称重述**：将 AI 风格的内容改写为第一人称"我"的视角，避免整段照搬
- ✅ **应用场景具体化**：将 AI 给的通用场景替换为更具体、有人物/系统/数据细节的场景
- ✅ **仓库命名说明**：在 README 中如实标注 GitHub 仓库名仍为 `-`（注册时中文输入法问题），方便老师理解

### 防止 AI 滥用
- ❌ **未编造任何论文 / 作者 / 年份 / 文档链接**
- ❌ **未上传任何 API Key、密码、个人隐私信息**（`.gitignore` 已排除 `.env`、`*.key`、`.env.local` 等）
- ✅ 全部资料来源均可在浏览器实际打开验证

## 版本与安全

### 已完成的版本管理
- 本地 Git 仓库已初始化
- 已完成本地 `commit`
- 已 `push` 到 GitHub 公开仓库（链接见作业提交）

### 安全措施
- `.gitignore` 已排除：
  - 敏感：`.env`、`.env.local`、`*.key`、`*.pem`、`secrets/`
  - 临时：`__pycache__/`、`*.log`
  - IDE/系统：`.vscode/`、`.idea/`、`.DS_Store`、`Thumbs.db`
  - 依赖：`node_modules/`、`.venv/`
- 仓库中<strong>不包含</strong>任何 API Key、个人隐私、密码

## 后续迭代方向

- 重命名 GitHub 仓库为更有意义的名字（如 `ai-learning-hub`）
- 用本 Skill 学习更多概念（注意力机制 / RAG / 微调 / 思维链 / Function Calling …），每学一个就生成一份 `learning-materials/<概念>.html`
- 把每个新概念都更新到 `concept-relationship.html` 的关系图里
- 积累更多项目级 Skill（如"提交代码"、"写周报"、"读论文"等）

---

**仓库维护**：gefrdrfygu2026 · 邮箱 gsdx41032@qq.com

## 0917 课堂作业（大数据与人工智能 · 课程 9）

> 完成日期：2026-09-20 · 对应课堂要点：0917课堂要点

| 作业项 | 文件 | 状态 |
|--------|------|------|
| ① 创建 .py 文件并运行 | `scripts/01.py` | ✅ 已运行成功（输出"我会成功拿到offer!"） |
| ② 创建 .ipynb 文件并运行 | `scripts/01.ipynb` | ✅ 已运行成功（输出 `hidd`、`hi`） |
| ③ 提交到 GitHub 远程仓库 | 本仓库 main 分支 | ✅ 已推送 |

### 课堂要点完成情况

1. 安装 vscode、python、git ✅
2. 设置 pip 为国内源（清华源）✅
3. 设置 vscode 为中文界面 ✅
4. 设置 vscode 为自动保存 ✅

### 运行方式

```bash
python scripts/01.py        # 运行 Python 脚本
# scripts/01.ipynb 在 VS Code 中用 Jupyter 打开逐格运行
```
