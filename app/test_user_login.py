import unittest  # 导入unittest
import requests
import json
import jsonpath
from config import config

class TestUserLogin(unittest.TestCase):  # 类必须Test开头，继承TestCase才能识别为用例类
    path = '/user/login'
    phoneNumber = '18667028889'
    passWord = '111111'
    passWord_wrong = '111112'
    def test_user_login_normal  (self):   # 前台登录
        data = {"phoneNumber":self.phoneNumber,"passWord":self.passWord}
        res = requests.post(url=config.url+self.path, data=json.dumps(data),headers = config.headers)
        res_dict = res.json()   # 将响应转为json对象（字典）等同于`json.loads(res.text)`
        #print("Response Body:    ",json.dumps(res_dict, indent=2, sort_keys=True, ensure_ascii=False))
        #self.assertIn('msg', res.text)  # 断言
        json_obj = json.loads(res.text)
        userid = jsonpath.jsonpath(json_obj,"$.data.userId")        #userid = json_obj["data"]["userId"]
        print ("userId:      ",userid[0])
        return userid[0]

'''
    def test_print_userid(self):   # 前台登录
        print("1")
        #print("userId",self.test_user_login_normal())
        print("2")

    def test_user_login_password_wrong(self):
        data = {"phoneNumber":self.phoneNumber,"passWord":self.passWord_wrong}
        res = requests.post(url=config.url+self.path, data=json.dumps(data),headers = config.headers)
        print(res.text)
        self.assertIn('密码错误', res.text)  # 断言
'''

if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2)    # 运行本测试类所有用例,verbosity为结果显示级别



