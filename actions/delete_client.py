from lib import action

class KeycloakDeleteClientAction(action.KeycloakBaseAction):
    def run(self, client_id):

        client = self.keycloak_admin.delete_client(client_id=client_id)
