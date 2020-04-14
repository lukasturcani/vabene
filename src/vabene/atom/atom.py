"""
Atom
====

"""


class Atom:
    """
    An atom of a molecule.

    """

    def __init__(self, atomic_number, charge, valid_valences):
        """
        Initialize an :class:`.Atom` instance.

        Parameters
        ----------
        atomic_number : :class:`int`
            The atomic number of the atom.

        charge : :class:`int`
            The formal charge of the atom.

        valid_valences : :class:`frozenset` of :class:`int`
            The valences the atom is allowed to have.

        """

        self._atomic_number = atomic_number
        self._charge = charge
        self._valid_valences = valid_valences

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

    def get_valid_valences(self):
        """
        Return the valences the atom is allowed to have.

        Returns
        -------
        :class:`frozenset` of :class:`int`
            The valences the atom is allowed to have.

        """

        return self._valid_valences
