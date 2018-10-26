from lib import action


class KeycloakClientCreateAction(action.KeycloakBaseAction):
    def run(self, client_id, name, skip_exists=True):
        payload = {}
        payload['id'] = client_id
        payload['name'] = name

        self.keycloak_admin.create_client_role(payload, skip_exists=skip_exists)
