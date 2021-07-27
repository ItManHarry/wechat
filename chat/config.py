import os
dev_db = os.getenv('DEV_DB')
pro_db = os.getenv('PRO_DB')
class AppGlobalConfig():
    SECRET_KEY = os.getenv('', '1234566789wsxcderfv%$#ikujolsdfd')
class AppDevelopConfig(AppGlobalConfig):
    # 数据库配置
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOP_DATABASE_URL', dev_db)
class AppProductConfig(AppGlobalConfig):
    # 数据库配置
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOP_DATABASE_URL', pro_db)
setting = {
    'dev_setting': AppDevelopConfig,
    'pro_setting': AppProductConfig
}