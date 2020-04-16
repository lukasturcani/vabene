"""
Bond Factory
============

"""


class BondFactory:
    """
    Abstract base class for :class:`.Bond` factories.

    """

    # Keep empty __init__() to hide ugly default docstring.
    def __init__(self):
        """"""

    def get_bonds(self, atoms):
        """
        Yield the bonds of a molecule.

        Parameters
        ----------
        atoms : :class:`tuple` of :class:`.Atom`
            The atoms of the molecule.

        Yields
        ------
        :class:`.Bond`
            A bond.

        """

        raise NotImplementedError()
