from flask import Flask, Response

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.default')  # type: ignore
app.config.from_pyfile('production.py')  # type: ignore

from craws import views, filters


@app.after_request
def apply_caching(response: Response) -> Response:
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response


if __name__ == "__main__":  # pragma: no cover
    app.run()
