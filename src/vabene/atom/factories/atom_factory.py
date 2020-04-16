"""
Atom Factory
============

.. toctree::
    :maxdepth: 2

    Random Atom Factory <vabene.atom.factories.random_atom.factory>

"""


class AtomFactory:
    """
    Abstract base class for :class:`.Atom` factories.

    """

    def get_atoms(self):
        """
        Yield the atoms of a molecule.

        Yields
        ------
        :class:`.Atom`
            An atom.

        """

        raise NotImplementedError()
