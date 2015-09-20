import os
import sys

from cliff.app import App
from cliff.commandmanager import CommandManager
from cliff.interactive import cmd2

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

    def initialize_app(self, argv):
        self.LOG.debug('initialize_app')

    def prepare_to_run_command(self, cmd):
        # credentials
        cmd.url = os.environ.get('CMDB_URL', '')
        cmd.user = os.environ.get('CMDB_USER', '')
        cmd.password = os.environ.get('CMDB_PASSWORD', '')

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
