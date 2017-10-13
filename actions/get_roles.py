from lib import action

class KeycloakgetRolesAction(action.KeycloakBaseAction):
    def run():

        return self.keycloak_admin.get_roles()
