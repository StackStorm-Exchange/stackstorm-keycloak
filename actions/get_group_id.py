from lib import action

class KeycloakGetGroupIdAction(action.KeycloakBaseAction):
    def run(self, name=None, path=None, parent=None):

        group_id = self.keycloak_admin.get_group_id(name=name, path=path, parent=parent)
        return group_id
