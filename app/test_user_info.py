import unittest  # 导入unittest
import requests
import json
import jsonpath
import re
from config import config
from app import test_user_login

class TestUserInfo(unittest.TestCase):  # 类必须Test开头，继承TestCase才能识别为用例类
      path = '/user/userInfo'
      def test_user_info(self):
          d = test_user_login.TestUserLogin.test_user_login_normal(test_user_login.TestUserLogin)
          data ={"userId" : d }
          print("POST data:",data)
          res = requests.post(url=config.url+self.path, data=json.dumps(data),headers = config.headers)
          res_dict = res.json() # 将响应转为json对象（字典）等同于`json.loads(res.text)`
          print("Response Body:",json.dumps(res_dict, indent=2, sort_keys=True, ensure_ascii=False))
          self.assertIn('success', res.text)  # 断言

if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2)    # 运行本测试类所有用例,verbosity为结果显示级别
