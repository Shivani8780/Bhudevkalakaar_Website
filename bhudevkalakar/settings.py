from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-rn#t@=jp5%4up41-v8h*-mmg81*m+kb06$zv9!qq^@x^#5zc^y'

DEBUG = True


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '79977cbb1ead.ngrok-free.app',
    'bhudevkalakaar-bhudevnetwork.pythonanywhere.com',  # ✅ corrected
]






INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main',  # ✅ new project
    'grappelli',  # ✅ old project
    'old_project.registration',  # ✅ old project
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

ROOT_URLCONF = 'bhudevkalakar.urls'

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

WSGI_APPLICATION = 'bhudevkalakar.wsgi.application'

# ✅ Multiple Databases
DATABASES = {
    "default": {  # new project DB
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "old": {  # old project DB
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "old_project/db.sqlite3",
    },
}

# ✅ Tell Django how to route models to DBs
DATABASE_ROUTERS = ["old_project.db_router.OldProjectRouter"]

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# ✅ Static files (CSS, JS, Images)
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "old_project/static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"  # required for collectstatic

# ✅ Media files (uploads)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ✅ CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    "https://79977cbb1ead.ngrok-free.app",
    "https://bhudevkalakaar-bhudevnetwork.pythonanywhere.com",  # ✅ corrected
]



 # Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

