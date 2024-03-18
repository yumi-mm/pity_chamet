from datetime import datetime
from app import pity
from app.utils.logger import Log
from app.controller.auth.user import auth
from app import dao

# 注册蓝图
pity.register_blueprint(auth)

'''
    @pity.route("/")是一个装饰器, 代表hello_world这个函数与路由/进行绑定，
    当访问到/路由的时候，函数hello_world会自动执行。
'''
@pity.route('/')
def hello_word():
    log = Log("hello world专用")
    log.info("有人访问你的网站啦")
    now = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
    print(now)
    return now

'''
    pity.run("0.0.0.0", threaded=True, port="7777") 这句话表示启动web服务, 
    第一个参数0.0.0.0表示接受任何ip的访问，
    threaded表示如果有多人同时访问一个接口时是非阻塞的，
    port代表服务挂载的端口，这里我们以clearlove为端口号: 7777。
'''
if __name__ == "__main__":
    pity.run("0.0.0.0",port="7777")
