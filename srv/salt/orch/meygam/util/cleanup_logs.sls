{% set message = salt['pillar.get']('message') %}
{% set target = salt['pillar.get']('target') %}

delete_logs:
  salt.function:
    - tgt: '{{ target }}'
    - name: meygamutil.delete_logs

resolve_incident:
  salt.runner:
    - name: pagerduty.resolve_incident
    - id: {{ message.data.incident.id }}
    - require:
      - salt: delete_logs
