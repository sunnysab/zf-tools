# ZF-Tools 正方教务系统工具

本项目是上海应用技术大学教务系统爬虫工具，适配于今年（2020年12月）上线的新版正方教务系统。由于 Github 上许多类似项目采用 Python2.7
编写，且存在依赖库较多、配套有数据库、安装不上或安装上后难以使用，因此决定造个轮子使用 Python3 重写一遍。 我使用的版本大概是 Python3.8~Python3.9。受限于条件，该代码仅在上海应用技术大学进行测试，敬请谅解。

此项目版本仅为一个最小版本，涵盖教务系统简单的功能。其主要目的是验证功能实现上的可行性、了解项目难度，并为后期使用 rust
语言重写并集成进“ [上应小风筝-数据抓取模块](https://github.com/sunnysab/kite-agent) “打基础。开发完成后可能仅在遇到问题后再更新。

作者希望尽力将该项目做得规范、明了。事实上看到 Github 上众网友、同学的爬虫代码，命名与项目规范比正方好太多。
在学校月初更换教务系统时，内心本有些许惊喜，想着学校终于肯花钱把旧教务系统换掉。可惜事与愿违，换来的是骂声一片的正方，功能还比以前少，只能长叹一声：唉——。

![新版正方教务系统截图](./front-page.png)

## 当前功能

- [x] 查询个人信息
- [x] 查询成绩单
- [x] 查询/计算课程绩点
- [x] 获取班级列表
- [x] 获取专业列表
- [x] 获取专业推荐课表
- [x] 批量导出学生课表/查询空闲学生 ([scripts](scripts/))
- [ ] 查询专业培养计划
- [ ] 选课
- [ ] 评教(短时间内不推出)
- [ ] 教务系统公告

## 使用示例

当前项目正在开发中，接口可能随时发生变化，实际使用方法以代码为准。

```python

from src import session
from src.parsers import Semester, AllSchoolYear, SchoolYear

# 创建一个 session
s = session.Session()
# 使用用户名或密码登录
err_message = s.login('user', 'password')

if err_message == 'success':
    user = s.user()  # 取得用户对象
    # 查询成绩表
    scores = user.get_score_list(SchoolYear(), Semester.ALL)
    for each_course_score in scores:
        print(each_course_score)
    # 查询绩点表
    print(user.get_GPA(AllSchoolYear(), Semester.ALL))
    # 查询分组后的课程表
    # 使用 user.get_timetable 可以查询原始课程表
    time_table = user.get_grouped_timetable(SchoolYear(2020), Semester.SECOND_TERM)
    for course_name in time_table:
        print(course_name)
        for each_class in time_table[course_name]:
            print(each_class)

    env = s.environment()  # 取得环境对象
    # 查询所有可用专业
    majors = env.get_major_list(SchoolYear(2018))
    for each_major in majors:
        print(each_major)
    # 查询全校班级列表(含毕业)
    classes = env.get_class_list(SchoolYear(2018), Semester.SECOND_TERM)
    for each_class in classes:
        print(each_class)
    # 查询某专业推荐课表
    suggested_courses = env.get_suggested_course(SchoolYear(2020), Semester.SECOND_TERM, 'B2203', '20122311')
    print(suggested_courses)

```

## 联系方式

邮箱: sunnysab@yeah.net

## 捐助

如果你觉得本项目对你有帮助，可以适当地赞助我。一两分我都会很开心 :D

![支付宝收款码](alipay_donation.png)

## 版权声明

Copyright (C) 2020 sunnysab

使用 [GPL v3](LICENSE) 协议分享本项目源代码