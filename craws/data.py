from typing import Any, Dict, List

team_members: List[Dict[str, str]] = [
    {
        'name': 'Alexander Watzinger',
        'function': 'Software Development',
        'image': 'alex.png',
        'email': 'alexander.watzinger@craws.net'},
    {
        'name': 'Jan Belik',
        'function': 'Graphic Design',
        'image': 'jan.png',
        'email': 'buero@janbelik.com'},
    {
        'name': 'Daniel Kittel',
        'function': 'Quality Assurance',
        'image': 'daniel.png',
        'email': 'daniel.kittel@craws.net'}]

projects: Dict[str, Dict[str, Any]] = {
    'OpenAtlas': {
        'date': '2013 - now',
        'image': 'openatlas.png',
        'tags': [
            'Debian', 'Flask', 'Non-Profit', 'Open Source', 'Python',
            'PostGIS', 'PostgreSQL'],
        'urls': {
            'Website': 'https://openatlas.eu',
            'Demo': 'https://demo.openatlas.eu',
            'Code': 'https://github.com/craws/OpenAtlas'},
        'description':
            'An open source, web based software for complex '
            'archaeological, historical and prosopographical data.'},
    'Folding@Home': {
        'date': '2009 - now',
        'image': 'folding.png',
        'tags': ['Non-Profit'],
        'urls': {
            'Website': 'https://foldingathome.org',
            'Team stats': 'https://stats.foldingathome.org/team/150343'},
        'description':
            "Participation at Folding@home, a distributed computing project for"
            " disease research."},
    'Lady Cancer': {
        'date': '2014 - 2017',
        'image': 'lady_cancer.png',
        'tags': ['Debian', 'Non-Profit', 'PHP', 'PostgreSQL'],
        'urls': {'Website': 'https://archive.craws.net/ladycancer'},
        'description':
            'Outreach for cancer survivors. Archived as static HTML  in 2017.'},
    'Ute Bock': {
        'date': '2010',
        'image': 'ute_bock.gif',
        'tags': ['Debian', 'Non-Profit'],
        'urls': {'Website': 'https://fraubock.at'},
        'description': "Teaching refugees basic computer skills."},
    'XplodingHead': {
        'date': '2005 - 2017',
        'image': 'xplodinghead.png',
        'tags': ['Debian', 'Non-Profit', 'PHP', 'PostgreSQL'],
        'urls': {'Website': 'https://archive.craws.net/xplodinghead'},
        'description':
            'A non-profit platform for projects with like-minded people. '
            'Archived as static HTML in 2018.'},
    'CloneBall': {
        'date': '2005 - 2011',
        'image': 'cloneball.png',
        'tags': ['Debian', 'Java', 'Non-Profit', 'PHP', 'PostgreSQL'],
        'urls': {
            'Website': 'https://archive.craws.net/xplodinghead/cloneball/'},
        'description':
            'A futuristic, not entirely serious online sports manager game.'},
    'Lila9': {
        'date': '2001',
        'image': 'lila9.png',
        'tags': ['Non-Profit'],
        'urls': {'Website': 'https://archive.craws.net/lila9'},
        'description':
            'A website for a small party in the 2001 council '
            'elections in Vienna.'}}
