import logging

from utils import Api, pretty_value

from cliff.lister import Lister
from cliff.show import ShowOne


class List(Lister):
    """
    list nodes
    """

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        api = Api('http://127.0.0.1:8081/api/v1/', 'root', 'cmdb')

        modul = self.cmd_name.split()[0]
        nodes = api.get(modul + '/')
        return (('Id', 'Name'),
                ((n['id'], n['name']) for n in nodes['objects'])
                )


class Show(ShowOne):
    """
    show details about a node
    """

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Show, self).get_parser(prog_name)
        parser.add_argument('name', nargs=1)
        return parser

    def take_action(self, parsed_args):
        api = Api('http://127.0.0.1:8081/api/v1/', 'root', 'cmdb')

        modul = self.cmd_name.split()[0]
        node = api.get('{}/{}/'.format(modul, parsed_args.name[0]))

        fields = node.keys()
        values = []
        for field in fields:
            values.append(pretty_value(node[field]))
        return (fields, values)
