import os
dev_db = os.getenv('DEV_DB')
pro_db = os.getenv('PRO_DB')
class AppGlobalSetting():
    SECRET_KEY = os.getenv('SECRET_KEY', '1234566789wsxcderfv%$#ikujolsdfd')
class AppDevelopSetting(AppGlobalSetting):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOP_DATABASE_URL', dev_db)
class AppProductSetting(AppGlobalSetting):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOP_DATABASE_URL', pro_db)
settings = {
    'dev_setting': AppDevelopSetting,
    'pro_setting': AppProductSetting
}