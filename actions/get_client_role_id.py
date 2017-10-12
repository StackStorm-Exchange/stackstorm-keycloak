from lib import action

class KeycloakUserCreateAction(action.KeycloakBaseAction):
    def run(client_id, role_name):

        client_role_id = self.keycloak_admin.get_client_role_id(client_id=client_id, role_name=role_name)
        return client_role_id
