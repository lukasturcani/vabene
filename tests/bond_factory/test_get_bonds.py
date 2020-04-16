import itertools as it


def test_get_bonds(case_data):
    """
    Test :meth:`.BondFactory.get_bonds`.

    Parameters
    ----------
    case_data : :class:`.CaseData`
        A test case. Holds the factory to test and the bonds which
        it should make.

    Returns
    -------
    None : :class:`NoneType`

    """

    _test_get_bonds(
        bond_factory=case_data.bond_factory,
        atoms=case_data.atoms,
        bonds=case_data.bonds,
    )


def _test_get_bonds(bond_factory, atoms, bonds):
    """
    Test :meth:`.BondFactory.get_bonds`.

    Parameters
    ----------
    bond_factory : :class:`.BondFactory`
        The bond factory to test.

    atoms : :class:`tuple` of :class:`.Atom`
        The atom to pass to :meth:`.BondFactory.get_bonds`.

    bonds : :class:`tuple` of :class:`.Bond`
        The bonds which should get made.

    Returns
    -------
    None : :class:`NoneType`

    """

    for bond1, bond2 in it.zip_longest(
        bond_factory.get_bonds(atoms),
        bonds,
    ):
        assert bond1.get_atom1_id() == bond2.get_atom1_id()
        assert bond1.get_atom2_id() == bond2.get_atom2_id()
        assert bond1.get_order() == bond2.get_order()
