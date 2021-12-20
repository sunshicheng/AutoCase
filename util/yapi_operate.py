"""
Author    : Mr. Sun.
FileName  : yapi_operate.py
Time      : 2021/12/13 9:45 AM
Desc      :  对yapi 接口进行操作
"""
# import json
import requests
from config.static_config import Static as si


def get_detail(inter_id):
    url = si.URI + si.URL_MAP['id_detail']
    payload = {
        "id": str(inter_id),
        "token": ""  # yapi对应的token
    }
    response = requests.get(url=url, params=payload).json()
    # print(json.dumps(response, indent=2, ensure_ascii=False))

    # 解析结果 获取需要的值
    result = {}
    # 接口基本信息

    title = response['data']['title']
    result['title'] = title
    path = response['data']['query_path']['path']
    result['interface'] = path
    method = response['data']['method']
    result['method'] = method
    # 处理headers
    for j in response['data']['req_headers']:
        result[j['name']] = j['value']
    # 请求参数
    """
    根据接口返回判断 只要有req_body_form 就会有必填 和 非必填
    如果全部都是非必填 req_query
    注意 字典覆盖 还有定义
    """
    result['params'] = {}
    if 'req_body_form' in response['data'].keys() and len(response['data']['req_body_form']) > 0:
        for i in response['data']['req_body_form']:
            name = i['name'].strip()
            result['params'][name] = {}
            if 'type' in list(i.keys()):
                result['params'][name]['type'] = i['type']
            else:
                result['params'][name]['type'] = 'number'
            if 'required' in list(i.keys()):
                result['params'][name]['iscompulsory'] = i['required']
            else:
                result['params'][name]['iscompulsory'] = 0
    elif 'req_query' in response['data'].keys() and len(response['data']['req_query']) > 0:
        for i in response['data']['req_query']:
            # 处理一下 name 去除特殊字符
            name = i['name'].strip()
            result['params'][name] = {}
            if 'type' in list(i.keys()):
                result['params'][name]['type'] = i['type']
            else:
                result['params'][name]['type'] = 'number'
            if 'required' in list(i.keys()):
                result['params'][name]['iscompulsory'] = i['required']
            else:
                result['params'][name]['iscompulsory'] = 0
    return result

# if __name__ == '__main__':
#     temp = get_detail(4250)
#     print(json.dumps(temp, indent=2, ensure_ascii=False))
