import pytest
from main import check

FIXTURES = [('{[]{()}}', 'Сбалансированно'), ('[{}{})(]', 'Несбалансированно'), ('((()', 'Несбалансированно')]

@pytest.mark.parametrize('a, etalon', FIXTURES)
def test_check(a, etalon):
    result = check(a)
    assert result == etalon