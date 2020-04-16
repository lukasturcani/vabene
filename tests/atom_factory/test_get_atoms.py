import itertools as it


def test_get_atoms(case_data):
    """
    Test :meth:`.AtomFactory.get_atoms`.

    Parameters
    ----------
    case_data : :class:`.CaseData`
        A test case. Holds the atom factory to test and the atoms which
        it should make.

    Returns
    -------
    None : :class:`NoneType`

    """

    _test_get_atoms(
        atom_factory=case_data.atom_factory,
        atoms=case_data.atoms,
    )


def _test_get_atoms(atom_factory, atoms):
    """
    Test :meth:`.AtomFactory.get_atoms`.

    Parameters
    ----------
    atom_factory : :class:`.AtomFactory`
        The atom factory to test.

    atoms : :class:`tuple` of :class:`.Atom`
        The atoms which should be created.

    Returns
    -------
    None : :class:`NoneType`

    """

    for atom1, atom2 in it.zip_longest(
            atom_factory.get_atoms(),
            atoms,
    ):
        assert atom1.get_atomic_number() == atom2.get_atomic_number()
        assert atom1.get_charge() == atom2.get_charge()
        assert atom1.get_valid_valences() == atom2.get_valid_valences()
