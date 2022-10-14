import pytest


def check_printable(answers, results, line):
    def _test_step(step):
        if len(answers) <= step:
            pytest.fail(f'Пункт {step + 1} не существует')
        if len(results) <= step:
            pytest.fail(f'Ожидалось хотя бы {step + 1} строк в выводе, выведено {len(results)}')
        assert str(answers[step]) == results[step]  # Выведен неверный результат

    lines = [line]
    if line is None:
        lines = list(range(len(answers)))
    for line in lines:
        _test_step(line)
