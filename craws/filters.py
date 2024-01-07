from urllib.parse import urlsplit

from craws import app


@app.template_filter()
def base_url(url: str) -> str:
    return f'{urlsplit(url).scheme}://{urlsplit(url).netloc}'


@app.template_filter()
def sanitize(string: str) -> str:
    return ''.join(i for i in string if i not in [' ', '(', ')'])
