from lib import action


class KeycloakGetClientAction(action.KeycloakBaseAction):
    def run(self, client_name):

        client_id = self.keycloak_admin.get_client_id(client_name=client_name)
        return client_id
