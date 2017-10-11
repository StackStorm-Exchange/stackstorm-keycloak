from lib import action

class KeycloakUserCreateAction(action.KeycloakBaseAction):
    def run(self, username, email, realm, firstName, lastName, enabled, emailVerified, groups, realmRoles, clientRoles):

        self.keycloak_admin.update_user(username=username, email=email, firstName=firstName, lastName=lastName, enabled=enabled, emailVerified=emailVerified, groups=groups, realmRoles=realmRoles, clientRoles=clientRoles)
