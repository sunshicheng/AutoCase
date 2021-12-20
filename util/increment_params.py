"""
Author    : Mr. Sun.
FileName  : case_generate.py
Time      : 2021/12/13 9:35 AM
Desc      : 增加params 组文件

对参数进行判断
type 不管是什么值 都统一给替换一次,目前支持的有boolean，number，string, date
range 这个支持传
是否必填 这个库里没有处理，需要自己处理
"""
import copy
import itertools


# 增加type 类型覆盖 case组
def type_increment_case(payload):
    result = []
    # 增加type case 组
    if len(payload['params']) > 0:
        type_list = ['text', 'number', 'integer']
        for type_detail in type_list:
            payload_temp = copy.deepcopy(payload)
            params_temp = payload_temp['params']
            # 获取所有的参数 对参数下的字典进行修改
            for key, value in payload['params'].items():
                if value['type'] == 'text' or value['type'] == 'number' or value['type'] == 'integer':
                    # 修改type 值
                    params_temp[key]['type'] = type_detail
            result.append(payload_temp)
    return result


# 增加必填参数校验 相关case组
def compulsory_increment_case(payload):
    result = []
    if len(payload['params']) > 0:
        compulsory_list = []
        # 获取所有的必填参数
        for key in payload['params'].keys():
            if payload['params'][key]['iscompulsory'] == '1':
                compulsory_list.append(key)

        # 必填参数组合
        combination_list = []
        for i in range(1, len(compulsory_list) + 1):
            iterm = itertools.combinations(compulsory_list, i)
            combination_list.append(list(iterm))

        # 循环遍历必填参数 然后进行删除
        for i in range(len(combination_list)):
            for j in combination_list[i]:
                payload_temp = copy.deepcopy(payload)
                params_temp = payload_temp['params']
                for keys in j:
                    params_temp.pop(keys)
                result.append(payload_temp)
    return result

# if __name__ == '__main__':
#     param = {
#         "title": "新增可用外呼号码",
#         "interface": "/galaxy-go/call-platform/add",
#         "method": "POST",
#         "Content-Type": "application/x-www-form-urlencoded",
#         "params": {
#             "callPlatform": {
#                 "type": "text",
#                 "iscompulsory": "1"
#             },
#             "phone": {
#                 "type": "text",
#                 "iscompulsory": "1"
#             },
#             "name": {
#                 "type": "text",
#                 "iscompulsory": "1"
#             }
#         }
#     }
#
