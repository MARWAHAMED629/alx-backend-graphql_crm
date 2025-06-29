# ALX Backend GraphQL CRM

A CRM system built with **Django** and **GraphQL** using the `graphene-django` library. This project is part of the ALX backend specialization and demonstrates how to build and query a GraphQL API integrated with Django models.

---

## 🚀 Features

- GraphQL endpoint with `graphene-django`
- CRUD operations for:
  - Customers
  - Products
  - Orders
- Bulk creation of customers
- Nested mutations with validation
- Filtering, pagination, and ordering using `django-filter`
- Schema introspection and GraphiQL explorer enabled

---

## 🧱 Project Structure
alx-backend-graphql_crm/
├── crm/ # Django app for CRM logic
│ ├── models.py # Models: Customer, Product, Order
│ ├── schema.py # GraphQL types and mutations
│ ├── filters.py # django-filter classes
├── graphql_crm/ # Project config (settings, urls)
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── schema.py # Main GraphQL schema
├── manage.py # Django CLI entrypoint
└── README.md


---

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/MARWAHAMED629/alx-backend-graphql_crm.git
cd alx-backend-graphql_crm

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
