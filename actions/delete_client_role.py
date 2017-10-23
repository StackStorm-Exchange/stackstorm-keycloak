from lib import action

class KeycloakDeleteClientRoleAction(action.KeycloakBaseAction):
    def run(self, client_id, role_name):
        self.keycloak_admin.delete_client_role(client_id=client_id, role_name=role_name)
