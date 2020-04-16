import pytest


@pytest.fixture(
    params=(
    ),
)
def case_data(request):
    return request.param
