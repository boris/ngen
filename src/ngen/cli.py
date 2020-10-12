import click
import subprocess

cmd = "keepassxc-cli"
db = "/home/boris/.keepassxc/worth.kdbx"

@click.group()
def cli():
    return True

@cli.command()
@click.option('--secret', default='/')
def list(secret):
    subprocess.run([cmd, 'ls', db, secret])

@cli.command()
@click.option('--copy', default='')
@click.option('--key', default='')
def copy(copy, key):
    #os.system("{} clip {} {}".format(cmd, db, key))
    subprocess.run([cmd, 'clip', db, key])
