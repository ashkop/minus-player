class MinusFile:

    def __init__(self, **kwargs):

        self.name = kwargs.get('name')
        self.url = kwargs.get('url')
        self.thumbnail_url = kwargs.get('thumbnail_url')