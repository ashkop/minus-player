from transport import MinusTransport


class MinusAuth(object):

    client_id = ''
    client_secret = ''
    access_token = None
    refresh_token = None
    scope = 'read_all'
    __logged_in = False

    def authenticate(self, username, password):
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'username': username,
            'password': password,
            'scope': self.scope,
            'grant_type': 'password'
        }
        try:
            response = MinusTransport.post('oauth/token', params=params)
        except Exception, exc:
            return False

        self.access_token = response['access_token']
        self.refresh_token = response['refresh_token']
        self.__logged_in = True
        return True

    def refresh_token(self):
        pass

    def is_logged_in(self):
        return self.__logged_in