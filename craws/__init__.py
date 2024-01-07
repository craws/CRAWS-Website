from flask import Flask, Response

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('production.py')

# pylint: disable=wrong-import-position, import-outside-toplevel
from craws import views, filters


@app.after_request
def apply_caching(response: Response) -> Response:
    response.headers['Strict-Transport-Security'] = \
        'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
