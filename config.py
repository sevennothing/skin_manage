import os
#from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
#load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
	# CSRF_ENABLED 激活 跨站点请求伪造 保护。在大多数情况下，你需要激活该配置使得你的应用程序更安全些
	CSRF_ENABLED = True
	# SECRET_KEY 配置仅仅当 CSRF 激活的时候才需要,
	# 它是用来建立一个加密的令牌，用于验证一个表单。当你编写自己的应用程序的时候，请务必设置很难被猜测到密钥。
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	#SQLALCHEMY_DATABASE_URI = 'mysql://root:18208158923@localhost:3306/skin_db?charset=utf8mb4'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_MIGRATE_REPO = 'app.db'
	SQLALCHEMY_DATABASE_URI = 'mysql://root:18208158923@localhost:3306/skin_db?charset=utf8mb4'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	ADMINS = ['sevennothing@hotmail.com']
	LANGUAGES = ['en', 'es']
	MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
	ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
	POSTS_PER_PAGE = 25
