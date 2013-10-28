logger_config = {
    'labels': ['dy', 'ydot', 'ydotdot', 'force_y', 'pred_force_y'],
    'types':  ['float', 'float', 'float', 'float', 'float'],
    'keys':   {
        'state': ['dy', 'ydot', 'ydotdot'],
        'force': ['y']
    }
}

predictor_config = {
    'serialization': {
        'path': '/tmp/pilot/default/copter',
        'save_freq': 1000
    }
}
