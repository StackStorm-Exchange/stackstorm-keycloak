from lib import action


class KeycloakGroupPermsAction(action.KeycloakBaseAction):
    def run(self, group_id, enabled=True):
        self.keycloak_admin.group_set_permissions(group_id=group_id, enabled=enabled)
