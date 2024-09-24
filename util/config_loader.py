import json


def load_config(env):
    with open(f'environments/{env}_config.json') as config_file:
        return json.load(config_file)
