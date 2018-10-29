from lib import action


class KeycloakCreateUserAction(action.KeycloakBaseAction):
    def run(self, username, email='', firstName='', lastName='', enabled=True,
            emailVerified=False, password=None, passwordTemp=True):
        payload = {}
        payload['username'] = username
        payload['email'] = email
        payload['firstName'] = firstName
        payload['lastName'] = lastName
        payload['emailVerified'] = emailVerified
        payload['enabled'] = enabled
        if password is not None:
            payload['credentials'][0] = {}
            payload['credentials'][0]['value'] = password
            payload['credentials'][0]['type'] = 'password'
            payload['credentials'][0]['temporary'] = passwordTemp

        user_id = self.keycloak_admin.get_user_id(username=username)
        if user_id is None:
            self.keycloak_admin.create_user(payload)
        else:
            return "User " + username + " already exists"
