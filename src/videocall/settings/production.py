import json
from django.conf import settings

with open('/home/blackrose/env/novavideocall.json') as config_file:
    config = json.load(config_file)

if not settings.DEBUG:

    from pathlib import Path

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    


    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = config['SECRET_KEY']
    

    ALLOWED_HOSTS = ['novavideocall.live', 'www.novavideocall.live']


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
        'account.apps.AccountConfig',
        'dashboard.apps.DashboardConfig',
    	'taggit',
    	'tinymce',
    	'widget_tweaks',
    	'imagekit',
    	'about.apps.AboutConfig',
    	'contactus.apps.ContactusConfig', 
    	'pricing.apps.PricingConfig',
    	'socialmedialinks.apps.SocialmedialinksConfig',
    	'publishapp.apps.PublishappConfig',
    	'testimonials.apps.TestimonialsConfig',
    	'homepage.apps.HomepageConfig',
    	'guidance.apps.GuidanceConfig',
    	'careers.apps.CareersConfig',
        'bitm.apps.BitmConfig',
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
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'videocall.wsgi.application'
    SECURE_SSL_REDIRECT = True


    # Database
    # https://docs.djangoproject.com/en/4.1/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config['DB_NAME'],
            'USER': config['DB_USER'],
            'PASSWORD': config['DB_PASS'],
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }


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
   

    STATIC_ROOT = BASE_DIR.parent / 'static_cdn'
  
    STATICFILES_DIRS = [
	BASE_DIR / 'static'
    ]

    MEDIA_URL = 'media/'

    MEDIA_ROOT =  BASE_DIR.parent / 'media_cdn'

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
  
