from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

# =============================
# SECURITY
# =============================
SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-change-this-in-production"
)

DEBUG = True   # Render वर test साठी OK

ALLOWED_HOSTS = ["*"]   # Render + local testing

# =============================
# APPLICATIONS
# =============================
INSTALLED_APPS = [
    "corsheaders",   # 👈 MUST be first

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "store",
]

# =============================
# MIDDLEWARE (ORDER IS CRITICAL)
# =============================
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # 👈 FIRST

    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# =============================
# CORS SETTINGS
# =============================
CORS_ALLOW_ALL_ORIGINS = True

# =============================
# URLS & WSGI
# =============================
ROOT_URLCONF = "Furniture_store_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Furniture_store_backend.wsgi.application"

# =============================
# DATABASE (Render PostgreSQL)
# =============================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT", default="5432"),
    }
}

# =============================
# PASSWORD VALIDATION
# =============================
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# =============================
# INTERNATIONALIZATION
# =============================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# =============================
# STATIC & MEDIA
# =============================
STATIC_URL = "/static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# =============================
# DEFAULT PK
# =============================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"