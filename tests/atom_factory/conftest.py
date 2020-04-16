import pytest
import vabene as vb

from .case_data import CaseData


@pytest.fixture(
    params=(
        CaseData(
            atom_factory=vb.RandomAtomFactory(
                atoms=(),
                num_atoms=2,
                required_atoms=(
                    vb.Atom(6, 0, 4),
                    vb.Atom(7, 2, 3),
                ),
                random_seed=None,
            ),
            atoms=(
                vb.Atom(6, 0, 4),
                vb.Atom(7, 2, 3),
            ),
        ),
        CaseData(
            atom_factory=vb.RandomAtomFactory(
                atoms=(),
                num_atoms=3,
                required_atoms=(
                    vb.Atom(6, 0, 4),
                    vb.Atom(7, 2, 3),
                ),
                random_seed=None,
            ),
            atoms=(
                vb.Atom(6, 0, 4),
                vb.Atom(7, 2, 3),
            ),
        ),
        CaseData(
            atom_factory=vb.RandomAtomFactory(
                atoms=(
                    vb.Atom(8, -1, 5),
                ),
                num_atoms=4,
                required_atoms=(
                    vb.Atom(6, 0, 4),
                    vb.Atom(7, 2, 3),
                ),
                random_seed=None,
            ),
            atoms=(
                vb.Atom(6, 0, 4),
                vb.Atom(7, 2, 3),
                vb.Atom(8, -1, 5),
                vb.Atom(8, -1, 5),
            ),
        ),
        CaseData(
            atom_factory=vb.RandomAtomFactory(
                atoms=(
                    vb.Atom(8, -1, 5),
                ),
                num_atoms=1,
                required_atoms=(
                    vb.Atom(6, 0, 4),
                    vb.Atom(7, 2, 3),
                ),
                random_seed=None,
            ),
            atoms=(
                vb.Atom(6, 0, 4),
            ),
        ),
    ),
)
def case_data(request):
    return request.param
