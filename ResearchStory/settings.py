"""
Django settings for ResearchStory project.
Generated by 'django-admin startproject' using Django 3.2.5.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yr2d^+f(@&0^74&9f3)=n_(bd_%o49-#b7cu6yq=14u&75gce!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['https://researchstory.herokuapp.com','researchstory.herokuapp.com', '127.0.0.1']

# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #################################
    'Users',
    'Story',
    'forum',
    'comment',
    'meeting',
    'interview',
    'Videos',
    'embed_video',

    # 第三方应用程序
    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader',  # 富文本编辑器上传图片模块
    'mptt',
    'password_reset',

    # allauth 启动必须项
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # 可添加需要的第三方登录
    'allauth.socialaccount.providers.github',

]
# 媒体文件配置
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

CKEDITOR_UPLOAD_PATH = "img"  # 上传图片保存路径，如果没有图片存储或者使用自定义存储位置，那么则直接写  ' ' ,如果是使用django本身的存储方式，那么你就指名一个目录用来存储即可。
# CKEDITOR_IMAGE_BACKEND = 'pillow'
# 富文本编辑器ckeditor配置
CKEDITOR_CONFIGS = {
    # （1）默认配置
    # 'default': {
    #     'toolbar': 'full',  # 工具条功能
    #     'height': 300,  # 编辑器高度
    #     'width': 800,  # 编辑器宽
    # },

    # （3）自定义配置带代码块显示
    'default': {
        'toolbar': (
            ['div', 'Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', 'Scayt'],
            ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat'],
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks', '-', 'About', 'pbckcode'],
            ['Blockquote', 'CodeSnippet'],
        ),
        'width': 'auto',
        # 添加按钮在这里
        'toolbar_Custom': [
            ['NumberedList', 'BulletedList'],
            ['Blockquote', 'CodeSnippet'],
        ],
        # 插件
        'extraPlugins': ','.join(['codesnippet', 'widget', 'lineutils', ]),
    },
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ResearchStory.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'ResearchStory.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test1',
        'USER': 'postgres',
        'PASSWORD': '93239323',
        'HOST': 'comp9323-postgres.c4ewkd5opwpk.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
AUTH_USER_MODEL = 'Users.User'

AUTHENTICATION_BACKENDS = [
    # Django 后台可独立于 allauth 登录
    'django.contrib.auth.backends.ModelBackend',
    # 配置 allauth 独有的认证方法，如 email 登录
    'allauth.account.auth_backends.AuthenticationBackend',
]

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# abc
# user login required
LOGIN_URL = 'Users/login/'

# abc


# SMTP服务器
EMAIL_HOST = 'smtp.gmail.com'
# 邮箱名
EMAIL_HOST_USER = 'your email'
# 邮箱密码
EMAIL_HOST_PASSWORD = 'your password'
# 发送邮件的端口
EMAIL_PORT = 587
# 是否使用 TLS
EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
# 默认的发件人
DEFAULT_FROM_EMAIL = 'tracyguoji@gmail.com'

# 设置站点
SITE_ID = 1

# 登录成功后重定向地址
LOGIN_REDIRECT_URL = '/'
