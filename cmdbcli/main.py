import os
import sys

from cliff.app import App
from cliff.commandmanager import CommandManager
from cliff.interactive import cmd2

from utils import Api

# list and show will be used in our application
del cmd2.Cmd.do_list
del cmd2.Cmd.do_show


class CmdbCliApp(App):

    def __init__(self):
        command = CommandManager('cmdbcli')
        super(CmdbCliApp, self).__init__(
            description='CLI for CMDB',
            version='0.1',
            deferred_help=True,
            command_manager=command,
        )

    def build_option_parser(self, description, version, argparse_kwargs=None):
        self.LOG.debug('build_option_parser')
        parser = super(CmdbCliApp, self).build_option_parser(description, version, argparse_kwargs)
        parser.add_argument('--url', action='store', default=None, help='CMDB API URL')
        parser.add_argument('--username', action='store', default=None, help='CMDB API username')
        parser.add_argument('--password', action='store', default=None, help='CMDB API password')
        return parser

    def initialize_app(self, argv):
        self.LOG.debug('initialize_app')

        # credentials
        self.cmdb_url = self.options.url or os.environ.get('CMDB_URL', '')
        self.cmdb_user = self.options.username or os.environ.get('CMDB_USER', '')
        self.cmdb_password = self.options.password or os.environ.get('CMDB_PASSWORD', '')

        # api
        self.cmdb_api = Api(self.cmdb_url, self.cmdb_user, self.cmdb_password)

    def prepare_to_run_command(self, cmd):
        self.LOG.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)


def main(argv=sys.argv[1:]):
    myapp = CmdbCliApp()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
