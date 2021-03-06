"""
Django settings for universe project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import os

from configurations import Configuration, values


class Common(Configuration):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    
    # Absolute filesystem path to the project directory:
    PROJECT_ROOT = os.path.dirname(__file__)

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)

    ALLOWED_HOSTS = values.ListValue(environ_name='ALLOWED_HOSTS')

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django_extensions',
        'djangoseo',
        'apps.notes',
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

    ROOT_URLCONF = 'universe.urls'
    
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
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

    WSGI_APPLICATION = 'universe.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/1.11/ref/settings/#databases
    DATABASES = values.DatabaseURLValue(
        'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
    )

    # Password validation
    # https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
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
    # https://docs.djangoproject.com/en/1.11/topics/i18n/
    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True
    
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.11/howto/static-files/
    STATIC_URL = '/static/'
    
    # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = (
        os.path.normpath(os.path.join(PROJECT_ROOT, 'static')),
    )

    STATIC_ROOT = os.path.join(BASE_DIR, 'public')

    SITE_ID = 1


class Development(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = True

    INTERNAL_IPS = [
        '127.0.0.1'
    ]

    INSTALLED_APPS = Common.INSTALLED_APPS + [
        'debug_toolbar'
    ];

    MIDDLEWARE = Common.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]

    def show_toolbar(request):
        return True
        
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
    }


class Staging(Common):
    """
    The in-staging settings.
    """
    # Security
    #SESSION_COOKIE_SECURE = values.BooleanValue(True)
    #SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    #SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    #SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    #SECURE_HSTS_SECONDS = values.IntegerValue(31536000)
    #SECURE_REDIRECT_EXEMPT = values.ListValue([])
    #SECURE_SSL_HOST = values.Value(None)
    #SECURE_SSL_REDIRECT = values.BooleanValue(True)
    #SECURE_PROXY_SSL_HEADER = values.TupleValue(
    #    ('HTTP_X_FORWARDED_PROTO', 'https')
    #)


class Production(Staging):
    """
    The in-production settings.
    """
    pass
