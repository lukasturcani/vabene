"""
Atom
====

"""


class Atom:
    """
    An atom of a molecule.

    """

    def __init__(self, atomic_number, charge, max_valence):
        """
        Initialize an :class:`.Atom` instance.

        Parameters
        ----------
        atomic_number : :class:`int`
            The atomic number of the atom.

        charge : :class:`int`
            The formal charge of the atom.

        max_valence : :class:`int`
            The maximum valence the atom is allowed to have.

        """

        self._atomic_number = atomic_number
        self._charge = charge
        self._max_valence = max_valence

    def get_atomic_number(self):
        """
        Return the atomic number of the atom.

        Returns
        -------
        :class:`int`
            The atomic number of the atom.

        """

        return self._atomic_number

    def get_charge(self):
        """
        Return the formal charge of the atom.

        Returns
        -------
        :class:`int`
            The formal charge of the atom.

        """

        return self._charge

    def get_max_valence(self):
        """
        Return the maximum valence the atom is allowed to have.

        Returns
        -------
        :class:`int`
            The maximum valence the atom is allowed to have.

        """

        return self._max_valence

    def __repr__(self):
        return (
            f'{self.__class__.__name__}('
            f'{self._atomic_number}, {self._charge}, '
            f'{self._max_valence}'
            ')'
        )

    def __str__(self):
        return repr(self)
