import os, unittest, uuid
from flask import url_for
from chat import create_app
from chat.plugins import db
from chat.models import User
from chat.forms import LoginForm
os.environ['GITHUB_CLIENT_ID'] = 'test'
os.environ['GITHUB_CLIENT_SECRET'] = 'test'
class BaseTestCase(unittest.TestCase):

    def setUp(self):
        app = create_app('test_setting')
        self.context = app.test_request_context()   #创建上下文
        self.context.push()                         #推送上下文
        self.client = app.test_client()
        self.runner = app.test_cli_runner()
        #初始化数据库
        db.create_all()
        #创建管理员
        user = User(
            id=uuid.uuid4().hex,
            code='admin',
            name='admin',
            email='admin@163.com',
            website='http://xxx.com',
            github='http://github.com/admin',
            bio='The system administrator'
        )
        user.set_password('12345678')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.drop_all()
        self.context.pop()  #销毁上下文

    def login(self, code=None, password=None):
        if code is None and password is None:
            code = 'admin'
            password = '12345678'
        form = LoginForm()
        form.code.data = code
        form.password.data = password
        return self.client.post(url_for('auth.login'), data=dict(form=form), follow_redirects=True)

    def logout(self):
        return self.client.get(url_for('auth.logout'), follow_redirects=True)