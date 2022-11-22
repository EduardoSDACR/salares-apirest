from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

'''
#Using SQL Server
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),

        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
}
'''

#Using SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}