from lib import action

class KeycloakGetGroupIdAction(action.KeycloakBaseAction):
    def run(self, name):

        group_id = self.keycloak_admin.get_group_id(name=name)
        return group_id
