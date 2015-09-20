import logging
import utils

from cliff.lister import Lister


class ItemList(Lister):
    """
    List items from CMDB
    """

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        items = utils.cmdb_get()
        return (('Id', 'Name'),
                ((i['id'], i['name']) for i in items['objects'])
                )
