import click
import subprocess

cmd = "keepassxc-cli"
db = "/path/to/worth.kdbx"

@click.group()
def main():
    return True

@main.command()
@click.option('--secret', default='/')
@click.option('--db', '-d', default=db)
def list(secret, db):
    subprocess.run([cmd, 'ls', db, secret])

@main.command()
@click.option('--copy', default='')
@click.option('--key', default='')
def copy(copy, key):
    subprocess.run([cmd, 'clip', db, key])
