import pytest
import vabene as vb

from .case_data import CaseData


@pytest.fixture(
    params=(
        CaseData(
            bond_factory=vb.RandomBondFactory(
                max_internal_bonds=0,
                required_bonds=(
                    vb.Bond(0, 1, 2),
                    vb.Bond(0, 2, 1),
                ),
                random_seed=None,
            ),
            atoms=(
                vb.Atom(6, 0, 4),
                vb.Atom(6, 0, 4),
                vb.Atom(6, 0, 4),
            ),
            bonds=(
                vb.Bond(0, 1, 2),
                vb.Bond(0, 2, 1),
            ),
        ),
    ),
)
def case_data(request):
    return request.param
