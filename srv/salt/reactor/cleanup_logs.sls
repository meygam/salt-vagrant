#!py

import re


def run():
  postdata = data['post']
  ret = {}
  for message in postdata['messages']:
    if message['type'] == "incident.trigger":
      if "High Volume Usage" in message['data']['incident']['trigger_summary_data']['subject']:
        re_result = re.search("\S+(?=.meygam.com)", message['data']['incident']['trigger_summary_data']['subject'])
        pillar_dict = {}
        pillar_dict['message'] = message
        pillar_dict['target'] = re_result.group()

        ret = {
            'cleanup_logs:': {
                'runner.state.orchestrate': [
                    {'mods': 'orch.meygam.util.cleanup_logs'},
                    {'pillar': pillar_dict}
                ]
            }
        }

  return ret
