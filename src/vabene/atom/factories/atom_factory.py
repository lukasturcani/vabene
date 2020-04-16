"""
Atom Factory
============

"""


class AtomFactory:
    """
    Abstract base class for :class:`.Atom` factories.

    """

    # Keep empty __init__() to hide ugly default docstring.
    def __init__(self):
        """"""

    def get_atoms(self):
        """
        Yield the atoms of a molecule.

        Yields
        ------
        :class:`.Atom`
            An atom.

        """

        raise NotImplementedError()
