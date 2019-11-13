import json
import requests
import logging
import asyncio
logger = logging.getLogger(__name__)


def build(kubos_sat, service):
    kubos_sat.definitions[service] = {
        "display_name": service,
        "description": f"GraphQL Request to the {service}",
        "tags": ["Raw GraphQL"],
        "fields": [
            {"name": "ip", "type": "string",
                "value": kubos_sat.ip},
            {"name": "port", "type": "string",
                "value": kubos_sat.config[service]["addr"]["port"]},
            {"name": "graphql", "type": "text", "default": "{ping}"}
        ]
    }


def raw_graphql(graphql, ip, port, gateway, command_id):
    """GraphQL Request Command"""
    result = query(graphql=graphql, ip=ip, port=port)

    if 'errors' in result:
        logger.error(
            f"GraphQL Command Failed: {result['errors']}")
        asyncio.ensure_future(gateway.fail_command(
            command_id=command_id,
            errors=[f"GraphQL Request Failed: {result['errors']}"]))
    else:
        asyncio.ensure_future(gateway.complete_command(
            command_id=command_id,
            output=json.dumps(result)))


def query(graphql, ip, port):
    """GraphQL Query"""
    logger.debug(graphql)
    url = f"http://{ip}:{port}/graphql"
    request = requests.post(
        url,
        json={
            'query': graphql
        })

    json_result = request.json()
    logger.debug(json.dumps(json_result, indent=2))
    return json_result
