import logging
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        #logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def getTitle(url):
    logger.info(f'Checking URL: {url}')

    try:
        html = urlopen(url)
    except HTTPError as e:
        logger.error(f'HTTP Error: {e}')
        return None
    else:
        logger.info('Server exists')

    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        logger.error(f'Attribute Error: {e}')
        return None
    else:
        logger.info('Body tag exists')

    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")

if title is None:
    logger.warning("Title could not be found")
else:
    logger.info(f'Title found: {title}')
    
