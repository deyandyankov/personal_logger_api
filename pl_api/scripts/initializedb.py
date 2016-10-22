import os
import sys
import transaction
import datetime

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from ..models import User, Activity, ActivityLog


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        user = User(email='deyan@dyankov.name')
        user_id = dbsession.add(user)
        dbsession.add(Activity(user_id=1, activity_name='work', created_on=datetime.datetime.now()))
        dbsession.add(Activity(user_id=1, activity_name='uni', created_on=datetime.datetime.now()))
        dbsession.add(Activity(user_id=1, activity_name='appdev', created_on=datetime.datetime.now()))
        dbsession.add(Activity(user_id=1, activity_name='dogwalking', created_on=datetime.datetime.now()))
        dbsession.add(Activity(user_id=1, activity_name='khan', created_on=datetime.datetime.now()))
        dbsession.add(Activity(user_id=1, activity_name='shower', created_on=datetime.datetime.now()))
        dbsession.add(Activity(user_id=1, activity_name='study', created_on=datetime.datetime.now()))
