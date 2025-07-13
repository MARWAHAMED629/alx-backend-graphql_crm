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

def update_low_stock():
    # Define the GraphQL mutation
    mutation = gql("""
    mutation {
        updateLowStockProducts {
            success
            updatedProducts
        }
    }
    """)

    # Execute the mutation
    try:
        transport = RequestsHTTPTransport(
            url='http://localhost:8000/graphql',
            verify=True,
            retries=3
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)
        response = client.execute(mutation)

        # Log the updated products
        with open('/tmp/low_stock_updates_log.txt', 'a') as log_file:
            log_file.write(f"{datetime.now()} - {response['updateLowStockProducts']['success']}\n")
            for product in response['updateLowStockProducts']['updatedProducts']:
                log_file.write(f"{product}\n")

        print("Low stock products updated successfully!")
    except Exception as e:
        print(f"Error updating low stock products: {e}")
