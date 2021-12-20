"""
Author    : Mr. Sun.
FileName  : generate_demo.py
Time      : 2021/12/13 10:12 AM
Desc      : 
"""

from allpairspy import AllPairs
from collections import OrderedDict

# INT = [1, 2, 3]
# STR = []
# parameters = [
#     ["", 1, "1", "2"],
#     ["98", "NT", "2000", "XP"],
#     ["Internal", "Modem", "1111", "2222"],
#     ["Salaried", "Hourly", "Part-Time", "Contr."],
#     [1, 2, "", "111"],
#     [1, 2, 4, 5, 6]
# ]
#
# print("PAIRWISE:")
# for i, pairs in enumerate(AllPairs(parameters)):
#     print("{:2d}: {}".format(i, pairs))

# parameters = OrderedDict({
#     "brand": ["Brand X", "Brand Y"],
#     "os": ["98", "NT", "2000", "XP"],
#     "minute": [15, 30, 60],
# })
#
# print("PAIRWISE:")
# for i, pairs in enumerate(AllPairs(parameters)):
#     print("{:2d} : {}".format(i, pairs))

from testcase_automaker.interface.http_params_generator import http_params_generator

params_structure = {
    'name': {
        'type': 'string',
        'range': ['张三', '李四'],
        'iscompulsory': True
    },
    'phone': {
        'type': 'number',
        'range': [1, 2, 3, 4, 5],
        'iscompulsory': True
    },
    'claimant': {
        'type': 'object',
        'value': {
            'name': {
                'type': 'string',
                'value': '',
                'iscompulsory': True
            },
            'phone': {
                'type': 'number',
                'value': '',
                'iscompulsory': True
            }
        },
        'iscompulsory': True
    },
    'informations': {
        'type': 'array',
        'value': [{
            'claimant': {
                'type': 'object',
                'value': {
                    'name': {
                        'type': 'string',
                        'value': '',
                        'iscompulsory': True
                    },
                    'phone': {
                        'type': 'number',
                        'value': '',
                        'iscompulsory': True
                    }
                },
                'iscompulsory': True
            }
        },
            {
                'name': {
                    'type': 'string',

                    'iscompulsory': True
                }
            }
        ],
        'iscompulsory': True
    }
}

if __name__ == '__main__':
    params_generator = http_params_generator(parameters_structure=params_structure)
    params_list = params_generator.generate_params_list()
    print(params_generator.generated_params_list)
"""
[{'name': '张三', 'phone': 18747931208, 'claimant': {'name': '乐糠晤', 'phone': 14770268531}, 'informations': [{'claimant': {'name': '滑倩', 'phone': 18748251603}}, {'name': '湛岩鍪'}]}, 
{'name': '张三', 'phone': None, 'claimant': {'name': None, 'phone': None}, 'informations': [{'claimant': {'name': None, 'phone': None}}, {'name': '胥闽嗦'}]}, 
{'name': '李四', 'phone': 18842750981, 'claimant': {'name': None, 'phone': 18893415682}, 'informations': [{'claimant': {'name': None, 'phone': 15551940367}}, {'name': None}]}, 
{'name': '张三', 'phone': None, 'claimant': {'name': '程俦', 'phone': None}, 'informations': [{'claimant': {'name': '吉持胚', 'phone': None}}, {'name': None}]}, 
{'name': '李四', 'phone': None, 'claimant': {'name': None, 'phone': 15194786125}, 'informations': [{'claimant': {'name': '宗蜡', 'phone': None}}, {'name': None}]}, 
{'name': '李四', 'phone': 13140237519, 'claimant': {'name': '後漶', 'phone': None}, 'informations': [{'claimant': {'name': '苗鳐', 'phone': None}}, {'name': None}]}, 
{'name': '张三', 'phone': None, 'claimant': {'name': '骆咆', 'phone': None}, 'informations': [{'claimant': {'name': None, 'phone': 13907654932}}, {'name': None}]}]


[{'name': '李四', 'phone': 14708913627, 'claimant': {'name': '郏竣衮', 'phone': 15247513802}, 'informations': [{'claimant': {'name': '任翦', 'phone': 15813295860}}, {'name': '桓龄塾'}]}, 
{'name': '李四', 'phone': None, 'claimant': {'name': None, 'phone': None}, 'informations': [{'claimant': {'name': None, 'phone': None}}, {'name': '郑桉'}]}, {'name': '张三', 'phone': 15228431769, 'claimant': {'name': None, 'phone': 13913290867}, 'informations': [{'claimant': {'name': None, 'phone': 18090643185}}, {'name': None}]}, {'name': '张三', 'phone': None, 'claimant': {'name': '空绚', 'phone': None}, 'informations': [{'claimant': {'name': '厉众', 'phone': None}}, {'name': None}]}, {'name': '李四', 'phone': None, 'claimant': {'name': None, 'phone': 13542978631}, 'informations': [{'claimant': {'name': '寇土', 'phone': None}}, {'name': None}]}, {'name': '张三', 'phone': 15386970235, 'claimant': {'name': '宋忙忌', 'phone': None}, 'informations': [{'claimant': {'name': '居糜醢', 'phone': None}}, {'name': None}]}, {'name': '李四', 'phone': None, 'claimant': {'name': '平饴陂', 'phone': None}, 'informations': [{'claimant': {'name': None, 'phone': 15031658729}}, {'name': None}]}]


[{'name': '张三', 'phone': 15696543170, 'claimant': {'name': '殷随惴', 'phone': 18582631709}, 'informations': [{'claimant': {'name': '黄楗', 'phone': 18893617842}}, {'name': '燕吐蘸'}]}, {'name': '张三', 'phone': None, 'claimant': {'name': None, 'phone': None}, 'informations': [{'claimant': {'name': None, 'phone': None}}, {'name': '寿钩挞'}]}, {'name': '李四', 'phone': 13716354278, 'claimant': {'name': None, 'phone': 18801947523}, 'informations': [{'claimant': {'name': None, 'phone': 13219684752}}, {'name': None}]}, {'name': '张三', 'phone': None, 'claimant': {'name': '法亏翊', 'phone': None}, 'informations': [{'claimant': {'name': '窦觎', 'phone': None}}, {'name': None}]}, {'name': '张三', 'phone': None, 'claimant': {'name': None, 'phone': 13918570296}, 'informations': [{'claimant': {'name': '楚弃馁', 'phone': None}}, {'name': None}]}, {'name': '李四', 'phone': 13670296541, 'claimant': {'name': '帅创', 'phone': None}, 'informations': [{'claimant': {'name': '松呶骤', 'phone': None}}, {'name': None}]}, {'name': '张三', 'phone': None, 'claimant': {'name': '万猗', 'phone': None}, 'informations': [{'claimant': {'name': None, 'phone': 15956192348}}, {'name': None}]}]


"""
