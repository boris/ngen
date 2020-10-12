from argparse import Action, ArgumentParser

db = "example.kdbx"

def create_ngen():
    ngen = ArgumentParser()
    ngen.add_argument('db', help="DB where the secrets are stored.")
    ngen.add_argument('--list', '-l', help="List secrets stored in the DB.")
    ngen.add_argument('--copy', '-c', help="Copy secret to clipboard")
    return ngen
