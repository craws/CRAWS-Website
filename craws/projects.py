# Created by Alexander Watzinger. Please see README.md for licensing information
from collections import OrderedDict


class Project(object):
    def __init__(self, identifier, name, start, end=None):
        self.identifier = identifier
        self.name = name
        self.start = start
        self.end = end

    name = None
    description = None
    start = None
    end = None
    url = None
    url_forum = None
    url_repository = None
    url_tracker = None
    tags = []
    urls = {}


def sanitize(string):
    return ''.join(x for x in string if x.isalnum())


projects = []

openatlas = Project('openatlas', 'OpenAtlas', 2013, 'now')
openatlas.description = 'An open source, web based database system for complex archaeological, historical and geospatial data.'

openatlas.urls = OrderedDict()
openatlas.urls['Website'] = 'https://openatlas.eu'
openatlas.urls['Demo version'] = 'https://demo.openatlas.eu'
openatlas.urls['Code on GitHub'] = 'https://github.com/craws/OpenAtlas'
openatlas.tags = ['Apache', 'Debian', 'Flask', 'Non-Profit', 'Open Source', 'Python', 'PostGIS', 'PostgreSQL']
projects.append(openatlas)

lady_cancer = Project('lady_cancer', 'Lady Cancer', 2014, 2017)
lady_cancer.description = 'Outreach for cancer survivors. Archived as static HTML in 2017.'
lady_cancer.urls = {'Website': 'https://archive.craws.net/ladycancer'}
lady_cancer.tags = ['Apache', 'Debian', 'Non-Profit', 'PHP', 'PostgreSQL']
projects.append(lady_cancer)

bock = Project('bock', 'Ute Bock', 2010)
bock.description = 'Teaching refugees basic computer skills.'
bock.tags = ['Debian', 'Non-Profit']
bock.urls = {'Website': 'https://fraubock.at'}
projects.append(bock)

folding = Project('folding', 'Folding@Home', 2009, 'now')
folding.description = 'Participation at Folding@home, a distributed computing project for disease research'
folding.urls = OrderedDict()
folding.urls['Website'] = 'https://foldingathome.org'
folding.urls['Team stats'] = 'https://stats.foldingathome.org/team/150343'
folding.tags = ['Non-Profit']
projects.append(folding)

xplodinghead = Project('xplodinghead', 'XplodingHead', 2005, 2017)
xplodinghead.description = 'A non-profit platform for projects with like-minded people. Archived as static HTML in 2018.'
xplodinghead.urls = {'Website': 'https://archive.craws.net/xplodinghead'}
xplodinghead.tags = ['Apache', 'Debian', 'Non-Profit', 'PHP', 'PostgreSQL']
projects.append(xplodinghead)

cloneball = Project('cloneball', 'CloneBall', 2005, 2011)
cloneball.description = 'A futuristic, not entirely serious online sports manager game.'
cloneball.urls = {'Website': 'https://archive.craws.net/xplodinghead/cloneball'}
cloneball.tags = ['Apache', 'Debian', 'Java', 'Non-Profit', 'PHP', 'PostgreSQL']
projects.append(cloneball)

lila9 = Project('lila9', 'Lila9', 2001)
lila9.description = 'A website for a small party in the 2001 council elections in Vienna.'
lila9.urls = {'Website': 'https://archive.craws.net/lila9'}
lila9.tags = ['Non-Profit']
projects.append(lila9)

tags = {}

for project in projects:
    project.tags_sanitized = []
    for tag in project.tags:
        sanitized_tag = sanitize(tag)
        project.tags_sanitized.append(sanitized_tag)
        # Counting in thousand steps and adding number for first character for sorting
        if tag in tags.keys():
            tags[tag] += 1
        else:
            tags[tag] = 1
