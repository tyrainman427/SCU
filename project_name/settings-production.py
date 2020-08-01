from . settings import *

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'silverci_scu',
'USER': 'silverci_etnuh427',
'PASSWORD': os.environ['DB_PASSWORD'],
'HOST': 'localhost',
    }
}
