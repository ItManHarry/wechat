import os
dev_db = os.getenv('DEV_DB')
pro_db = os.getenv('PRO_DB')
test_db = os.getenv('TEST_DB')
class AppGlobalSetting():
    SECRET_KEY = os.getenv('SECRET_KEY', '1234566789wsxcderfv%$#ikujolsdfd')
    GITHUB_OAUTH_URL = 'http://github.com/login/oauth/authorize'
class AppDevelopSetting(AppGlobalSetting):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOP_DATABASE_URL', dev_db)
class AppTestSetting(AppGlobalSetting):
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', test_db)
        WTF_CSRF_ENABLED = False
        TESTING = True
class AppProductSetting(AppGlobalSetting):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('PRODUCT_DATABASE_URL', pro_db)
settings = {
    'dev_setting': AppDevelopSetting,
    'pro_setting': AppProductSetting,
    'test_setting': AppTestSetting
}