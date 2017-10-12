from lib import action

class KeycloakUserCreateAction(action.KeycloakBaseAction):
    def run(client_id):

        client = self.keycloak_admin.get_client(client_id=client_id)
        return client
