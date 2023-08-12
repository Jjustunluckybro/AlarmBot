class RequestException(ValueError):

    def __init__(self, status: int, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.status = status


