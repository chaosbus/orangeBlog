from ._pygments import HighlighterRenderer


def misaka_markdown(value):
    renderer = HighlighterRenderer()
    return renderer.rendering(value)
    # md = m.Markdown(renderer, extensions=('fenced-code',))
    # return md(value)


def init_app(app):
    app.jinja_env.filters['misaka_markdown'] = misaka_markdown

