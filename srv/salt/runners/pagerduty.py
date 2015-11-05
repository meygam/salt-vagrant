import requests
import salt.client
import sys
import logging


log = logging.getLogger(__name__)

def acknowledge_incident(id):
    ret = {}
    local = salt.client.Caller()
    pagerduty_token = local.function('pillar.get', 'meygam:pagerduty:token')
    payload = {'requester_id' : 'PDSP96Z'}
    headers = {'Authorization' : 'Token token=' + pagerduty_token}
    try:
        r = requests.put("https://meygam.pagerduty.com/api/v1/incidents/" + id + "/acknowledge", headers=headers, data=payload)
        ret = r.text
    except:
        log.error('Failed to acknowledge pagerduty incident : {}'.format(sys.exc_info()[0]))
        ret = 'Failed to acknowledge pagerduty incident'
    return ret

def resolve_incident(id):
    ret = {'name': 'Pagerduty', 'changes': {}, 'result': False, 'comment': ''}
    local = salt.client.Caller()
    pagerduty_token = local.function('pillar.get', 'meygam:pagerduty:token')
    payload = {'requester_id' : 'PDSP96Z'}
    headers = {'Authorization' : 'Token token=' + pagerduty_token}
    try:
        r = requests.put("https://meygam.pagerduty.com/api/v1/incidents/" + id + "/resolve", headers=headers, data=payload)
        ret = r.text
    except:
        log.error('Failed to resolve pagerduty incident : {}'.format(sys.exc_info()[0]))
        ret = 'Failed to resolve pagerduty incident'
    return ret
