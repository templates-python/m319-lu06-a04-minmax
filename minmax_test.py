from minmax import main


def test(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Total: 78.75\n"
