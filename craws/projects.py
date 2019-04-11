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
openatlas.description = 'Web-based interface to process historical data for the Austrian Academy of Sciences.'

openatlas.urls = OrderedDict()
openatlas.urls['Demo'] = 'https://demo.openatlas.eu'
openatlas.urls['Wiki'] = 'https://redmine.openatlas.eu/projects/uni/wiki'
openatlas.urls['Project website'] = 'http://openatlas.eu/website'
openatlas.urls['Code on GitHub'] = 'https://github.com/craws/OpenAtlas'
openatlas.tags = ['Apache', 'Debian', 'Flask', 'jQuery', 'Non Profit', 'Open Source', 'Python', 'PostGIS', 'PostgreSQL']
projects.append(openatlas)

lady_cancer = Project('lady_cancer', 'Lady Cancer', 2014, 2017)
lady_cancer.description = 'Outreach for cancer survivors. Archived as static HTML in 2017.'
lady_cancer.urls = {'Website': 'https://ladycancer.craws.net'}
lady_cancer.tags = ['Apache', 'Debian', 'jQuery', 'Non Profit', 'PHP', 'PostgreSQL', 'Zend Framework']
projects.append(lady_cancer)

childer = Project('childer', 'Childer', 2014, 'now')
childer.description = 'Website for a gothic underground band. Converted to static HTML in 2017.'
childer.urls = {'Website': 'https://childer.net'}
childer.tags = ['Apache', 'Debian', 'jQuery', 'Non Profit', 'PHP', 'PostgreSQL', 'Zend Framework']
projects.append(childer)

dickmadam = Project('dickmadam', 'Dickmadam', 2014)
dickmadam.description = 'Website for an eating disorder therapist.'
dickmadam.urls = {'Website': 'http://www.dickmadam.at'}
dickmadam.tags = ['PHP']
projects.append(dickmadam)

wohnkraft = Project('wohnkraft', 'Wohnkraft', 2012, 2017)
wohnkraft.description = 'Website and hosting for a furniture store.'
wohnkraft.urls = {'Website': 'http://wohnkraft.net'}
wohnkraft.tags = ['Apache', 'Debian', 'jQuery', 'PHP', 'PostgreSQL', 'Zend Framework']
projects.append(wohnkraft)

bock = Project('bock', 'Ute Bock', 2010)
bock.description = 'Teaching refugees basic computer skills.'
bock.tags = ['Debian', 'Non Profit']
bock.urls = {'Website': 'http://fraubock.at'}
projects.append(bock)

folding = Project('folding', 'Folding@Home', 2009, 'now')
folding.description = 'Participation in the Folding@home project.'
folding.urls = {'Stats': 'https://stats.foldingathome.org/team/150343'}
folding.tags = ['Non Profit']
projects.append(folding)

xplodinghead = Project('xplodinghead', 'XplodingHead', 2005, 2017)
xplodinghead.description = 'A non-profit platform for projects with like-minded people. Converted to static HTML in 2018.'
xplodinghead.urls = {'Website': 'https://xplodinghead.org'}
xplodinghead.tags = ['Apache', 'Debian', 'Non Profit', 'PHP', 'PostgreSQL']
projects.append(xplodinghead)

cloneball = Project('cloneball', 'CloneBall', 2005, 2011)
cloneball.description = 'A futuristic, not entirely serious online sports manager game.'
cloneball.urls = {'Website': 'https://xplodinghead.org/cloneball'}
cloneball.tags = ['Apache', 'Debian', 'Java', 'jQuery', 'Non Profit', 'PHP', 'PostgreSQL']
projects.append(cloneball)

icmpd = Project('icmpd', 'International Centre for Migration Policy Development', 2005)
icmpd.description = 'Web application for visualization of applications for asylum in Europe.'
icmpd.tags = ['MySQL', 'PHP']
projects.append(icmpd)

agrar = Project('agrar', 'Agrarbündnis Österreich', 2003)
agrar.description = 'A website for an agriculture alliance.'
agrar.tags = ['MySQL', 'Non Profit', 'PHP']
projects.append(agrar)

lila9 = Project('lila9', 'Lila9', 2001)
lila9.description = 'A website for a small party in the 2001 council elections in Vienna.'
lila9.urls = {'Website': 'https://lila9.craws.net'}
lila9.tags = ['Non Profit']
projects.append(lila9)

patent = Project('patent', 'European Patent Office', 2001)
patent.description = "Fulltext search interface for the ESPACE Legal publication."
patent.tags = ['Java']
projects.append(patent)

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
