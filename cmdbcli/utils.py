import logging
import json
# import pprint
import re
import requests
import urlparse


class Api():
    """
    API class for CMDB
    """

    log = logging.getLogger(__name__)

    # disable logging of request module
    logging.getLogger("requests").setLevel(logging.WARNING)

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def get(self, path):
        """
        API get method
        """

        complete_url = self.url + '/' + path
        complete_url = urlparse.urljoin(complete_url, re.sub('/{2,}', '/', urlparse.urlparse(complete_url).path))
        self.log.debug('get: ' + complete_url)

        r = requests.get(complete_url, auth=(self.username, self.password))
        self.log.debug('status code: {}'.format(r.status_code))
        return r.json()


def pretty_value(value):
    # return pprint.pformat(value).replace('u\'', '\'')
    return json.dumps(value, indent=None)
