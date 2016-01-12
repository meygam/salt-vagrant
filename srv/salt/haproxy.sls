haproxy:
  pkg.installed: []
  service.running:
    - watch:
      - file: /etc/haproxy/haproxy.cfg
    - require:
      - pkg: haproxy

/etc/haproxy/haproxy.cfg:
  file.managed:
    - source: salt://haproxy/config
    - template: jinja

/etc/default/haproxy:
  file.managed:
    - source: salt://haproxy/default
    - template: jinja
