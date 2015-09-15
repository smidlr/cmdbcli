import logging
import os
import requests

from cliff.lister import Lister


class Items(Lister):
    """
    List items from CMDB
    """

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        return (('Name', 'Size'),
                ((n, os.stat(n).st_size) for n in os.listdir('.'))
                )
