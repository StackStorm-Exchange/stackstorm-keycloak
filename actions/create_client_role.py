from lib import action
import json

class KeycloakUserCreateAction(action.KeycloakBaseAction):
    def run(self, client_id, role_name):
        self.keycloak_admin.create_client_role(client_id=client_id, role_name=role_name)
