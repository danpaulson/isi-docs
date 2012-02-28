MAINTENANCE = False
DEBUG = True

TEMPLATE_DEBUG = DEBUG

MEDIA_URL = '/files/x'

ADMIN_MEDIA_PREFIX = '/files/admin/'

ROOT_URLCONF = 'urls'

LOGIN_REDIRECT_URL = '/a/'

DATABASES = {
	'default': {
		'HOST': 'localhost',
		'ENGINE': 'django.db.backends.mysql',  # change to: django.db.backends.mysql for MySQL
		'USER': '',
		'PASSWORD': '',
		'NAME': '',
	},
}

SECRET_KEY = 'LONG_RANDOM_SECRET_KEY'

ADMINS = (
	('Dan Paulson', 'danpaulson@gmail.com', 'dan'),
)
MANAGERS = ADMINS

SESSION_COOKIE_AGE = 1209600