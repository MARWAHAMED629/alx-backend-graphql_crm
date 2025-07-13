import requests
from datetime import datetime

def log_crm_heartbeat():
    # Log the heartbeat message
    with open('/tmp/crm_heartbeat_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now().strftime('%d/%m/%Y-%H:%M:%S')} CRM is alive\n")

    # Optionally query the GraphQL hello field
    try:
        response = requests.post(
            'http://localhost:8000/graphql',
            json={'query': '{ hello }'}
        )
        if response.status_code == 200:
            print("GraphQL endpoint is responsive.")
        else:
            print("GraphQL endpoint is not responsive.")
    except Exception as e:
        print(f"Error querying GraphQL endpoint: {e}")
