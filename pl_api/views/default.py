from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
import datetime
from ..models.plmodels import *


### helper functions
def get_activity(request, user_id, activity_name):
    return request.dbsession.query(Activity).filter_by(user_id=user_id, activity_name=activity_name).first()

def start_activity(request, activity):
    activity_log = ActivityLog(activity_id=activity.id, user_id=activity.user_id, start_time=datetime.datetime.now())
    request.dbsession.add(activity_log)
    return activity_log

def get_current_activity_log(request, user_id):
    current_activities = request.dbsession.query(ActivityLog).filter_by(user_id=user_id, end_time=None).all()
    if len(current_activities) > 1:
        raise Exception("More than one current activity!")
    if len(current_activities) == 0:
        return None
    return current_activities[0]

def end_current_activity(request):
    current_activity_log = get_current_activity(request, 1)
    if current_activity_log is None:
        return 0
    current_activity_log.end_time = datetime.datetime.now()
    request.dbsession.add(current_activity_log)
    return True


### views
@view_config(route_name='view_activity_start', renderer='json')
def view_activity_start(request):
    end_current_activity(request)
    activity_name = request.matchdict['activity_name']
    activity = get_activity(request, 1, activity_name)
    activity_log = start_activity(request, activity)
    return {'success': True} 

@view_config(route_name='view_activity_end', renderer='json')
def view_activity_end(request):
    end_current_activity(request)
    return True

@view_config(route_name='view_activity_current', renderer='json')
def view_activity_current(request):
    current_activity_log = get_current_activity_log(request, 1)
    current_activity = request.dbsession.query(Activity).filter_by(id=current_activity_log.activity_id).first()
    return {'activity_name': current_activity.activity_name, 'start_time': current_activity_log.start_time.strftime("%Y-%m-%d %H:%M:%S")}
