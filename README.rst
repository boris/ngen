Ngen
====

CLI for interacting with keepass-xc. The word **ngen** means *owner* in
`Mapudungún`_.

Setup
-----
Copy ``config-example.yml`` to ``config.yml``. Modify the ``db`` line to point to your
file.

.. code-block:: yaml

    db: '/path/to/file.kdbx'

How does it work
----------------

Assumming that you have your `Keepassxc` DB in ``~/keepass/example.kdbx``, do
the following:

::

    $ ngen --help
    $ ngen list
    $ ngen copy --key Some/Secret
    $ ngen copy -k Some/Secret
    $ ngen search --term Secret
    $ ngen search -t Secret

Also, default DB, defined in ``config.yaml`` can be overwritten as follows:

::

    $ ngen list -d ~/keepass/example.kdbx
    $ ngen list --db ~/keepass/example.kdbx
    $ ngen copy -d ~/keepass/example.kdbx -k Some/Secret
    $ ngen copy --db ~/keepass/example.kdbx --key Some/Secret
    $ ngen search -d ~/keepass/example.kdbx Secret
    $ ngen search --db ~/keepass/example.kdbx Secret

The above will do the following:

1. Print help
2. List the secrets in the DB defined
3. Copy the secret located in ``Some/Secret`` using the short format
4. Same above, but using long format
5. Search for a term

Search feature:

- Is not case sensitive. Searching for 'Secret' will return the same as searching
  for 'secret'
- Includes substrings. Searching for 'Secre' will include 


Dev list
--------

1. Ensure dependencies are installed.
2. Read keepass-xc DB from config.
3. Include wheel installer.
4. Read DB definition from config file.


.. _Mapudungún: https://en.wikipedia.org/wiki/Ngen
.. _Keepassxc: https://keepassxc.org/
