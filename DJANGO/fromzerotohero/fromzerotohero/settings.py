"""
admin
123

"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '**=#!s*blt6ua_uoiuzi7zucauy7yak%tn5sa*26g5is!q0de9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Our Apps
    'main.apps.MainConfig',
    'news.apps.NewsConfig',
    'panel.apps.PanelConfig',
    'category.apps.CategoryConfig',
    'subcategory.apps.SubcategoryConfig',
    'trending.apps.TrendingConfig',
    'users.apps.UsersConfig',
    'comments.apps.CommentsConfig',
    'django.contrib.humanize',
    'django_crontab',
    'qr_code',
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

ROOT_URLCONF = 'fromzerotohero.urls'

#AUTH_USER_MODEL = 'users.CustomUser' #hangi model ile auth işlemlerini yapabileceğimizi belirledik. app_adi.model_adi
LOGIN_URL = '/login/' # login required gibi işlemlerde nereye redirect yapacağını belirledik
SESSION_EXPIRE_AT_BROWSER_CLOSE = True # browser aç-kapa yapılınca tekrar login required olur!
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processor.get_categories',  # yazdığımız context_processors'leri dahil ettik
                'subcategory.context_processors.get_subcategories',
                'news.context_processors.get_last_news',
                'main.context_processors.get_site_settings',
                'news.context_processors.get_popular_posts',
                'trending.context_processors.get_trendings',
            ],
        },
    },
]
#_("deneme")


WSGI_APPLICATION = 'fromzerotohero.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CRONJOBS = [
    # python manage.py crontab add
    # python manage.py crontab show
    # python manage.py crontab remove
    ('*/5 * * * *', 'main.cron.my_cron')
    # her 5 saniyede 1 çalışacak crontab
]
