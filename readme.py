import unittest  # 导入unittest
import requests
import json
import jsonpath
import re
from config import config
from app import test_user_login

class TestUserLogin(unittest.TestCase):  # 类必须Test开头，继承TestCase才能识别为用例类
      path = '/user/userInfo'

      def test_user_info(self):
          #data = {"userId":self.test_get_userId()}
          data = {"userId":self.test_get_userId()}
          res = requests.post(url=config.url+self.path, data=json.dumps(data),headers = config.headers)
          print("userInfo",res.text)


      def test_get_userId(self):   # 前台登录
          path = '/user/login'
          url = 'http://192.168.2.7:8082'
          data = '{"phoneNumber":"19921111111","passWord":"111111"}'
          res = requests.post(url=url+path, data=data)
          #print(res.text)
          self.assertIn('success', res.text)  # 断言
          json_obj = json.loads(res.text)
          #print(json_obj)
          userid1 = jsonpath.jsonpath(json_obj,"$.data.userId")
          userid2 = json_obj["data"]["userId"]
          #print(userid1)
          print("userId",userid2)
          return userid2


if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2)    # 运行本测试类所有用例,verbosity为结果显示级别
