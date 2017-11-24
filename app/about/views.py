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

### 用户鉴权、订购同步

```c
#include <stdio.h>

int main(int c, char *p)
{
return 0;
{
```

### 8. proxy_redirect

[Ref: proxy_redirect](http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_redirect)

Sets the text that should be changed in the "Location" and "Refresh" header fields of a proxied server response.


```nginx
server {
    listen 22223;

    location /test_limit {

        # 某个IP来源的请求同时只能1个
        limit_conn ConnIP 1;
        # 服务端只接受最大100个连接
        limit_conn ConnServer 100;

        # 限流速
        limit_rate 100k;
        limit_rate_after 10M;

        # 限请求频率
        limit_req zone=ReqIP burst=30 nodelay;
        limit_req zone=ReqServer burst=40;
    }
}
```

## 二、订购同步

### 改造进度【TODO】

  - [x] 上海

  - [ ] 辽宁
"""

from flask_flatpages import pygments_style_defs, pygmented_markdown


@bp_about.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}


@bp_about.route('/md1')
def mdtest():
    return render_template('about/markdown.html', md=AAA)


@bp_about.route('/docs')
def index111():
    pp = (p for p in pages if 'date' in p.meta)
    return render_template('public/index.html', pages=pp)


@bp_about.route('/docss/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('public/tag.html', pages=tagged, tag=tag)


@bp_about.route('/docs/<path:path>')
def pagefrunc(path):
    pp = pages.get_or_404(path)
    return render_template('public/page.html', page=pp)

