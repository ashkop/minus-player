from minus.file import MinusFile
from minus.folder import MinusFolder

class MinusApi:


    def __init__(self, transport):
        """
        @type transport: RestTransport
        @type auth: MinusAuth
        """
        self.__transport = transport

    def get_user_folders(self, user=None):
        if user is None: #defaults to active user
            user = self.get_active_user()


        folders = self.__transport.get('api/v2/users/'+user+'/folders', {})
        result = {}
        for folder in folders['results']:
            f = MinusFolder(**folder)
            result[f.id] = f

        return result

    def get_folder_files(self, folder):
        """
         Get list of file in folder
         @type folder: MinusFolder
        """
        if not isinstance(folder, MinusFolder):
            raise ValueError('MinusFolder instance expected')

        files = self.__transport.get('api/v2/folders/'+folder.id+'/files', {})

        result = {}
        for file in files['results']:
            f = MinusFile(**file)
            result[f.id] = f

        return result


    def get_active_user(self):
        pass