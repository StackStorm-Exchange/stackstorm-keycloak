from lib import action

class KeycloakGetClientAction(action.KeycloakBaseAction):
    def run(self, clientname):

        client_id = self.keycloak_admin.get_client_id(clientname=clientname)
        return client_id
