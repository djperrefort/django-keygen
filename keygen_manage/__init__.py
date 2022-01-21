"""Generation of secret keys for django applications security keys."""

import string
from warnings import warn

from django.utils.crypto import get_random_string

from keygen_manage.warnings import SecurityWarning


class KeyGen:
    """Generates and prints a new secret key"""

    @property
    def default_char_set(self):
        """Default character set used to generate secret keys"""

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

        if length < 30:
            warn(
                'Secret key length is short. Consider increasing the length of the generated key.',
                SecurityWarning)

        if len(set(chars)) < 20:
            warn(
                'Secret key generated with few unique characters. Try increasing the character set size.',
                SecurityWarning)

        return get_random_string(length, chars)
