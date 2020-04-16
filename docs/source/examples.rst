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

Forcing Atoms to be Present in Random Graphs
--------------------------------------------

Sometimes, we want to have a random molecular graph, subject to the
constraint that it is guaranteed to include a specific atom, or
group of atoms. The `required_atoms` parameter of the
:class:`.RandomAtomFactory` allows us to do this.

.. code-block:: python

    import vabene as vb

    atom_factory = vb.RandomAtomFactory(
        atoms=(vb.Atom(6, 0, 4), vb.Atom(7, 0, 3)),
        # The factory is guaranteed to produce these atoms every time
        # get_atoms() is called. These atoms will not be included in
        # the random selection, unless they were provided to the
        # "atoms" parameter too.
        required_atoms=(vb.Atom(35, 0, 1), vb.Atom(35, 0, 1)),
        num_atoms=10,
    )
    # A random set of carbon and nitrogen atoms, together with 2
    # bromine atoms.
    atoms = tuple(atom_factory.get_atoms())


Forcing Bonds to be Present in Random Graphs
--------------------------------------------

Sometimes, we want to have a random molecular graph, but we want to
force it to have a certain substructure. For example, let's assume
that we want to make a random molecule graph, but we want to
guarantee that it has a ``BrCCCBr`` substructure.

First, lets create a :class:`.RandomAtomFactory`, which is forced to
yield these atoms

.. code-block:: python

    import vabene as vb

    atom_factory = vb.RandomAtomFactory(
        atoms=(vb.Atom(6, 0, 4), vb.Atom(7, 0, 3)),
        required_atoms=(
            vb.Atom(35, 0, 1),
            vb.Atom(6, 0, 4),
            vb.Atom(6, 0, 4),
            vb.Atom(6, 0, 4),
            vb.Atom(35, 0, 1),
        ),
        num_atoms=10,
    )
    atoms = tuple(atom_factory.get_atoms())


Next, lets create a `.RandomBondFactory`, which force to yield the
necessary bond, as well as other, random, bonds


.. code-block:: python

    bond_factory = vb.RandomBondFactory(
        # We know what atom ids to use for the bonds, because
        # RandomAtomFactory will yield that required_atoms first, in
        # the order that we provided them.
        required_bonds=(
            vb.Bond(0, 1, 1),
            vb.Bond(1, 2, 1),
            vb.Bond(2, 3, 1),
            vb.Bond(3, 4, 1),
        ),
    )
    bonds = bond_factory.get_bonds(atoms)

Finally, we can make a random :class:`.Molecule`, which is guaranteed
to have the ``BrCCCBr`` substructure

.. code-block:: python

    molecule = vb.Molecule(atoms, bonds)

Here is the one I got:

.. image::
