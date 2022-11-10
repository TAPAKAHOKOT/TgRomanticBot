from os import mkdir, getenv

from dotenv import load_dotenv
from loguru import logger

load_dotenv()

try:
    mkdir("Logs")
except FileExistsError:
    pass

logger.add('Logs/logs.log', format='{time} {level} {message}', \
           level=getenv('LOG_LEVEL', 'INFO'), rotation='1 MB', compression='zip')

logger.info('-' * 50)
logger.info('Logging start')
