class CaseData:
    """
    A test case.

    Attributes
    ----------
    bond_factory : :class:`.BondFactory`
        The bond factory to test.

    atoms : :class:`tuple` of :class:`.Atom`
        The atom to pass to :meth:`.BondFactory.get_bonds`.

    bonds : :class:`tuple` of :class:`.Bond`
        The bonds which should get made.

    """

    def __init__(self, bond_factory, atoms, bonds):
        """
        Initialize a :class:`.CaseData` instance.

        Parameters
        ----------
        bond_factory : :class:`.BondFactory`
            The bond factory to test.

        atoms : :class:`tuple` of :class:`.Atom`
            The atom to pass to :meth:`.BondFactory.get_bonds`.

        bonds : :class:`tuple` of :class:`.Bond`
            The bonds which should get made.

        """

        self.bond_factory = bond_factory
        self.atoms = atoms
        self.bonds = bonds
