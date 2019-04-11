import os.path
from collections import OrderedDict
from urllib.parse import urlsplit

from flask import render_template

from craws import app, projects


@app.route('/')
def index():
    content = '<div id="tags">'
    tags = OrderedDict(sorted(projects.tags.items(), key=lambda t: t[0].casefold(), reverse=False))
    for tag in tags:
        content += '<div id="' + projects.sanitize(tag) + '">' + tag + '</div>'
    content += '</div>'
    content += '<div id="projects">'
    for project in projects.projects:
        content += '<div class="clear-both">'
        content += '<div class="project ' + ' '.join(project.tags_sanitized) + '">'
        content += '<div class="screenshot">'
        file_path = '/static/images/projects/' + project.identifier + '.png'
        if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + file_path):
            content += '<a href="' + file_path + '"><img src="' + file_path + '" alt="" /></a>'
        content += '</div>'
        content += '<div class="project-info">'
        content += '<span class="project-name">' + project.name + '</span>'
        content += ' <span class="project-dates">\n'
        content += str(project.start)
        if project.end:
            content += ' - ' + str(project.end)
        content += '</span>'
        content += '<p class="project-detail">' + project.description + '</p>'
        for tag in project.tags:
            content += '<div class="tag ' + projects.sanitize(tag) + '" onclick="tagClick(\'' + \
                       projects.sanitize(tag) + '\')">' + tag
            content += '</div>'
        content += '<div class="clear-both"></div>'
        for url in project.urls:
            base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(project.urls[url]))
            content += url + ': '
            content += '<a target="_blank" rel="noopener" href="' + project.urls[url] + '">'
            content += base_url + '</a><br/>'
        content += '</div></div></div>'
    content += '</div>'
    return render_template('index.html', page="index", content=content)


@app.route('/team')
def team():
    return render_template('team.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(403)
def page_forbidden(e):
    return render_template('403.html'), 403
