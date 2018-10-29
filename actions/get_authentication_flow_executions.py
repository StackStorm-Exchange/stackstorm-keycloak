from lib import action


class KeycloakGetAuthenticationFlowExecutionssAction(action.KeycloakBaseAction):
    def run(self, flow_alias):

        client = self.keycloak_admin.get_authentication_flow_executions(flow_alias=flow_alias)
        return client
