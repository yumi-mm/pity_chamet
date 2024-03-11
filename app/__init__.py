from flask import Flask
from config import Config

# 这是flask的约定用法, 引入Flask类并实例化了一个Flask对象, 其中__name__为通俗写法。
# 得到一个名为"pity"的Flask实例

pity = Flask(__name__)
pity.config.from_object(Config)
