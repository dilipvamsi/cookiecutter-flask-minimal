import os
from flask import Flask

APP = Flask(__name__)
APP.config.from_object('{{cookiecutter.package_name}}_flask.default_settings')
APP.config.from_envvar('{{cookiecutter.package_name.upper()}}_SETTINGS')

__FORMAT = '[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)d] %(message)s'

if not APP.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler
    # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
    file_handler = TimedRotatingFileHandler(
        os.path.join(APP.config['LOG_DIR'],
        '{{cookiecutter.package_name}}.log'), 'midnight'
    )
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(__FORMAT))
    APP.logger.addHandler(file_handler)
