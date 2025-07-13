#!/bin/bash
# Script to delete customers with no orders in the past year and log the result

cd "$(dirname "$0")/../.."

COUNT=$(python manage.py shell -c "from crm.models import Customer, Order; from django.utils import timezone; from datetime import timedelta; one_year_ago = timezone.now() - timedelta(days=365); to_delete = Customer.objects.exclude(order__created_at__gte=one_year_ago); deleted, _ = to_delete.delete(); print(deleted)")

echo "$(date '+%Y-%m-%d %H:%M:%S') - Deleted $COUNT inactive customers" >> /tmp/customer_cleanup_log.txt
