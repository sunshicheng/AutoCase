"""
Author    : Mr. Sun.
FileName  : main.py
Time      : 2021/12/13 9:34 AM
Desc      :  执行文件
 pytest main.py --html=./report/report.html --self-contained-html

"""
import pytest
import json
import requests

from util.orthogonal_generate import params_parametrize, create_case
from util.tools import saasHeaders
from config.url_router import UrlRouter as ur



# 定义使用
def saas_permission():
    payload = {
        'title': '用户权限查询',
        'interface': '/galaxy-go/crm/staff/get-permission',
        'method': 'GET',
        'Content-Type': 'application/x-www-form-urlencoded',
        'params':
            {'account':
                 {'type': 'text',
                  'range': ['sunshicheng', '297999'],
                  'iscompulsory': '1'
                  }
             }
    }
    case_group = create_case(payload=payload)
    return case_group


class TestBenchmark(object):
    data, id_list = saas_permission()

    # 通过ids 给方法进行重新命名
    @pytest.mark.parametrize("title,inter,method,params", data,
                             ids=id_list)
    def test_requests(self, title, inter, method, params):
        # 添加描述 函数
        # test_requests.__doc__ = title
        # 类
        url = ur.env['test'] + inter
        self.test_requests.__func__.__doc__ = title
        if method == 'POST':
            print("请求参数 : ", json.dumps(params, ensure_ascii=False))
            print("请求方式: ", method)
            print("返回结果 ")
        elif method == 'GET':
            print("请求参数 : ", json.dumps(params, ensure_ascii=False))
            response = requests.get(url=url, params=params, headers=headers)
            print("返回code : ", response.status_code)
            print("返回结果 : ", response.text, '\n')


if __name__ == '__main__':
    saas_permission()