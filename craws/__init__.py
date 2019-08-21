# Created by Alexander Watzinger. Please see README.md for licensing information
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.default')  # Load config
app.config.from_pyfile('production.py')  # Load instance

from craws import views


@app.after_request
def apply_caching(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response


if __name__ == "__main__":  # pragma: no cover
    app.run()
