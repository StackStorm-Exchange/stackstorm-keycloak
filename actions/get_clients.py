from lib import action

class KeycloakGetClientsAction(action.KeycloakBaseAction):
    def run():

        return self.keycloak_admin.get_clients()
