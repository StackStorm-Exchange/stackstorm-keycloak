from lib import action


class KeycloakGetUserAction(action.KeycloakBaseAction):
    def run(self, user_id):

        user = self.keycloak_admin.get_user(user_id=user_id)
        return user
