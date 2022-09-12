import os
import logging
from ast import literal_eval


BASEDIR = os.getcwd()
WORKDIR = os.path.abspath(os.path.dirname(__file__))


DEBUG = True
LOG_LEVEL = 'DEBUG'  # CRITICAL / ERROR / WARNING / INFO / DEBUG


SQLALCHEMY_DATABASE_URI = os.environ["PASSPORT_DATABASE"]

PROPAGATE_EXCEPTIONS = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG_TB_INTERCEPT_REDIRECTS=False
DEBUG_TB_PROFILER_ENABLED=False

SERVER_PORT = os.environ['SERVER_PORT']


