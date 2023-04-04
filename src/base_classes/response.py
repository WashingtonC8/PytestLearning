class Response:
    def __init__(self, response):
        self.response = response
    def validate(self, schema):
        if isinstance(self.response, list):
            for item in self.response:
                validate(item)

        for item in received_posts:
            validate(item, POST_SCHEMA)