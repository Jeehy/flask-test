SECRET_KEY="sadfeagegafag:lf"

# Mysql所在主机名
HOSTNAME = "127.0.0.1"
# 监听端口号 默认3306
PORT = 3306
# 主机名和密码
USERNAME = "root"
PASSWORD = "1221"
# 创建的数据库名称
DATABASE = "zhiliaooa"
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "826329938@qq.com"
MAIL_PASSWORD = "nhqorohqpidvbejh"
MAIL_DEFULT_SENDER = "826329938@qq.com"
