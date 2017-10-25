from lib import action

class KeycloakGroupCreateAction(action.KeycloakBaseAction):
    def run(self, name, client_roles, realm_roles, sub_groups):
        self.keycloak_admin.create_group(name=name, client_roles=client_roles, realm_roles=realm_roles, sub_groups=sub_groups)
