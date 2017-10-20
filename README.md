# Stackstorm Keycloak Pack

Pack built on python-keycloak module

## Current Status & Capabilities

Runs keycloak admin operations:
  - getters for user, client and role
  - create/delete user
  - create client
  - create role
  - assign client role to user

## Roadmap

Features to add:
  - client create/delete
  - ID Provider operations
  - SMTP config
  - Realm config

## Configuration

Copy the example configuration in [keycloak.yaml.example](./keycloak.yaml.example)
to `/opt/stackstorm/configs/keycloak.yaml` and edit as required.

It must contain:

* ``host`` - Keycloak server IP/name
* ``scheme`` - http/https - default https
* ``port`` - Keycloak server port
* ``user`` - Keycloak user
* ``password`` - Keycloak password
* ``realm`` - Keycloak realm - default master
* ``verify`` - Verify SSL certificate - default True

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`
