import logging

from utils import Api, pretty_value

from cliff.lister import Lister
from cliff.show import ShowOne


class GeneralList(Lister):
    """
    """

    log = logging.getLogger(__name__)

    def __init__(self, app, app_args, cmd_name=None):
        super(GeneralList, self).__init__(app, app_args, cmd_name=cmd_name)
        self.path = ''
        self.columns = None
        self.mapping = {}

    def take_action(self, parsed_args):
        json = self.app.cmdb_api.get(self.path)

        objects = json.get('objects', [])
        if not self.columns and objects:
            # print all columns
            self.columns = objects[0].keys()

        mapping = {k.lower(): self.mapping[k].lower() for k in self.mapping}
        result = [[s.title() for s in self.columns]]
        values = []
        for record in objects:
            tmp = []
            for column in self.columns:
                lc = column.lower()
                if lc in mapping and record[lc]:
                    # translate value
                    tmp.append(record[lc][mapping[lc]])
                else:
                    # print raw value
                    tmp.append(record[lc])
            values.append(tmp)

        result.append(values)
        return result


class PropertyList(GeneralList):
    """
    list properties
    """

    def __init__(self, app, app_args, cmd_name=None):
        super(PropertyList, self).__init__(app, app_args, cmd_name=cmd_name)
        self.path = '/property/'
        self.columns = ('id', 'item', 'name', 'value', 'created', 'modified')
        self.mapping = {'item': 'name'}


class ItemList(GeneralList):
    """
    list items
    """

    def __init__(self, app, app_args, cmd_name=None):
        super(ItemList, self).__init__(app, app_args, cmd_name=cmd_name)
        self.path = '/item/'
        self.columns = ('id', 'name', 'parent', 'item_type', 'location')
        self.mapping = {'parent': 'name', 'item_type': 'name', 'location': 'name'}


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
