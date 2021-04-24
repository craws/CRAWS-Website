from typing import Dict

from flask import render_template

from craws import app
from craws.data.projects import projects
from craws.filters import sanitize


@app.route('/')
def index() -> str:
    tags: Dict[str, int] = {}
    for name, project in projects.items():
        project['main_url'] = list(project['urls'].values())[0]
        project['tags_sanitized'] = []
        for tag in project['tags']:
            project['tags_sanitized'].append(sanitize(tag))
            if tag in tags.keys():
                tags[tag] += 1
            else:
                tags[tag] = 1
    tags_html = [f'<div id="{sanitize(tag)}">{tag}</div>' for tag in sorted(tags.keys())]
    return render_template(
        'index.html',
        page="index",
        projects=projects,
        tags=f'<div id="tags">{"".join(tags_html)}</div>')


@app.route('/team')
def team() -> str:
    return render_template('team.html')


@app.errorhandler(404)
def page_not_found(e: Exception) -> tuple:
    return render_template('404.html', e=e), 404
