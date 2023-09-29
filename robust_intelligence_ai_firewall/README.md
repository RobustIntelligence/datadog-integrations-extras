# Agent Check: Robust Intelligence AI Firewall

## Overview

The Robust Intelligence AI Firewall Integration brings the performance metrics of your Firewall to your monitoring dashboards.

## Setup

Follow the instructions below to install and configure this check for an Agent running on a host. For containerized environments, see the [Autodiscovery Integration Templates][4] for guidance on applying these instructions.

### Installation

For Agent v7.21+ / v6.21+, follow the instructions below to install the Robust Intelligence AI Firewall check on your host. See [Use Community Integrations][3] to install with the Docker Agent or earlier versions of the Agent.

1. Run the following command to install the Agent integration:

   ```shell
   datadog-agent integration install -t datadog-robust-intelligence-ai-firewall==<INTEGRATION_VERSION>
   ```

2. Configure your integration similar to core [integrations][4].

### Configuration

1. Edit the `robust_intelligence_ai_firewall.d/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's configuration directory to start collecting your Robust Intelligence AI Firewall performance data.
    ```yaml
    init_config:

    instances:
        ## @param metrics_endpoint - string - required
        ## The URL to Robust Intelligence AI Firewall 
        ## internal metrics per loaded plugin in Prometheus
        ## format.
        #
      - metrics_endpoint: http://localhost:8080/metrics
    ```
   See the [sample fluentbit.d/conf.yaml][5] file for all available configuration options.

2. [Restart the Agent][6].

### Validation

[Run the Agent's status subcommand][7] and look for `robust_intelligence_ai_firewall` under the Checks section.

## Data Collected

### Metrics

Robust Intelligence AI Firewall does not include any metrics.

### Service Checks

Robust Intelligence AI Firewall does not include any service checks.

### Events

Robust Intelligence AI Firewall does not include any events.

## Troubleshooting

Need help? Contact [Datadog support][3].

[1]: **LINK_TO_INTEGRATION_SITE**
[2]: https://app.datadoghq.com/account/settings/agent/latest
[3]: https://docs.datadoghq.com/agent/kubernetes/integrations/
[4]: https://github.com/DataDog/integrations-extras/blob/master/robust_intelligence_ai_firewall/datadog_checks/robust_intelligence_ai_firewall/data/conf.yaml.example
[5]: https://docs.datadoghq.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[6]: https://docs.datadoghq.com/agent/guide/agent-commands/#agent-status-and-information
[7]: https://github.com/DataDog/integrations-extras/blob/master/robust_intelligence_ai_firewall/metadata.csv
[8]: https://github.com/DataDog/integrations-extras/blob/master/robust_intelligence_ai_firewall/assets/service_checks.json
[9]: https://docs.datadoghq.com/help/

