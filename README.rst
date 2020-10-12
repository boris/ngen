Ngen
====

CLI for interacting with keepass-xc. The word **ngen** means *owner* in
`Mapudungún`_.

How does it work
----------------

Assumming that you have your `Keepassxc` DB in ``~/keepass/example.kdbx``, do
the following:

::

    $ ngen --help
    $ ngen list -d ~/keepass/example.kdbx
    $ ngen copy -d ~/keepass/example.kdbx -k Some/Secret
    $ ngen copy --db ~/keepass/example.kdbx --key Some/Secret

The above will do the following:

1. Print help
2. List the secrets in the DB defined
3. Copy the secret located in ``Some/Secret`` using the short format
4. Same above, but using long format


Dev list
--------

1. Ensure dependencies are installed.
2. Read keepass-xc DB from config.
3. Include wheel installer.
4. Read DB definition from config file.


.. _Mapudungún: https://en.wikipedia.org/wiki/Ngen
.. _Keepassxc: https://keepassxc.org/
