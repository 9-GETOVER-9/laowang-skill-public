# 维护与更新

公开仓库只接收蒸馏后的 public-safe 内容，不接收原始数据集。完整的本地操作说明见工作区 `05-docs/UPDATE_AND_RELEASE_GUIDE.md`。

## 修复 Bug

1. 建立 `fix/...` 分支。
2. 修改 `SKILL.md`、模块、表达规则或案例。
3. 为问题补充回归案例或评测。
4. 运行 `python scripts/validate_public_release.py`。
5. 提交并通过 Pull Request 合并。

## 更新知识

新语料应先在私有工程中完成去重、来源登记、证据分层和重新蒸馏。公开仓库只接收审核后的 finding、模块、public-safe 摘要、合成案例和评测结果。

## 版本建议

- `PATCH`：修正文案、边界、路由或客户 Bug。
- `MINOR`：新增领域模块、明显扩充能力或吸收一批新语料。
- `MAJOR`：改变 Skill 核心角色、调用契约或目录结构。

