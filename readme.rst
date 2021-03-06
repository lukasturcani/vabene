:Author: Lukas Turcani
:Documentation: https://vabene.readthedocs.io

.. image:: https://i.imgur.com/ifNvkO4.jpg

Vabene
======

.. image:: https://travis-ci.com/lukasturcani/vabene.svg?branch=master
    :target: https://travis-ci.com/github/lukasturcani/vabene

.. image:: https://readthedocs.org/projects/vabene/badge/?version=latest
    :target: https://vabene.readthedocs.io

.. image:: https://img.shields.io/lgtm/grade/python/g/lukasturcani/vabene.svg?logo=lgtm&logoWidth=18)
    :target: https://lgtm.com/projects/g/lukasturcani/vabene

----

``vabene`` is a Python library for creating molecular graphs, which
obey user-defined valence restrictions. You can install it with::

    pip install vabene


Simple Example
---------------

This is a quick demonstration of the API, look at the docs for more
detailed examples

.. code-block:: python

    import vabene as vb

    atom_factory = vb.RandomAtomFactory(
        # The atoms, which are randomly picked for use in our molecular
        # graph. Each atom can be picked multiple times.
        # vb.Atom(atomic_number, charge, max_valence)
        atoms=(vb.Atom(6, 0, 4), vb.Atom(7, 0, 3)),
        # The total number of atoms the factory will produce.
        num_atoms=10,
    )
    # The atoms our molecular graph will use.
    atoms = tuple(atom_factory.get_atoms())

    # Used to generate a random set of bonds for our atoms.
    bond_factory = vb.RandomBondFactory()
    bonds = bond_factory.get_bonds(atoms)

    # Our molecular graph.
    molecule = vb.Molecule(atoms, bonds)

----

Other atom and bond factories will be added in the future. For example,
factories which can be used to produce an exhaustive set of possible
molecular graphs, which fulfill user-defined restrictions.
