import os
from copy import deepcopy
from rdflib import Namespace
import pytest

BRICK_VERSION = '1.0.3'
BRICK = Namespace(f'https://brickschema.org/schema/{BRICK_VERSION}/Brick#')

HOSTNAME = os.environ['HOSTNAME']
API_BASE = HOSTNAME + '/brickapi/v1'
ENTITY_BASE = API_BASE + '/entities'
QUERY_BASE = API_BASE + '/rawqueries'
DATA_BASE = API_BASE + '/data'
ACTUATION_BASE = API_BASE + '/actuation'
AUTH_BASE = HOSTNAME + '/auth'


default_headers = {
    "Authorization": "Bearer " + os.environ['JWT_TOKEN']
}


def authorize_headers(headers={}):
    headers.update(default_headers)
    return headers
