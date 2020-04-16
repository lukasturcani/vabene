"""
Bond
====

"""


class Bond:
    """
    A bond of a :class:`.Molecule`.

    """

    def __init__(self, atom1_id, atom2_id, order):
        """
        Initialize a :class:`.Bond` instance.

        Parameters
        ----------
        atom1_id : :class:`int`
            The id of the first atom of the bond.

        atom1_id : :class:`int`
            The id of the second atom of the bond.

        order : :class:`int`
            The order of the bond.

        """

        self._atom1_id = atom1_id
        self._atom2_id = atom2_id
        self._order = order

    def get_atom1_id(self):
        """
        Return the id of the first atom of the bond.

        Returns
        -------
        :class:`int`
            The id of the first atom of the bond.

        """

        return self._atom1_id

    def get_atom2_id(self):
        """
        Return the id of the second atom of the bond.

        Returns
        -------
        :class:`int`
            The id of the second atom of the bond.

        """

        return self._atom2_id

    def get_atom_ids(self):
        """
        Yield the ids of the atoms of the bond.

        Yields
        ------
        :class:`int`
            An atom id.

        """

        yield self._atom1_id
        yield self._atom2_id

    def get_order(self):
        """
        Return the bond order.

        Returns
        -------
        :class:`int`
            The bond order.

        """

        return self._order

    def __repr__(self):
        return (
            f'{self.__class__.__name__}('
            f'{self._atom1_id}, {self._atom2_id}, '
            f'{self._order}'
            ')'
        )

    def __str__(self):
        return repr(self)
