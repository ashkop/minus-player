class MinusFolder:

    def __init__(self, **kwargs):

        self.id = kwargs.get('id')
        self.file_order = kwargs.get('item_ordering', [])
        self.name = kwargs.get('name')
        self.files_url = kwargs.get('files')
        self.files_count = kwargs.get('item_count', 0)