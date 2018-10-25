from lib import action

class KeycloakUpdateUserAction(action.KeycloakBaseAction):
    def run(self, username, email='', firstName='', lastName='', enabled=True, emailVerified=False, password=None, passwordTemp=True):
        payload = {}
        payload['username']=username
        payload['email']=email
        payload['firstName']=firstName
        payload['lastName']=lastName
        payload['emailVerified']=emailVerified
        payload['enabled']=enabled
        if password is not None:
            payload['credentials'][0]={}
            payload['credentials'][0]['value']=password
            payload['credentials'][0]['type']='password'
            payload['credentials'][0]['temporary']=passwordTemp

        user_id = self.keycloak_admin.get_user_id(username=username)
        if user_id != None:
            self.keycloak_admin.update_user(payload)
        else:
            return "User " + username + " does not exist"
