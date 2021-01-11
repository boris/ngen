import click
import subprocess
import yaml
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../../config.yml')

cfg = open(filename, 'r')
cfg_yaml = yaml.load(cfg, Loader=yaml.FullLoader)
cmd = "keepassxc-cli"
db = cfg_yaml['db']

@click.group()
def main():
    return True

@main.command()
@click.option('--secret', '-s', default='/', help='Secret name')
@click.option('--db', '-d', default=db, help='DB to read the secrets from')
def list(secret, db):
    """
    List secrets in current DB
    """
    subprocess.run([cmd, 'ls', db, secret])

@main.command()
@click.option('--key', '-k', default='', help='Name of the secret to copy to clipboard')
@click.option('--db', '-d', default=db, help='DB to copy the secrets from')
def copy(key, db):
    """
    Copy selected secret
    """
    subprocess.run([cmd, 'clip', db, key])

@main.command()
@click.option('--term', '-t', default='', help='The term to be searched on the DB')
@click.option('--db', '-d', default=db, help='DB to copy secrets from')
def search(term, db):
    """
    Search 'term' on DB
    """
    subprocess.run([cmd, 'locate', db, term])
