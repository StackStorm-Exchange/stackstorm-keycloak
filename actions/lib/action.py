from st2actions.runners.pythonrunner import Action

# https://bitbucket.org/agriness/python-keycloak.git
from keycloak import KeycloakAdmin

class KeycloakBaseAction(Action):

    def _get_client(self):
        host = self.config['host']
        port = self.config['port']
        scheme = self.config['scheme']
        realm = self.config['realm']
        user = self.config['user']
        password = self.config['password']


        keycloak_admin = KeycloakAdmin(server_url=scheme + "://" + host + ":" + port + "/auth/",
                       username=user,
                       password=password,
                       realm_name=realm)

        return keycloak_admin
