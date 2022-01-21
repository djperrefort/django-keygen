from argparse import ArgumentParser
from unittest import TestCase, mock

from keygen_manage import KeyGen
from keygen_manage.management.commands.genkey import Command


class CliDocumentation(TestCase):
    """Test the command line parser help text is set"""

    def runTest(self) -> None:
        self.assertEqual(KeyGen.__doc__, Command.help)


class CliParsing(TestCase):
    """Test for the parsing of command line arguments"""

    def test_for_cli_arguments(self) -> None:
        """Test arguments are added to the command line parser"""

        command = Command()
        test_parser = ArgumentParser()
        command.add_arguments(test_parser)

        self.assertEqual(50, test_parser.get_default('length'))
        self.assertEqual(command.default_chars, test_parser.get_default('chars'))

    @mock.patch('sys.stdout')
    def test_handle_output_to_stdout(self, mock_stdout) -> None:
        """Test the ``handle`` method outputs the generated key to stdout"""

        command = Command()
        key = command.handle(length=50, chars=command.default_chars)
        mock_stdout.write.assert_has_calls([
            mock.call(key + '\n')
        ])
