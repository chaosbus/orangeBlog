# -*- coding:utf-8 -*-
import misaka as m
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.formatters import ClassNotFound
from pygments.lexers import get_lexer_by_name


# class HighlighterRendererBak(m.HtmlRenderer):
#     def blockcode(self, text, lang):
#         if not lang:
#             return '\n<pre><code>{}</code></pre>\n'.format(text.strip())
#         lexer = get_lexer_by_name(lang, stripall=True)
#         formatter = HtmlFormatter(linenos='inline')
#
#         return highlight(code=text, lexer=lexer, formatter=formatter)
#
#     def table(self, content):
#         return u'\n<table class="table table-bordered table-hover">{}</table>\n'.format(content.strip())


class HighlighterRenderer(m.HtmlRenderer):
    def blockcode(self, text, lang):
        if not lang:
            return '\n<pre><code>{}</code></pre>\n'.format(text.strip())

        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except ClassNotFound:
            lexer = None

        if lexer:
            formatter = HtmlFormatter(linenos='inline')
            return highlight(text, lexer, formatter)
        # default
        return '\n<pre><code>{}</code></pre>\n'.format(text.strip())

    def rendering(self, content):
        renderer = HighlighterRenderer()
        md = m.Markdown(renderer, extensions=('fenced-code',))
        return md(content)

# renderer = HighlighterRenderer()
# md = m.Markdown(renderer, extensions=('fenced-code',))
#
# print(md(AAA))

