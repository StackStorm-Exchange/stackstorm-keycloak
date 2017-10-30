from lib import action

class KeycloakGroupRemoveUserAction(action.KeycloakBaseAction):
    def run(self, user_id, group_id):
        self.keycloak_admin.group_user_remove(user_id=user_id, group_id=group_id)
