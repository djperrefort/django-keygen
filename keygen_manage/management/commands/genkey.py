from argparse import ArgumentParser

from django.core.management.base import BaseCommand

from keygen_manage import KeyGen


class Command(BaseCommand, KeyGen):
    """Secret key generator"""

    help = KeyGen.__doc__

    def add_arguments(self, parser: ArgumentParser) -> None:
        """Add arguments to a command line parser

        Adds ``len`` and ``chars`` arguments to CLI.

        Args:
            parser: The parser to add arguments to
        """

        parser.add_argument(
            'length', nargs='?', type=int, default=50,
            help='Length of the key to generate')

        parser.add_argument(
            'chars', type=str, default=self.default_char_set,
            help='Characters to include in the secret key')

    def handle(self, *args, **options) -> str:
        """Handle a command line call for the parent class"""

        key = self.gen_secret_key(options['length'], options['chars'])
        self.stdout.write(key)
        return key
