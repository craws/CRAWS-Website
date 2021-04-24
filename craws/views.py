from flask import render_template

from craws import app
from craws.data import projects


@app.route('/')
def index():
    html = ''
    for tag in sorted(projects.tags.items(), key=lambda t: t[0].casefold(), reverse=False):
        html += f'<div id="{projects.sanitize(tag)}">{tag}</div>'
    return render_template(
        'index.html',
        page="index",
        projects=projects,
        tags=f'<div id="tags">{html}</div>')


@app.route('/team')
def team():
    return render_template('team.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
