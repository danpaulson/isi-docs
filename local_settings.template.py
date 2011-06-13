import iptools

DEBUG = True

TEMPLATE_DEBUG = DEBUG

MEDIA_URL = '/files/'

ADMIN_MEDIA_PREFIX = '/files/admin/'

# format: {current directory name}.urls
ROOT_URLCONF = 'django_template.urls'

DATABASES = {
	'default': {
		'HOST': '',
		'ENGINE': 'django.db.backends.mysql',
		'USER': '',
		'PASSWORD': '',
		'NAME': '',
	},
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '6_mczf!*_*r=pz9lb#mnk*-im!lt3obxlk!pzht^)$rllwk@jx'

# Email Configuration
EMAIL_HOST = "localhost"
SERVER_EMAIL = "root@localhost"
EMAIL_PORT = 25

ADMINS = (
	# ('Your Name', 'Email', 'Username'),
)

MANAGERS = ADMINS

# logging settings
INTERNAL_IPS = iptools.IpRangeList(
    '127.0.0.1',                # single ip
    ('10.171.155.1', '10.171.155.255'),  # Library
    ('10.173.87.1', '10.173.87.255'),  # P2
)

# Django Debugging Toolbar
DEBUG_TOOLBAR_CONFIG = { 'INTERCEPT_REDIRECTS': False }

# Session Setup in seconds
SESSION_COOKIE_AGE = 60*60

#Cache Settings
CACHE_EXPIRES = 0 # 30 minutes
#CACHE_BACKEND = 'db://cache'
#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'