"""
Django settings for ratemyrig project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
if os.path.exists("env.py"):
    import env


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [os.environ.get('C9_HOSTNAME')]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # own apps
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'comments.apps.CommentsConfig',
    # third party apps
    'crispy_forms',
    'django_resized',
    'django_filters',

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

ROOT_URLCONF = 'ratemyrig.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.environ.get(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ratemyrig.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# to get messages module to work with cloud 9 
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# top level direcotry for base.html CSS and SASS
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )

# NOTE! when using built in login class base view by django
# after loggin in - it will automatically redirects to "accounts/profile"
# this will overwrite that feature and we get to redirect to a given url!
LOGIN_REDIRECT_URL='blog-home'

# link to use if the user tries to access links that are only
# accessible when they are authenticated(loggged in)
# e.g user/profile will now return a 404 error instead of a blank page(no user data to show
# since there isnt a user logged in)
LOGIN_URL='user-login'



# MEDIA_ROOT - is the directory where we want django to store the media! such as profile pics
# also note that the media isnt being stored in the database for performance purposes
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')    # BASE_DIR - is the project's base directory, and "media" is being added at the end

# MEDIA_URL - is the public url of MEDIA_ROOT  
# that's how we access the media through the browser
MEDIA_URL = '/media/' 

# ----------------------- THIRD PARTY APP SETTINGS ---------------------------
# CRISPP_FORM - by default crispy_forms defaults to bootstrap 2
#               since that's wayy too old , we're change it to bootstrap 4
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# django_resized settings to force the format of the resized image 
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'PNG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'PNG': ".png"}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
