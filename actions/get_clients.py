from lib import action

class KeycloakUserCreateAction(action.KeycloakBaseAction):
    def run():

        return self.keycloak_admin.get_clients()
