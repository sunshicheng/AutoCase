### 接口case 自动处理工具

#### 参数获取

1. 解析接口文档获取(目前支持的yapi,其他需要自己添加)
2. 也可以自己输入

#### case 生成

1. 使用testcase_automaker 处理基本参数
2. 自己增量添加 参数类型 以及 必填参数缺失部分
3. 最底层使用的开源库 allpairspy

#### ddt运行

1. 只是处理了参数部分，这部分还需要自己进行添加,可以使用pytest或者unittest 进行ddt 驱动测试 ，生成报告

#### 项目目录简介

``` 
├── config                      项目配置文件夹
│├── static_config.py           静态配置文件
│└── url_router.py              测试的路由
├── conftest.py                 pytest 配置文件
├── main.py                     运行文件
├── report                      报告文件夹
│└── report.html                报告
├── requirements.txt            所需要的依赖文件
└── util                        工具文件夹
    ├── generate_demo.py        testcase_automaker 示例
    ├── increment_params.py     增量添加case
    ├── orthogonal_generate.py  最后case 拼装
    ├── tools.py                工具类
    └── yapi_operate.py         yapi文档解析


可以自己在main 文件中进行修改自己的接口进行使用

```

#### pytes 简单执行

1. 直接执行

```
pytest main.py
pytest -v main.py(中文乱码, 将conftest 的注释打开就行)
pytest -v -s main.py
```

2. 生成报告 使用pytest=html

```
pytest main.py --html=./report/report.html --self-contained-html
```