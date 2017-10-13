from lib import action

class KeycloakGetServerInfoAction(action.KeycloakBaseAction):
    def run():

        return self.keycloak_admin.get_server_info()
