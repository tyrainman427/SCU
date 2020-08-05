from . settings import *

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'silverci_silvercity',
'USER': 'silverci_etnuh427',
'PASSWORD': os.environ['DB_PASSWORD'],
'HOST': 'localhost',
    }
}
