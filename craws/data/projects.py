
projects = {
    'OpenAtlas': {
        'start': 2013,
        'end': 'now',
        'image': 'openatlas.png',
        'tags': ['Apache', 'Debian', 'Flask', 'Non-Profit', 'Open Source', 'Python', 'PostGIS',
                 'PostgreSQL'],
        'urls': {
            'Website': 'https://openatlas.eu',
            'Demo version': 'https://demo.openatlas.eu',
            'Code on GitHub': 'https://github.com/craws/OpenAtlas'},
        'description': "An open source, web based database system for complex archaeological, "
                       "historical and geospatial data."},
    'Lady Cancer': {
        'start': 2014,
        'end': 2017,
        'image': 'lady_cancer.png',
        'tags': ['Apache', 'Debian', 'Non-Profit', 'PHP', 'PostgreSQL'],
        'urls': {'Website': 'https://archive.craws.net/ladycancer'},
        'description': 'Outreach for cancer survivors. Archived as static HTML in 2017.'},
    'Ute Bock': {
        'start': 2010,
        'end': '',
        'image': 'ute_bock.gif',
        'tags': ['Debian', 'Non-Profit'],
        'urls': {'Website': 'https://fraubock.at'},
        'description': "Teaching refugees basic computer skills."},
    'Folding@Home': {
        'start': 2009,
        'end': 'now',
        'image': 'folding.png',
        'tags': ['Non-Profit'],
        'urls': {
            'Website': 'https://foldingathome.org',
            'Team stats': 'https://stats.foldingathome.org/team/150343'},
        'description': "Participation at Folding@home, a distributed computing project for disease "
                       "research"},
    'XplodingHead': {
        'start': 2005,
        'end': 2017,
        'image': 'xplodinghead.png',
        'tags': ['Apache', 'Debian', 'Non-Profit', 'PHP', 'PostgreSQL'],
        'urls': {'Website': 'https://archive.craws.net/xplodinghead'},
        'description': "A non-profit platform for projects with like-minded people. Archived as "
                       "static HTML in 2018."},
    'CloneBall': {
        'start': 2005,
        'end': 2011,
        'image': 'cloneball.png',
        'tags': ['Apache', 'Debian', 'Java', 'Non-Profit', 'PHP', 'PostgreSQL'],
        'urls': {'Website': 'https://archive.craws.net/xplodinghead'},
        'description': "A futuristic, not entirely serious online sports manager game."},

    'Lila9': {
        'start': '2001',
        'end': '',
        'image': 'lila9.png',
        'tags': ['Non-Profit'],
        'urls': {'Website': 'https://archive.craws.net/lila9'},
        'description': "A website for a small party in the 2001 council elections in Vienna."}}


def sanitize(string):
    return ''.join(x for x in string if x.isalnum())


tags = {}
for name, project in projects.items():
    project.tags_sanitized = []
    for tag in project['tags']:
        sanitized_tag = sanitize(tag)
        project.tags_sanitized.append(sanitized_tag)
        # Counting in thousand steps and adding number for first character for sorting
        if tag in tags.keys():
            tags[tag] += 1
        else:
            tags[tag] = 1
