import logging

from utils import Api, pretty_value

from cliff.lister import Lister
from cliff.show import ShowOne


class NodeList(Lister):
    """
    list nodes
    """

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(self.__class__, self).get_parser(prog_name)
        parser.add_argument('--url', help='CMDB API URL')
        parser.add_argument('--user', help='CMDB API user')
        parser.add_argument('--password', help='CMDB API password')
        return parser

    def take_action(self, parsed_args):
        url = self.url if not parsed_args.url else parsed_args.url
        api = Api(url, 'root', 'cmdb')

        nodes = api.get('/node/')
        return (('Id', 'Name'),
                ((n['id'], n['name']) for n in nodes['objects'])
                )


class NodeShow(ShowOne):
    """
    show details about a node
    """

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(NodeShow, self).get_parser(prog_name)
        parser.add_argument('--url', default=self.url, help='CMDB API URL')
        parser.add_argument('name', nargs=1)
        return parser

    def take_action(self, parsed_args):
        api = Api('http://127.0.0.1:8081/api/v1/', 'root', 'cmdb')

        node = api.get('node/{}/'.format(parsed_args.name[0]))

        fields = node.keys()
        values = []
        for field in fields:
            values.append(pretty_value(node[field]))
        return (fields, values)
