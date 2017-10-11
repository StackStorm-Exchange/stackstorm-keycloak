from lib import action

class KeycloakUserCreateAction(action.KeycloakBaseAction):
    def run(username):

        user_id = self.keycloak_admin.get_user_id(username=username)
        return user_id
