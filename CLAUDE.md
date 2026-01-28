# ABFinance Python API

## Skills First Workflow

在执行任何任务前，必须先检查以下 skills 是否适用：

- `/git-commit` - Git 提交工作流（创建分支、提交、PR，不添加 Claude 署名）

### 规则

1. 收到用户请求后，首先扫描 Available skills 列表
2. 如果任务与某个 skill 匹配，必须使用 Skill 工具调用该 skill
3. 只有在没有匹配的 skill 时，才手动执行任务

### 关键词映射

| 用户请求关键词 | 对应 Skill |
|--------------|-----------|
| 提交、commit、push、推送、推上去 | `/git-commit` |
| 前端、UI、界面、组件、页面 | `/frontend-design` |
