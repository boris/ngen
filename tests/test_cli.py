import pytest
from ngen import cli

cmd = 'keepassxc-cli'
db = 'example.kdbx'

@pytest.fixture
def ngen():
    return cli.create_ngen()

def test_ngen_with_unknown_db(ngen):
    """
    Will fail if the DB is unknown
    """
    with pytest.raises(SystemExit) as e:
        ngen.parse_args([cmd, 'ls', 'null_db'])
    assert e.type == SystemExit
    assert e.value.code == 2

def test_ngen_with_known_db(ngen):
    """
    Will not fail if the DB is known
    """
    with pytest.raises(SystemExit) as e:
        ngen.parse_args([cmd, 'lsss', db])
    assert e.type == SystemExit
    assert e.value.code == 2

