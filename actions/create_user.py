from lib import action
import json

class KeycloakUserCreateAction(action.KeycloakBaseAction):
    def run(self, username, email, realm, firstName, lastName, enabled, emailVerified):
        user_id = self.keycloak_admin.get_user_id(username=username)
        if user_id = None:
            data={}
            data["username"]=username
            data["email"]=email
            data["firstName"]=firstName
            data["lastName"]=lastName
            data["emailVerified"]=emailVerified
            data["enabled"]=enabled
            self.keycloak_admin.create_user(data)
        else:
