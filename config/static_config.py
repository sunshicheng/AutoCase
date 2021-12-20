"""
Author    : Mr. Sun.
FileName  : static_config.py
Time      : 2021/12/13 9:35 AM
Desc      :  一些静态配置
"""


class Static(object):
    # yapi uri和需要的接口
    URI = ""  # 自己家yapi域名
    URL_MAP = {
        "id_detail": "/api/interface/get"
    }
    # yapi project token
    TOKEN_MAP = {
        "saas": "f2f96c70447dfe43108baa33b02fe6e5f1e0c0c440189f9dd305e20fe54dd196",
        "pro_wechat": "fd79fed6d502e8737a5eef50624ff1ff6b737f4d6a9c70047b7d1851f4d6c144"
    }

    # 参数类型映射表
    TYPE_MAP = {
        "text": "string",
        "number": "number",
        "integer": "number",
        "array": "array",
        "object": "object",
        "boolean": "boolean"
    }
