
from typing import Any  # noqa: F401

from datadog_checks.base import OpenMetricsBaseCheckV2  # noqa: F401

from .config_models import ConfigMixin
from .metrics import METRIC_MAP

# from datadog_checks.base.utils.db import QueryManager
# from requests.exceptions import ConnectionError, HTTPError, InvalidURL, Timeout
# from json import JSONDecodeError


class RobustIntelligenceAiFirewallCheck(OpenMetricsBaseCheckV2, ConfigMixin):

    # This will be the prefix of every metric and service check the integration sends
    __NAMESPACE__ = 'robust_intelligence_ai_firewall'

    def __init__(self, name, init_config, instances):
        super(RobustIntelligenceAiFirewallCheck, self).__init__(name, init_config, instances)

        self.openmetrics_endpoint = self.instance.get('openmetrics_endpoint')

    def get_default_config(self):
        default_config = {
            'openmetrics_endpoint': self.openmetrics_endpoint,
            'metrics': METRIC_MAP,
        }

        return default_config

    # def check(self, _):
        # type: # (Any) -> None
        # The following are useful bits of code to help new users get started.

        # Perform HTTP Requests with our HTTP wrapper.
        # More info at https://datadoghq.dev/integrations-core/base/http/
        # try:
        #     response = self.http.get(self.url)
        #     response.raise_for_status()
        #     response_json = response.json()

        # except Timeout as e:
        #     self.service_check(
        #         "can_connect",
        #         AgentCheck.CRITICAL,
        #         message="Request timeout: {}, {}".format(self.url, e),
        #     )
        #     raise

        # except (HTTPError, InvalidURL, ConnectionError) as e:
        #     self.service_check(
        #         "can_connect",
        #         AgentCheck.CRITICAL,
        #         message="Request failed: {}, {}".format(self.url, e),
        #     )
        #     raise

        # except JSONDecodeError as e:
        #     self.service_check(
        #         "can_connect",
        #         AgentCheck.CRITICAL,
        #         message="JSON Parse failed: {}, {}".format(self.url, e),
        #     )
        #     raise

        # except ValueError as e:
        #     self.service_check(
        #         "can_connect", AgentCheck.CRITICAL, message=str(e)
        #     )
        #     raise

        # This is how you submit metrics
        # There are different types of metrics that you can submit (gauge, event).
        # More info at https://datadoghq.dev/integrations-core/base/api/#datadog_checks.base.checks.base.AgentCheck
        # self.gauge("test", 1.23, tags=['foo:bar'])

        # Perform database queries using the Query Manager
        # self._query_manager.execute()

        # This is how you use the persistent cache. This cache file based and persists across agent restarts.
        # If you need an in-memory cache that is persisted across runs
        # You can define a dictionary in the __init__ method.
        # self.write_persistent_cache("key", "value")
        # value = self.read_persistent_cache("key")

        # If your check ran successfully, you can send the status.
        # More info at
        # https://datadoghq.dev/integrations-core/base/api/#datadog_checks.base.checks.base.AgentCheck.service_check
        # self.service_check("can_connect", AgentCheck.OK)

        # If it didn't then it should send a critical service check
        # self.service_check("can_connect", OpenMetricsBaseCheckV2.CRITICAL)
