from lib import action

class KeycloakgetGroupAction(action.KeycloakBaseAction):
    def run(self, group_id):

        group = self.keycloak_admin.get_group(group_id=group_id)
        return group
