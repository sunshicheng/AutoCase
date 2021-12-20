"""
Author    : Mr. Sun.
FileName  : orthogonal_generate.py
Time      : 2021/12/14 9:19 AM
Desc      :  正交用例生成文件
"""
from testcase_automaker.interface.http_params_generator import http_params_generator
from util.increment_params import type_increment_case, compulsory_increment_case
from config.static_config import Static as si
from util.tools import random_num
from util.yapi_operate import get_detail


def auto_testcase(params_structure):
    params_generator = http_params_generator(parameters_structure=params_structure)
    params_temp = params_generator.generate_params_list()
    result = params_generator.generated_params_list
    return result


# 对需要参数化的case 再次进行加工 增加一些接口需要的东西
def params_parametrize(payload):
    """
    :return:
    """
    # 所有的case 进行累加

    case_list = [payload]
    type_add = type_increment_case(payload)
    compulsory_add = compulsory_increment_case(payload)

    case_list = case_list + type_add + compulsory_add
    # 构造返回值
    result = []
    id_s = []
    # 用于去重
    params_temp = []

    # 需要补充的值

    for case in case_list:
        inter = case['interface']
        method = case['method']
        title = case['title']
        params_structure = case['params']
        #  integer 处理
        for key in params_structure.keys():
            if params_structure[key]['type'] == 'integer':
                # 默认填充进去6个
                params_structure[key]['range'] = random_num(6)

        # 进行type 映射处理
        for key in params_structure.keys():
            params_type = params_structure[key]['type']
            params_structure[key]['type'] = si.TYPE_MAP[params_type]

        if len(params_structure) > 0:
            params_list = auto_testcase(params_structure)
            for params in params_list:
                if params not in params_temp:
                    params_temp.append(params)
                    result.append((title, inter, method, params))
                    id_s.append(title)
        else:
            params_temp.append({})
            result.append((title, inter, method, {}))
            id_s.append(title)

    return result, id_s


def create_case(inter_id=None, payload=None):
    """
    :param inter_id:
    :param payload:
    :return:
    """
    if inter_id:
        params_ = get_detail(inter_id)
        result, id_s = params_parametrize(params_)
        return result, id_s
    elif payload:
        params_ = payload
        result, id_s = params_parametrize(params_)
        return result, id_s
    else:
        return [], []


# if __name__ == '__main__':
#     param = {
#         'title': '用户权限查询',
#         'interface': '/galaxy-go/crm/staff/get-permission',
#         'method': 'GET',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'params':
#             {'account':
#                  {'type': 'text',
#                   'range': ['sunshicheng', '297999'],
#                   'iscompulsory': '1'
#                   }
#              }
#     }
#     print(params_parametrize(param)[0])
