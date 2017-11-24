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


# class HighlighterRenderer(m.HtmlRenderer):
#     def blockcode(self, text, lang):
#         if not lang:
#             return '\n<pre><code>{}</code></pre>\n'.format(text.strip())
#
#         try:
#             lexer = get_lexer_by_name(lang, stripall=True)
#         except ClassNotFound:
#             lexer = None
#
#         if lexer:
#             formatter = HtmlFormatter(linenos='inline')
#             return highlight(text, lexer, formatter)
#         # default
#         return '\n<pre><code>{}</code></pre>\n'.format(text.strip())
#
#     def rendering(self, content):
#         renderer = HighlighterRenderer()
#         md = m.Markdown(renderer, extensions=('fenced-code',))
#         return md(content)

AAA = u"""

# nginx完整心得笔记（内测不删档，送宝刀屠龙）

> 集天地之精华

> 呕心吐血未完成

> FIXME

[TOC]


## 一、功能点说明

### 1. 配置

#### 1.1 location

`location [=|~|~*|^~] /uri/ { … }`

|         模式         |                                     含义                                    |
|----------------------|-----------------------------------------------------------------------------|
| location = /uri      | = 表示精确匹配，只有完全匹配上才能生效                                      |
| location ^~ /uri     | ^~ 开头对URL路径进行前缀匹配，并且在正则之前。                              |
| location ~ pattern   | 开头表示***区分大小写***的【***正则***】匹配                                |
| location ~\* pattern | 开头表示***不区分大小写***的【***正则***】匹配                              |
| location /uri        | 不带任何修饰符，也表示前缀匹配，但是在正则匹配之后                          |
| location /           | 通用匹配，任何未匹配到其它location的请求都会匹配到，相当于switch中的default |

前缀匹配时，Nginx不对url做编码，因此请求为`/static/20%/aa`，可以被规则`^~ /static/ /aa`匹配到（注意是空格）

多个`location`配置的情况下匹配顺序为:

- 首先精确匹配 `=`
- 其次前缀匹配 `^~`
- 其次是按文件中顺序的正则匹配
- 然后匹配不带任何修饰的前缀匹配。
- 最后是交给 `/` 通用匹配
- 当有匹配成功时候，停止匹配，按当前匹配规则处理请求

**注意**：前缀匹配，如果有包含关系时，按最大匹配原则进行匹配。\
比如在前缀匹配：`location /dir01`与`location /dir01/dir02`，\
如有请求`http://localhost/dir01/dir02/file`将最终匹配到`location /dir01/dir02`

#### 1.2 你哪个单位的

- [ ] todo

- [x] done

- 空间单位

  k/K : KiloByte\
  m/M : MegaBye

- 时间单位

  ms : 毫秒\
  s  : 秒\
  m  : 分\
  h  : 时\
  d  : 天\
  M  : 月\
  y  ：年

### 2. nginx变量

[link:nginx变量](http://nginx.org/en/docs/varindex.html)

> 变态搞这么多，我也不造

```
$ancient_browser
$upstream_status
$uri
```


```c
int a = 0;
```
"""


def misaka_markdown(value):
    renderer = HighlighterRenderer()
    return renderer.rendering(value)

print(md(AAA))



