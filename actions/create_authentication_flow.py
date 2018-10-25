from lib import action

class KeycloakCreateAuthenticationFlowAction(action.KeycloakBaseAction):
    def run(self, payload, skip_exists=True):

        self.keycloak_admin.create_authentication_flow(payload=payload, skip_exists=skip_exists)
