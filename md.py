# -*- coding: utf-8 -*-

# import houdini as h
import misaka as m
from pygments import highlight
from pygments.formatters import HtmlFormatter, ClassNotFound
from pygments.lexers import get_lexer_by_name

class HighlighterRenderer(m.HtmlRenderer):
    def blockcode(self, text, lang):
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except ClassNotFound:
            lexer = None

        if lexer:
            formatter = HtmlFormatter()
            return highlight(text, lexer, formatter)
        # default
        return '\n<pre><code>{}</code></pre>\n'

renderer = HighlighterRenderer()
md = m.Markdown(renderer, extensions=('fenced-code',))


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
  "boss_api_type": "sub_sync",
  "streaming_no": "20171101125959000123",
  "timestamp": "20171101125959",
  "seq": "123",
  "user": "13500000001",
  "user_id_type": "1",
  "user_pay_type": "0",
  "area_code": "028",

  "sub_type": "订购/退订/替换/...",
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
print(md(AAA))