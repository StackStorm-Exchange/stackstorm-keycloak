from lib import action

class KeycloakGroupCreateAction(action.KeycloakBaseAction):
    def run(self, name, path, client_roles, realm_roles, sub_groups, parent):
        self.keycloak_admin.create_group(name=name, path=path, client_roles=client_roles, realm_roles=realm_roles, sub_groups=sub_groups, parent=parent)
