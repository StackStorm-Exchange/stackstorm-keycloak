from lib import action
import json

class KeycloakUserCreateAction(action.KeycloakBaseAction):
    def run(self, user_id, client_id, role_id, role_name):
        self.keycloak_admin.assign_client_role(user_id=user_id, client_id=client_id, role_id=role_id, role_name=role_name)
