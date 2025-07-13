# Ensure INSTALLED_APPS is defined
INSTALLED_APPS = [
    # ...existing apps...
    'django_crontab',
]

# Add the cron job configuration
CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.log_crm_heartbeat'),
    ('0 */12 * * *', 'crm.cron.update_low_stock'),
]