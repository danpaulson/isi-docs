import os, sys

PROJECT_ROOT = os.path.dirname(__file__)

MEDIA_ROOT = PROJECT_ROOT + '/files/'

sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
#	  'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
	# django middleware
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.middleware.transaction.TransactionMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

TEMPLATE_DIRS = (
	PROJECT_ROOT + '/templates',
)

AUTH_PROFILE_MODULE = 'userprofile.UserProfile'

INSTALLED_APPS = (
	# django apps
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.admin',
	'django.contrib.messages',
	
	# local project apps
	'common',
	'userprofile',
	'docmanager',
)

try:
	from local_settings import *
except ImportError:
	pass