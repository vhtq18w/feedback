from config.deployment import DeploymentConfig
from config.development import DevelopmentConfig
from config.testing import TestingConfig


config = {
    'default': DevelopmentConfig,
    'deployment': DeploymentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
