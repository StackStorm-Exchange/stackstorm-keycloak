from lib import action

class KeycloakCreateUserAction(action.KeycloakBaseAction):
    def run(self, username, email='', firstName='', lastName='', enabled=True, emailVerified=False, password=None, passwordTemp=True):
        user_id = self.keycloak_admin.get_user_id(username=username)
        if user_id == None:
            self.keycloak_admin.create_user(username=username, email=email, firstName=firstName, lastName=lastName, emailVerified=emailVerified, enabled=enabled, password=password, passwordTemp=passwordTemp)
        else:
            return "User " + username + " already exists"
