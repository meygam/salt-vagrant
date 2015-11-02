saltuser:
  user.present:
    - password: $1$TM7UYz5h$NUBkJ.3oGk.o9vQ40kfcS0

salt-api:
  pkg.installed

salt-api_service:
  service.running:
    - name: salt-api
    - enable: True
