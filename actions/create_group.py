from lib import action


class KeycloakGroupCreateAction(action.KeycloakBaseAction):
    def run(self, name, path, clientRoles={}, realmRoles=[], subGroups={},
            parent=None, skip_exists=True):
        payload = {}
        payload['name'] = name
        payload['path'] = path
        payload['clientRoles'] = clientRoles
        payload['realmRoles'] = realmRoles
        payload['subGroups'] = subGroups

        self.keycloak_admin.create_group(payload=payload, parent=parent, skip_exists=skip_exists)
