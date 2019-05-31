
# Python API Wrappers for NJUPT.   南京邮电大学网站接口 Python 封装

## 注意：由于肯定是“技术升级”的原因, 现在你无法外网使用它。等几天，或者内网调用
[![Build Status](https://travis-ci.com/gaoliang/NJUPT-API.svg?branch=master)](https://travis-ci.com/gaoliang/NJUPT-API)

[【阅读文档】](http://gaoliang.github.io/NJUPT-API)

## 功能特性

[正方教务](#正方教务)

- [获取课程成绩和绩点](#获取课程成绩和绩点)
- [获取等级考试信息](#获取等级考试信息)
- [获取全部课程](#获取全部课程)
- [获取可选课程](#获取可选课程)
- [获取课表](#获取课表)

[校园卡系统](#校园卡系统)

- [获取校园卡余额](#获取校园卡余额)
- [充值校园卡](#充值校园卡)
- [获取账单](#获取账单)
- [获取网费余额](#获取网费余额)
- [充值网费](#充值网费)
- [充值寝室电费](#充值寝室电费)

[图书馆系统](#图书馆系统)

- [获取基本信息](#获取基本信息)

[早锻炼系统](#早锻炼系统)

- [查询早锻炼次数和记录](#早锻炼系统)

## 安装

```bash
pip install njupt
# 仅支持python3
```

## 使用示例

这里是一些简单的使用案例
```python
# 校园卡充值
from njupt import Card
card = Card(account='11020xxxxxxxxxx',password='passwd')
>>> card.recharge_xianlin_elec(amount=2.33,building_name='兰苑11栋',big_room_id='403', small_room_id='1')
{
    'success': True,
    'code' : 0,
    'Msg' : '缴费成功！'
}
```
```python
# 查询课程表
from njupt import SSO
sso = SSO(username='B12345678', password='password') # 通过 my.njupt.edu.cn 单点登录
zf = sso.zhengfang()
>>> zf.get_courses()
[
    {
        'class_end': 9,
        'class_start': 8,
        'day': 1,
        'name': '市场营销',
        'room': '教4－101',
        'teacher': '王波(男)',
        'week': '第1-15周|单周',
        'interval': 2,
        'week_end': 15,
        'week_start': 1
    },
    ...
]
```
更多示例参见 [文档](http://gaoliang.github.io/NJUPT-API)

## 谁在使用？

- [save1s shortcuts](https://shortcuts.save1s.com) : 为生活节省一秒的ios捷径
- [NJUPT-iCal](https://github.com/shaoye/NJUPT-iCal) : 生成课表ics文件并导入系统日历
