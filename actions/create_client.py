from lib import action

class KeycloakClientCreateAction(action.KeycloakBaseAction):
    def run(self, name, client_id, redirect_uris, protocol, public_client, direct_access_grants):
        self.keycloak_admin.create_client(name=name, client_id=client_id, redirect_uris=redirect_uris, protocol=protocol, public_client=public_client, direct_access_grants=direct_access_grants)
