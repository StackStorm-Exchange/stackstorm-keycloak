from lib import action

class KeycloakUpdateAuthenticationFlowExecutionsAction(action.KeycloakBaseAction):
    def run(self, flow_alias, payload, skip_exists=False):

        self.keycloak_admin.create_authentication_flow(flow_alias=flow_alias, payload=payload, skip_exists=skip_exists)
