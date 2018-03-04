STATIC_ROOT = '/var/www/django-two/static/'

DEBUG = False
ALLOWED_HOSTS = [
    "ec2-13-125-167-5.ap-northeast-2.compute.amazonaws.com"
]

print("Loaded settings for deployment using Apache and WSGI")
