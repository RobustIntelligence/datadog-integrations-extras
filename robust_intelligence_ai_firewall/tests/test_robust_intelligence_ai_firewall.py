from typing import Any, Callable, Dict  # noqa: F401

from datadog_checks.base import AgentCheck  # noqa: F401
from datadog_checks.base.stubs.aggregator import AggregatorStub  # noqa: F401
from datadog_checks.dev.utils import get_metadata_metrics
from datadog_checks.robust_intelligence_ai_firewall import RobustIntelligenceAiFirewallCheck


def test_check(dd_run_check, aggregator, instance):
    # type: (Callable[[AgentCheck, bool], None], AggregatorStub, Dict[str, Any]) -> None
    check = RobustIntelligenceAiFirewallCheck('robust_intelligence_ai_firewall', {}, [instance])
    dd_run_check(check)

    aggregator.assert_all_metrics_covered()
    aggregator.assert_metrics_using_metadata(get_metadata_metrics())


def test_emits_critical_service_check_when_service_is_down(dd_run_check, aggregator, instance):
    # type: (Callable[[AgentCheck, bool], None], AggregatorStub, Dict[str, Any]) -> None
    check = RobustIntelligenceAiFirewallCheck('robust_intelligence_ai_firewall', {}, [instance])
    dd_run_check(check)
    aggregator.assert_service_check(
        'robust_intelligence_ai_firewall.can_connect', RobustIntelligenceAiFirewallCheck.CRITICAL
    )