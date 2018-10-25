from lib import action


class KeycloakDeleteClientAction(action.KeycloakBaseAction):
    def run(self, group_id):

        self.keycloak_admin.delete_group(group_id=group_id)
