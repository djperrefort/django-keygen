"""Defines logic for the generation of custom security keys."""

import string

from django.utils.crypto import get_random_string


class KeyGen:
    """Generates and prints a new secret key"""

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
