from __future__ import annotations

from split_settings.tools import include

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test_postgres",
        "USER": "postgres",
        "PASSWORD": "your-super-secret-and-long-postgres-password",
        "HOST": "pgbouncer",
        "PORT": "5432",
        "TEST": {
            "NAME": "test_postgres_temp",
        },
    },
}

include(
    "base.py",
    "logging.py",
    "application.py",
    "auth.py",
    "database.py",
    "security.py",
    "storage.py",
    "rest.py",
    "sentry.py",
    "silk.py",
    "spectacular.py",
    "celery.py",
    "cache.py",
    "axes.py",
)
