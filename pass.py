import click
import os

cmd = "keepassxc-cli"
db = "/home/boris/.keepassxc/worth.kdbx"

@click.group()
def cli():
    pass

@cli.command()
@click.option('--secret', default='/')
def list(secret):
    os.system("{} ls {} {}".format(cmd, db, secret))

@cli.command()
@click.option('--copy', default='')
@click.option('--key', default='')
def copy(copy, key):
    os.system("{} clip {} {}".format(cmd, db, key))
