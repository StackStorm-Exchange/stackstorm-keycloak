from lib import action

class KeycloakGetGroupsAction(action.KeycloakBaseAction):
    def run(self):

        return self.keycloak_admin.get_groups()
