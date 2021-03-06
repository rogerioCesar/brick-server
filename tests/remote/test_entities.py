from urllib.parse import quote_plus
import pdb
import requests
from pdb import set_trace as bp

from .common import ENTITY_BASE, authorize_headers, BRICK
from .data import znt_id


def test_load_ttl():
    with open('examples/data/bldg.ttl', 'rb') as fp:
        headers = authorize_headers({
            'Content-Type': 'text/turtle',
        })
        resp = requests.post(ENTITY_BASE + '/upload', headers=headers, data=fp, allow_redirects=False)
        assert resp.status_code == 200

def test_get_an_entity():
    headers = authorize_headers()
    resp = requests.get(ENTITY_BASE + '/' + quote_plus(znt_id), headers=headers)
    assert resp.status_code == 200
    assert resp.json()['type'].split('#')[-1] == 'Zone_Air_Temperature_Sensor'
    # How to reuse the response schema?

def test_delete_an_entity():
    headers = authorize_headers()
    resp = requests.get(ENTITY_BASE + '/' + quote_plus(znt_id), headers=headers)
    assert resp.status_code == 200
    assert resp.json()['type'].split('#')[-1] == 'Zone_Air_Temperature_Sensor'
    resp = requests.delete(ENTITY_BASE + '/' + quote_plus(znt_id), headers=headers)
    assert resp.status_code == 200
    resp = requests.get(ENTITY_BASE + '/' + quote_plus(znt_id), headers=headers)
    assert resp.status_code == 404


def test_reload_ttl():
    headers = authorize_headers({
        'Content-Type': 'text/turtle',
    })
    with open('examples/data/bldg.ttl', 'rb') as fp:
        resp = requests.post(ENTITY_BASE + '/upload',
                             headers=headers,
                             data=fp,
                             allow_redirects=False,
                             )
        assert resp.status_code == 200

def test_create_entities():
    headers = authorize_headers()
    body = {
        str(BRICK.Zone_Temperature_Sensor): 2,
        str(BRICK.Thermal_Power_Sensor): 2,
    }
    resp = requests.post(ENTITY_BASE, json=body, headers=headers)
    assert resp.status_code == 200
    assert len(resp.json()[str(BRICK.Zone_Temperature_Sensor)]) == 2

