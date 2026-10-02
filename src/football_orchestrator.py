from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class Evidence:
    source: str
    signal: str
    strength: float
    detail: str = ""


@dataclass
class AnalysisResult:
    status: str
    conclusion: str
    confidence: float
    evidence: List[Evidence] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)


class FootballOrchestrator:
    """统一编排足球比赛分析流程。"""

    def analyze(
        self,
        match: Dict[str, Any],
        odds: Dict[str, Any] | None = None,
        historical_matches: List[Dict[str, Any]] | None = None,
    ) -> AnalysisResult:

        odds = odds or {}
        historical_matches = historical_matches or []

        evidence: List[Evidence] = []
        risks: List[str] = []

        # 1. 基础数据验证
        if not match:
            return AnalysisResult(
                status="insufficient_data",
                conclusion="暂不推荐：缺少比赛数据",
                confidence=0.0,
                risks=["缺少比赛基础数据"],
            )

        evidence.append(
            Evidence(
                source="match",
                signal="match_data_available",
                strength=1.0,
                detail="比赛基础数据已提供",
            )
        )

        # 2. 赔率数据
        if odds:
            evidence.append(
                Evidence(
                    source="odds",
                    signal="odds_available",
                    strength=0.8,
                    detail="赔率数据已提供，等待进一步计算",
                )
            )
        else:
            risks.append("缺少赔率数据")

        # 3. 历史相似盘
        if historical_matches:
            evidence.append(
                Evidence(
                    source="historical_matching",
                    signal="historical_matches_available",
                    strength=0.8,
                    detail=f"发现 {len(historical_matches)} 条历史匹配记录",
                )
            )
        else:
            risks.append("暂无历史相似盘匹配结果")

        # 4. Risk Gate
        if len(evidence) < 2:
            return AnalysisResult(
                status="blocked",
                conclusion="暂不推荐：证据不足",
                confidence=0.0,
                evidence=evidence,
                risks=risks,
            )

        # 5. 当前阶段不强行给出赛果
        return AnalysisResult(
            status="ready_for_analysis",
            conclusion="数据已进入分析流水线，等待赔率、历史匹配及复盘模块进一步计算",
            confidence=0.5,
            evidence=evidence,
            risks=risks,
        )


if __name__ == "__main__":
    orchestrator = FootballOrchestrator()

    result = orchestrator.analyze(
        match={"home": "Home", "away": "Away"}
    )

    print(result)
