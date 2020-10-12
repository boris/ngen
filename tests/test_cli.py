from click.testing import CliRunner
import pytest
from ngen import cli

@pytest.fixture(scope="module")
def runner():
    return CliRunner()

def test_ngen_with_unknown_db(runner):
    """
    Will fail if the DB is unknown
    """
    result = runner.invoke(cli.main, ['list', 'fake.'])
    assert result.exit_code == 2

def test_ngen_with_known_db(runner):
    """
    Will not fail if the DB is known
    """
    result = runner.invoke(cli.main, ['list', '-d' , '~/.keepassxc/worth.kdbx'])
    assert result.exit_code == 0
