from sys import version_info
import motor.motor_asyncio
import configparser
import sys
import os


modules_help = {}
requirements_list = []

github = '<a href=https://github.com/Deanonparnisha/Black-Rose-Userbot> github</a>'


config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)


def get_prefix():
    prefix = config.get("prefix", "prefix")
    return prefix
        

try:
    prefix = get_prefix()

except Exception as e:
    config.add_section("prefix")
    config.set('prefix', 'prefix', '.')
    with open(config_path, "w") as config_file:
        config.write(config_file)
    prefix = '.'
