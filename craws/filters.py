from urllib.parse import urlsplit

from craws import app


@app.template_filter()
def base_url(url: str) -> str:
    return "{0.scheme}://{0.netloc}/".format(urlsplit(url))


@app.template_filter()
def sanitize(string: str) -> str:
    return ''.join(i for i in string if i not in [' ', '(', ')'])
