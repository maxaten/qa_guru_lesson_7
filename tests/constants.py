import os

CURRENT_FILE_PATH = os.path.abspath(__file__)
PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(CURRENT_FILE_PATH))
RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, 'resources')
PROJECT_PATH_TMP = os.path.join(PROJECT_ROOT_PATH, 'tmp')