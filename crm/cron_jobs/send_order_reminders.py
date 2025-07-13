import requests
from datetime import datetime, timedelta

# Define the GraphQL query
query = """
query {
  orders(orderDate_Gte: "{start_date}", orderDate_Lte: "{end_date}") {
    id
    customer {
      email
    }
  }
}
"""

# Calculate the date range for the last 7 days
end_date = datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

# Format the query with the date range
formatted_query = query.format(start_date=start_date, end_date=end_date)

# Send the GraphQL request
response = requests.post(
    'http://localhost:8000/graphql',
    json={'query': formatted_query}
)

# Check the response
if response.status_code == 200:
    data = response.json()
    orders = data.get('data', {}).get('orders', [])

    # Log the orders
    with open('/tmp/order_reminders_log.txt', 'a') as log_file:
        for order in orders:
            order_id = order['id']
            customer_email = order['customer']['email']
            log_file.write(f"{datetime.now()} - Order ID: {order_id}, Customer Email: {customer_email}\n")

    print("Order reminders processed!")
else:
    print(f"Failed to fetch orders: {response.status_code}")
