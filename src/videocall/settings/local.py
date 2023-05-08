import json
from pathlib import Path


with open('/etc/novavideocall/config.json') as config_file:
    config = json.load(config_file)



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
BASE_URL = 'http://127.0.0.1:8000'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5b@qjt3lrh$e4#84o16!8v##h&@pst+q$le8=c0#_hxja)v=9i"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'core.apps.CoreConfig',
    'taggit',
    'tinymce',
    'widget_tweaks',
    'imagekit',
    'rest_framework',
    'about.apps.AboutConfig',
    'contactus.apps.ContactusConfig', 
    'api.apps.ApiConfig',
    'footer.apps.FooterConfig',
    'pricing.apps.PricingConfig',
    'socialmedialinks.apps.SocialmedialinksConfig',
    'publishapp.apps.PublishappConfig',
    'testimonials.apps.TestimonialsConfig',
    'homepage.apps.HomepageConfig',
    'guidance.apps.GuidanceConfig',
    'careers.apps.CareersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SITE_ID = 1
ROOT_URLCONF = 'videocall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.seo_attr',
                'core.context_processors.twitter_seo_attr',
                'core.context_processors.og_seo_attr',
            ],
        },
    },
]

SECURE_SSL_REDIRECT = False
WSGI_APPLICATION = 'videocall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]

STATIC_ROOT = BASE_DIR.parent / 'static_cdn'


MEDIA_URL = 'media/'

MEDIA_ROOT =  BASE_DIR.parent / 'media_cdn'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


'''
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s'
        }
    },

    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './logs/debug.log',
        },

        'gunicorn': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': './logs/gunicorn.errors',
            'maxBytes': 1024 * 1024 * 100,  # 100 mb
        }

    },

    'loggers': {
        'django': {
            'handlers': ['file', 'gunicorn'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
'''
