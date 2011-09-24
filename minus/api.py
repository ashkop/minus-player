from minus.folder import MinusFolder

class MinusApi:


    def __init__(self, transport, auth):
        """
        @type transport: RestTransport
        @type auth: MinusAuth
        """
        self.__transport = transport
        self.__auth = auth

    def get_user_folders(self, user=None):
        if user is None: #defaults to active user
            user = self.get_active_user()


        folders = self.__transport.get('api/v2/users/'+user+'/folders', {})
        result = []
        for folder in folders['results']:
            result.append(MinusFolder(**folder))

        return result


    def get_active_user(self):
        pass