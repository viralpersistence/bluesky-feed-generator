import sys
from dotenv import load_dotenv
from server.logger import logger

'''
load_dotenv()

logger.info(sys.path)

path = '/home/viralpersistence/bluesky-feed-generator/'
if path not in sys.path:
   sys.path.insert(0, path)

logger.info(sys.path)
'''

from server.app import app as application