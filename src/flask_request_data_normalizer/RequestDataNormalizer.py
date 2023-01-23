from src.flask_request_data_normalizer.NormalizedRequest import NormalizedRequest

class RequestDataNormalizer:
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        app.request_class = NormalizedRequest