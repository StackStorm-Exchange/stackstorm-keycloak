from lib import action


class KeycloakUpdateAuthenticationFlowExecutionsAction(action.KeycloakBaseAction):
    def run(self, payload, skip_exists=False):

        self.keycloak_admin.create_authentication_flow(payload=payload, skip_exists=skip_exists)
