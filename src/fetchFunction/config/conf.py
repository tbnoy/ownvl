import configparser
import os.path
import os

conf = {
    'authUrl': os.environ.get('authUrl'),
    'waiversUrl': os.environ.get('waiversUrl'),
    'platformUrl': os.environ.get('platformUrl'),
    'profileToken': os.environ.get('profileToken'),
}