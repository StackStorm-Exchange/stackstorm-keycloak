from lib import action


class KeycloakGetAuthenticationFlowsAction(action.KeycloakBaseAction):
    def run(self):

        return self.keycloak_admin.get_authentication_flows()
