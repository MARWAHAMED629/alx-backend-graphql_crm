from gql.transport.requests import RequestsHTTPTransport
from gql import gql, Client

# Existing imports
import requests
from datetime import datetime

def log_crm_heartbeat():
    # Log the heartbeat message
    with open('/tmp/crm_heartbeat_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now().strftime('%d/%m/%Y-%H:%M:%S')} CRM is alive\n")

    # Optionally query the GraphQL hello field
    try:
        transport = RequestsHTTPTransport(
            url='http://localhost:8000/graphql',
            verify=True,
            retries=3
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)
        query = gql("query { hello }")
        response = client.execute(query)
        print("GraphQL endpoint response:", response)
    except Exception as e:
        print(f"Error querying GraphQL endpoint: {e}")
