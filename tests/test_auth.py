from tests.base import BaseTestCase
import unittest
from flask import url_for
class AuthTestCase(BaseTestCase):
    #测试登录
    def test_login_user(self):
        response = self.login()
        data = response.get_date(as_text=True)
        print(data)
if __name__ == '__main__':
    unittest.main()