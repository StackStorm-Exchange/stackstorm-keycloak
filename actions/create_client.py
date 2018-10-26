from lib import action


class KeycloakClientCreateAction(action.KeycloakBaseAction):
    def run(self, name, clientId, redirectUris, protocol, publicClient,
            directAccessGrantsEnabled, skip_exists=True):
        payload = {}
        payload['name'] = name
        payload['clientId'] = clientId
        payload['redirectUris'] = redirectUris
        payload['protocol'] = protocol
        payload['publicClient'] = publicClient
        payload['directAccessGrantsEnabled'] = directAccessGrantsEnabled

        self.keycloak_admin.create_client(payload, skip_exists=skip_exists)
