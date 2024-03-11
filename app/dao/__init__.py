from app.models import db
from app import pity
from app.models.user import User

# db.create_all()
# pity.app_context().push()
# 在需要执行数据库操作的地方
with pity.app_context():
    db.create_all()
# # 在操作完成后，确保在相同的上下文中推出
# pity.app_context().pop()
