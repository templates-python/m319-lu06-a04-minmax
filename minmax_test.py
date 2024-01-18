from minmax import main


def test_random(capsys):
    numbers = main()
    captured = capsys.readouterr()
    assert captured.out == f'{min(numbers)}\n{max(numbers)}\n'


def test_extended(capsys, monkeypatch):
    inputs = iter([31])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    numbers = main()
    assert len(numbers) == 31
    captured = capsys.readouterr()
    assert captured.out == f'{min(numbers)}\n{max(numbers)}\n'

