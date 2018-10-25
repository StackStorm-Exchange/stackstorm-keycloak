from lib import action

class KeycloakGetGroupIdAction(action.KeycloakBaseAction):
    def run(self, path=None, search_in_subgroups=True):

        group = self.keycloak_admin.get_group_by_path(path=path,search_in_subgroups=search_in_subgroups)
        return group
