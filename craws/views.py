from typing import Dict, Tuple

from flask import render_template

from craws import app
from craws.data import projects, team_members
from craws.filters import sanitize


@app.route('/')
def index() -> str:
    tags: Dict[str, int] = {}
    for project in projects.values():
        project['main_url'] = list(project['urls'].values())[0]
        project['tags_sanitized'] = []
        for tag in project['tags']:
            project['tags_sanitized'].append(sanitize(tag))
            if tag in tags.keys():
                tags[tag] += 1
            else:
                tags[tag] = 1
    tags_html = [
        f'<div id="{sanitize(tag)}">{tag}</div>'
        for tag in sorted(tags.keys())]
    return render_template(
        'index.html',
        page="index",
        projects=projects,
        tags=f'<div id="tags">{"".join(tags_html)}</div>')


@app.route('/team')
def team() -> str:
    return render_template('team.html', team_members=team_members)


@app.errorhandler(404)
def page_not_found(e: Exception) -> Tuple[str, int]:
    return render_template('404.html', e=e), 404
