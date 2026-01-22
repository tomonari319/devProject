import os
from pathlib import Path
from dotenv import load_dotenv

# .envファイルを読み込む（ローカル用）
load_dotenv()

# プロジェクトのベースディレクトリ
BASE_DIR = Path(__file__).resolve().parent.parent

# --- セキュリティ設定 ---

# Renderの環境変数にSECRET_KEYがあればそれを使う。なければデフォルト（ローカル用）
SECRET_KEY = os.getenv('SECRET_KEY', "django-insecure-+uu^ewne%ngysr%49bejjr8#zwzgs#@y^n&sn#b1v-s%pc%w7)")

# 重要：Render上では DEBUG=False になるように設定
# 環境変数 DEBUG が 'True' の時だけ True になり、それ以外（Render等）は False になる
DEBUG = os.getenv('DEBUG') == 'True'

# 全てのホストと、Renderのドメインを許可
ALLOWED_HOSTS = ['*']
if os.getenv('RENDER_EXTERNAL_HOSTNAME'):
    ALLOWED_HOSTS.append(os.getenv('RENDER_EXTERNAL_HOSTNAME'))

# --- アプリケーション定義 ---

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    "testApp", 
    # 'debug_toolbar',  # 本番環境でのエラー回避のため無効化
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # 静的ファイルを本番で配信するための設定（WhiteNoiseを入れるのが理想ですが、まずは標準）
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 'debug_toolbar.middleware.DebugToolbarMiddleware', # 無効化
]

ROOT_URLCONF = "devProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "devProject.wsgi.application"

# --- データベース ---
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --- パスワードバリデーション ---
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- 国際化 ---
LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_TZ = True

# --- 静的ファイル設定 ---
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] if os.path.exists(os.path.join(BASE_DIR, 'static')) else []

# --- ログイン・セキュリティ追加設定 ---
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_REDIRECT_URL = '/'

# Render（HTTPS）でのCSRF対策
if not DEBUG:
    CSRF_TRUSTED_ORIGINS = [f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}"]
else:
    CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000', 'http://localhost:8000']