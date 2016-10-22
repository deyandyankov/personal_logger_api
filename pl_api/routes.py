def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('view_activity_start', '/activity/{activity_name}/start')
    config.add_route('view_activity_end', '/activity/end')
    config.add_route('view_activity_current', '/activity/_current')
