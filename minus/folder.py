class MinusFolder:

    def __init__(self, **kwargs):

        self.id = kwargs.get('id')
        self.file_order = kwargs.get('file_order', [])
        self.name = kwargs.get('name')
        self.files_url = kwargs.get('file')