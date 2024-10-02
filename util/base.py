from util.config_loader import load_config
import os
from locust import HttpUser

env = os.getenv('LOCUST_ENV', 'prod')
config = load_config(env)


class BaseUser(HttpUser):
    abstract = True
    host = config['host']
