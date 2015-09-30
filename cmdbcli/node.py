import logging

from cliff.lister import Lister
from cliff.show import ShowOne

from utils import pretty_value


class NodeList(Lister):
    """
    list nodes
    """

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(self.__class__, self).get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):

        nodes = self.app.cmdb_api.get('/node/')
        return (('Id', 'Name'),
                ((n['id'], n['name']) for n in nodes['objects'])
                )


class NodeShow(ShowOne):
    """
    show details about a node
    """

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(self.__class__, self).get_parser(prog_name)
        parser.add_argument('name', nargs=1)
        return parser

    def take_action(self, parsed_args):
        node = self.app.cmdb_api.get('node/{}/'.format(parsed_args.name[0]))

        fields = node.keys()
        values = []
        for field in fields:
            values.append(pretty_value(node[field]))
        return (fields, values)
