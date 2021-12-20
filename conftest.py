"""
Author    : Mr. Sun.
FileName  : conftest.py
Time      : 2021/12/13 9:39 AM
Desc      :  对 pytest 生成的报告一些改造

"""

from py.xml import html
import pytest
from datetime import datetime


# 标题
@pytest.mark.optionalhook
def pytest_html_report_title(report):
    report.title = "自动化测试报告"


# 环境部分修改
def pytest_configure(config):
    # 添加项目名称
    config._metadata["项目名称"] = "基于接口文档正交基准测试"
    # 删除Plugins
    config._metadata.pop("Plugins")
    # 删除执行平台 Platform
    config._metadata.pop("Platform")


# summary 修改
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):  # 添加summary内容
    prefix.extend([html.p("所属部门: 测试组")])
    prefix.extend([html.p("测试人员: 孙事成")])


# 表格相关修改
# 表头
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    cells.pop(-1)  # 删除link


# 表内容
@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop(-1)  # 删除link列


# 具体值
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):  # description取值为用例说明__doc__
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)


# 字体转码修改
def pytest_collection_modifyitems(items) -> None:
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        # 生成报告的时候不需要
        # item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")
