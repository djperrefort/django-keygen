"""Tests for the generation of secret keys"""

import string
from unittest import TestCase

from source.apps.keygen_manage.management.commands.genkey import Command


class KeyGeneration(TestCase):
    """Tests for the generation of secret keys"""

    def test_error_on_non_positive_length(self) -> None:
        """Test for a ``ValueError`` on a non-positive key"""

        with self.assertRaises(ValueError):
            Command().gen_secret_key(length=0)

        with self.assertRaises(ValueError):
            Command().gen_secret_key(length=-1)

    def test_returned_length(self) -> None:
        """Tet the returned key length matches the ``length`` argument"""

        for i in range(10, 25, 50):
            self.assertEqual(i, len(Command().gen_secret_key(i)))

    def test_sequential_not_equal(self) -> None:
        """Test sequential keys do not match"""

        # This isn't really a true test for randomness - those are very involved
        # However, it will protect a developer who left behind a seed while debugging
        self.assertNotEqual(
            Command().gen_secret_key(),
            Command().gen_secret_key()
        )


class DefaultCharSet(TestCase):
    """Tests for the character set used in key generation"""

    def assertSubsetChars(self, expected: str, actual: str) -> None:
        """Test if characters of the ``expected`` string are a subset of the ``actual`` string"""

        expected_set = set(expected)
        actual_set = set(actual)
        self.assertTrue(expected_set.issubset(actual_set))

    def test_contains_ascii_lower(self) -> None:
        """Test keys pull from lowercase letters"""

        self.assertSubsetChars(string.ascii_lowercase, Command().default_char_set)

    def test_contains_ascii_upper(self) -> None:
        """Test keys pull from uppercase letters"""

        self.assertSubsetChars(string.ascii_uppercase, Command().default_char_set)

    def test_contains_punctuation(self) -> None:
        """Test keys pull from punctuation"""

        self.assertSubsetChars(string.punctuation, Command().default_char_set)
