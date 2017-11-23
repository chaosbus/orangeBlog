# -*- coding: utf-8 -*-

from flask import render_template, request
from flask_login import login_required
from . import bp_about
# from .. import db
from ..models import User, Role
from .. import pages


@bp_about.route('/')
def index():
    a = User.query.filter_by(username='tom').first()

    return render_template('about/dbshow.html', role=a.role.name, username=a.username)


@bp_about.route('/1')
@login_required
def index1():
    return 'Only authenticated user'


@bp_about.route('/2')
def index2():
    a = request.args.get('next')
    b = request.args
    c = request
    e = 0
    return render_template('about/index.html')


@bp_about.route('/3')
def index3():
    return render_template('about/index.html')


AAA = u"""
# 控制中心BOSS接口改造

> 用户鉴权接口，订购同步接口


[TOC]


## 一、流程结构


### 说明

* 控制中心使用内部定义的通用报文（json）格式向nginx发送请求
* ngx_lua模块通过lua脚本将协议转换为各省的报文，同时解析应答，再转为内部的json协议
* nginx为适配层，各类千奇百怪的协议在nginx中通过lua转义为内部json协议

### 用户鉴权、订购同步

```json
{
  "boss_api_type": "sub_sync",  // 接口类型
  "streaming_no": "20171101125959000123", // 流水号 time + {%.6d}序号
  "timestamp": "20171101125959", // *opt 当前时间，报文中会用到时间
  "seq": "123",                // *opt 流水序号
  "user": "13500000001",     // 用户号
  "user_id_type": "1",      // 用户帐号类型
  "user_pay_type": "0",   // 用户付费类型
  "area_code": "028",    // 地区编码

  "sub_type": "订购/退订/替换/...", // 操作类型
  "prod_code": "产品号",
  "alter_prod_code": "替换时，老产品号",
  "sp_code": "SP编码",
  "svc_code": "业务编码",
  "effect_type": "待生效",
  "charge_type": "扣费类型，按天、月、年",
  "sub_time": "订购时间",
  "effect_time": "生效时间",
  "expire_time": "失效时间"
}
```



## 二、订购同步

### 改造进度【TODO】
  - [x] 上海
  - [ ] 辽宁
  - [ ] 湖南
  - [ ] 湖北

"""

from flask_flatpages import pygments_style_defs, pygmented_markdown


@bp_about.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}


@bp_about.route('/md')
def mdtest():
    return render_template('about/markdown.html', md=AAA)


@bp_about.route('/<path:path>')
def pagege(path):
    page = pages.get_or_404(path)
    # template = page.meta.get('templates.public', 'flatpage.html')
    # template = page.meta.get('template', 'flatpage.html')
    # return render_template(template, page=page)
    return render_template('public/flatpage.html', page=page)


# @bp_about.route('/all')
# def index():
#     # Articles are pages with a publication date
#     articles = (p for p in pages if 'published' in p.meta)
#     # Show the 10 most recent articles, most recent first.
#     latest = sorted(articles, reverse=True,
#                     key=lambda p: p.meta['published'])
#     return render_template('articles.html', articles=latest[:10])


