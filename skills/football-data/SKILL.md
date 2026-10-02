---
name: football-data
description: 足球比赛数据采集与质量检查 Skill，为足球分析引擎提供统一、可靠、可追溯的数据输入。
---

# Football Data

## 目标

负责为 Football AI 提供标准化比赛数据，并确保数据质量、时间一致性和历史回测的可靠性。

## 数据优先级

1. 官方或可靠 API 数据
2. 用户提供的历史 CSV 数据库
3. 可靠的赔率时间序列
4. 用户提供的截图作为补充数据

截图可以用于读取当前盘口，但不能替代历史 CSV 数据库。

## 基础数据

尽可能获取：

- 比赛 ID
- 联赛
- 比赛时间
- 主队
- 客队
- 主客场
- 最近比赛
- 进球/失球
- 主客场表现
- 积分与排名
- 伤停信息（只有可靠来源才使用）
- 欧赔
- 竞彩数据
- 亚盘
- 大小球
- 数据采集时间

## 数据标准化

处理数据时必须：

- 统一球队名称
- 统一比赛 ID
- 统一时区
- 记录数据采集时间
- 标记缺失数据
- 标记异常数据
- 区分历史数据和实时数据

## API-Football

API Key 只能从环境变量读取。

禁止：

- 把 API Key 写进代码
- 把 API Key 写进 Skill
- 把 API Key 提交到 GitHub
- 在日志中输出 API Key

建议环境变量：

API_FOOTBALL_KEY

## 历史 CSV 数据库

历史 CSV 是历史同赔、相似盘型和回测的重要数据源。

必须：

- 保留原始 CSV
- 建立标准化字段
- 记录数据来源
- 记录清洗过程
- 保留原始比赛日期
- 防止未来数据进入过去的回测

## 时间一致性

进行历史回测时：

只能使用比赛开始之前能够获得的数据。

禁止使用：

- 赛后赔率
- 赛果
- 赛后新闻
- 未来比赛数据

污染历史预测。

## 数据质量检查

如果出现：

- 比赛 ID 不一致
- 球队名称无法匹配
- 赔率缺失
- 时间异常
- 重复比赛
- 数据来源冲突

必须标记问题。

不得静默修正重要数据。

## 输出

向 Football AI 提供：

match_id
league
kickoff_time
home
away
recent_form
standings
injuries
odds_open
odds_current
odds_latest
handicap
over_under
data_timestamp
data_source
data_quality
missing_fields

## 核心原则

数据不完整时降低预测置信度。

数据无法验证时，不得伪造。

数据不足时允许输出：

暂不推荐 / 证据不足。
