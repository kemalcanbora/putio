from chalicelib.base_config import DefaultSettings


class DevelopmentConfig(DefaultSettings):
    def __init__(self):
        super(DevelopmentConfig, self).__init__()




settings = DevelopmentConfig()