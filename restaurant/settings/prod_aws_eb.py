
from .common import *
import os


# DEBUG = False  # sentry를 통한 에러로깅

import pymysql
pymysql.install_as_MySQLdb() # pymysql이 MySQLdb처럼 동작토록 세팅

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.mysql'),
        'HOST': 'restaurant.cmras9lkaqpw.ap-northeast-2.rds.amazonaws.com',
        'USER': 'restaurant',
        'PASSWORD': 'qhdordmlgla!',
        'NAME': 'restaurant',
        'PORT': 3306,
    },
}

INSTALLED_APPS += ['storages']

# django-storages 앱 의존성 추가
# 기본 static/media 저장소를 django-storages로 변경
STATICFILES_STORAGE = 'restaurant.storages.StaticS3Boto3Storage'
DEFAULT_FILE_STORAGE = 'restaurant.storages.MediaS3Boto3Storage'

# S3 파일 관리에 필요한 최소 설정
# 소스코드에 설정정보를 남기지마세요. 환경변수를 통한 설정 추천
AWS_ACCESS_KEY_ID = 'AKIAIU3YS4OO24ICPLXQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'restaurant3' # 필수 지정
AWS_S3_REGION_NAME = 'ap-northeast-2'
