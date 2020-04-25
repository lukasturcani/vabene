"""
Atom Factory
============

"""

__all__ = ('AtomFactory', )


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
