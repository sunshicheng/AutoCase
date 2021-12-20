"""
Author    : Mr. Sun.
FileName  : tools.py
Time      : 2021/12/14 6:11 PM
Desc      : 
"""
import random
import json
import hashlib
import urllib.parse
import requests
from config.url_router import UrlRouter as ur


def random_num(length):
    random_nums_list = []
    for i in range(1, length + 1):
        random_nums_list.append(random.randint(1, 127))
    return random_nums_list
