from minmax import main


def test_random(capsys, monkeypatch):
    # Wir nutzen den monkeypatch, um die Benutzerangabe zu simulieren
    inputs = iter([15])  # Simulieren, dass der Benutzer 15 Zahlen eingibt
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    numbers = main()
    captured = capsys.readouterr()

    assert len(numbers) == 15  # Sicherstellen, dass genau 15 Zahlen erstellt wurden
    assert captured.out == f'{min(numbers)}\n{max(numbers)}\n'


def test_extended(capsys, monkeypatch):
    inputs = iter([31])  # Simulieren, dass der Benutzer 31 Zahlen eingibt
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    numbers = main()
    captured = capsys.readouterr()

    assert len(numbers) == 31  # Sicherstellen, dass genau 31 Zahlen erstellt wurden
    assert captured.out == f'{min(numbers)}\n{max(numbers)}\n'