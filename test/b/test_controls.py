import sys

import pytest
import inspect

from io import StringIO
import re

from test.common.mockit import mock, mock_print
from test.common.context import get_integer, get_float
from test.common.modules import unload


TEST_CASES = [
    (
        10, 3, 'abacaba',
        ['10 3 abacaba', 6, 6, 4]
    )
]


@pytest.mark.parametrize(
    ['x', 'y', 'z', 'answers'],
    TEST_CASES
)
def test_arithmetics(x, y, z, answers, line):
    # noinspection PyUnboundLocalVariable
    unload('tasks.b.controls')

    with mock(get_integer).returns_many(x, y), mock(get_float).returns(z), \
            mock_print() as output:
        import tasks.b.arithmetics
        results = [line for line in output.getvalue().split('\n') if line.strip() != '']

    def _test_step(step):
        if len(answers) <= step:
            pytest.fail(f'Пункт {step + 1} не существует')
        if len(results) <= step:
            pytest.fail(f'Ожидалось хотя бы {step + 1} строк в выводе, выведено {len(results)}')
        assert str(answers[step]) == results[step]  # 'Выведен неверный результат'

    lines = [line]
    if line is None:
        lines = list(range(len(answers)))
    for line in lines:
        _test_step(line)


@pytest.mark.parametrize(
    ['x', 'y', 'z'],
    [tc[0:3] for tc in TEST_CASES]
)
def test_floats_count(x, y, z):
    unload('tasks.b.arithmetics')
    with mock(get_integer).returns_many(x, y), mock(get_float).returns(z), \
            mock_print() as output:
        import tasks.b.arithmetics
        results = [line for line in output.getvalue().split('\n') if line.strip() != '']

    def _is_type(s, typ):
        try:
            typ(s)
            return True
        except ValueError:
            return False

    cnt = -1
    for line in results:
        if _is_type(line, float) and not _is_type(line, int):
            cnt += 1
    if tasks.b.arithmetics.FLOATS != cnt:
        pytest.fail('Неверное число float\'ов')
