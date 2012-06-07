# Configuration
HOST = 'http://domainForTest.loc'

# absolute or relative path to access nginx log
PATH_TO_NGINX_ACCESS_LOG = '/var/log/nginx/access.log.1'

# Absolute or relative path to directory were is putting log files
PATH_TO_LOG = 'logs/'

# count latest bites from access log for analize (zero - parsing all file)
COUNT_LATEST_BITES = 2*1024*1024

# count threading
COUNT_THREADING = 8

# print current status every PRINT_STATUS_COUNT urls
PRINT_STATUS_COUNT = 1

# no checked url with substring in logs of string
FAKE_SUBSTR = ['POST', 'check', 'Zabbix', '/media/', '/static/']

# credentional for Django sites
DJANGO_ADMIN_LOGIN = 'dev'
DJANGO_ADMIN_PASSWORD = 'pool'
