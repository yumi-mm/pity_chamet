# 基础配置类
import os

class Config(object):
    # log文件路径
    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT,'logs','pity.log')
    # Flask jsonify编码问题
    JSON_AS_ASCII = False

    # mock server
    MYSQL_HOST = "localhost"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PWD = "123456"
    DBNAME = "pity"

    # MySQL配置 init sqlalchemy (used by apscheduler)
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
        MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
