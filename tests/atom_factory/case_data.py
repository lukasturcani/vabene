class CaseData:
    """
    A test case.

    Attributes
    ----------
    atom_factory : :class:`.AtomFactory`
        The atom factory to test.

    atoms : :class:`tuple` of :class:`.Atom`
        The atoms which should be created.

    """

    def __init__(self, atom_factory, atoms):
        """
        Initialize a :class:`.CaseData` instance.

        Parameters
        ----------
        atom_factory : :class:`.AtomFactory`
            The atom factory to test.

        atoms : :class:`tuple` of :class:`.Atom`
            The atoms which should be created.

        """

        self.atom_factory = atom_factory
        self.atoms = atoms
