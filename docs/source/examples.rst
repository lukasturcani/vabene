Examples
========

Creating Random Molecular Graphs
--------------------------------

One of the simplest things you can do with :mod:`vabene`, is generate
random molecular graphs, which obey your chosen valence restrictions.
First, let's introduce the :class:`.Atom`. It has 3 parameters, the
atomic number, the formal charge and the maximum valence it is
allowed to have.

.. code-block:: python

    import vabene as vb

    # Create an uncharged carbon atom, which can have a valence of
    # up to 4.
    atom = vb.Atom(6, 0 , 4)

With that out of the way, we can use the :class:`.RandomAtomFactory`
to generate a random set of atoms, given we provide it with a
:class:`tuple` of atoms we want it to select from

.. code-block:: python

    atom_factory = vb.RandomAtomFactory(
        # The atoms, which are randomly picked for use in our molecular
        # graph. Each atom can be picked multiple times.
        atoms=(vb.Atom(6, 0, 4), vb.Atom(7, 0, 3)),
        # The total number of atoms the factory will produce.
        num_atoms=10,
    )
    # The atoms our molecular graph will use.
    atoms = tuple(atom_factory.get_atoms())

Now that we have a random set of atoms for use in our molecular graph,
we need to pair them with a random set of bonds. To get a random
set of bonds, we use the :class:`.RandomBondFactory`


.. code-block:: python

    bond_factory = vb.RandomBondFactory()
    bonds = bond_factory.get_bonds(atoms)

Now that we have our atoms and bonds, we can make a
:class:`.Molecule`

.. code-block:: python

    molecule = vb.Molecule(atoms, bonds)

Done. You made a molecule that looks something like this

.. image::


Yours will be different, because we didn't set a random seed.
However, you can use the `random_seed` parameter on the factories to
get reproducible results.

Forcing Atoms to be Selected in Random Graphs
---------------------------------------------

Sometimes, we want to have a random molecular graph, subject to the
constraint that it is guaranteed to include a specific atom, or
group of atoms. The `required_atoms` parameter of the
:class:`.RandomAtomFactory` allows us to do this.

.. code-block:: python

    import vabene as vb

    atom_factory = vb.RandomAtomFactory(
        atoms=(),
        required_atoms=(),
        num_atoms=(),
    )


Forcing Bonds to be Present in Random Graphs
--------------------------------------------
