from lib import action


class KeycloakDeleteClientRoleAction(action.KeycloakBaseAction):
    def run(self, role_name):
        self.keycloak_admin.delete_client_role(role_name=role_name)
