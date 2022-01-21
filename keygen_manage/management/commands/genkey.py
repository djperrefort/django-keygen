"""Defines logic for the generation of custom security keys."""

import string
from argparse import ArgumentParser

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    """Secret key generator"""

    help = 'Generates and prints a new secret key'

    @property
    def default_char_set(self):
        return string.ascii_letters + string.digits + string.punctuation

    def gen_secret_key(self, length: int = 50, chars: str = None) -> str:
        """Generate a secret key for Django

        Args:
            length: The length of the key
            chars: Optionally use only the given characters
        """

        chars = chars or self.default_char_set
        if length <= 0:
            raise ValueError('Key length must be greater than zero.')

        return get_random_string(length, chars)

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

    def handle(self, *args, **options) -> None:
        """Handle a command line call for the parent class"""

        self.stdout.write(
            self.gen_secret_key(options['length'], options['chars'])
        )
