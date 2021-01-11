from click.testing import CliRunner
import pytest
import subprocess
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

def test_check_keepassxc_exists(runner):
    """
    Will fail if keepassxc-cli is not installed
    """
    process = subprocess.Popen(['keepassxc-cli', '-v'], stdout=subprocess.PIPE)
    out, _ = process.communicate()
    assert process.returncode == 0

def test_search_existent_item(runner):
    """
    Will not fail if the item exists
    """
    result = runner.invoke(cli.main, ['search', '-d' , '~/.keepassxc/worth.kdbx', '-t', 'Test'])
    assert result.exit_code == 0

def test_search_unexistent_item(runner):
    """
    Will fail if the item does not exists
    """
    result = runner.invoke(cli.main, ['search', '-d' , '~/.keepassxc/worth.kdbx', '-t', 'Fake'])
    assert result.output == ""
