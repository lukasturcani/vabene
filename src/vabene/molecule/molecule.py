"""
Molecule
========

"""

from .utilities import dedupe


class Molecule:
    """
    A molecular graph.

    """

    def __init__(self, atoms, bonds):
        """
        Initialize a :class:`.Molecule` instance.

        Parameters
        ----------
        atoms : :class:`tuple` of :class:`.Atom`
            The atoms of the molecule.

        bonds : :class:`iterable` of :class:`.Bond`
            The bonds of the molecule.

        """

        self._atoms = atoms

        def get_atom_ids(bond):
            return frozenset(bond.get_atom_ids())

        self._bonds = tuple(dedupe(bonds, get_key=get_atom_ids))

    def get_atoms(self, atom_ids=None):
        """
        Yield the atoms of the molecule.

        Parameters
        ----------
        atom_ids : :class:`iterable` of :class:`int`
            The ids of the atoms which should be yielded. Can
            be an :class:`int`, if only one atom should
            be yielded.

        Yields
        ------
        :class:`.Atom`
            An atom of the molecule.

        """

        if atom_ids is None:
            atom_ids = range(len(self._atoms))
        elif isinstance(atom_ids, int):
            atom_ids = (atom_ids, )

        for atom_id in atom_ids:
            yield self._atoms[atom_id]

    def get_num_atoms(self):
        """
        Return the number of atoms in the molecule.

        Returns
        -------
        :class:`int`
            The number of atoms in the molecule.

        """

        return len(self._atoms)

    def get_bonds(self, bond_ids=None):
        """
        Yield the bonds of the molecule.

        Parameters
        ----------
        bond_ids : :class:`iterable` of :class:`int`
            The ids of bonds which should be yielded. Can be an
            :class:`int`, if only one bond should be yielded.

        Yields
        ------
        :class:`.Bond`
            A bond of the molecule.

        """

        if bond_ids is None:
            bond_ids = range(len(self._bonds))
        elif isinstance(bond_ids, int):
            bond_ids = (bond_ids, )

        for bond_id in bond_ids:
            yield self._bonds[bond_id]

    def get_num_bonds(self):
        """
        Return the number of bonds in the molecule.

        Returns
        -------
        :class:`int`
            The number of bonds in the molecule.

        """

        return len(self._bonds)
