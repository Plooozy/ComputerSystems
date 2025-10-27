from week_5.guess.Guessing import Guessing

# for testing I use pytest

def test_guessing_correct_first_try(monkeypatch, capsys):
    # 1. Change randrange, so it's 50
    monkeypatch.setattr("week_5.guess.Guessing.randrange", lambda a, b: 50)
    # 2. Change input, so input would be 50
    monkeypatch.setattr("builtins.input", lambda _: "50")
    # 3. Launch
    Guessing()
    # 4. Check output
    captured = capsys.readouterr()
    # 5. Check what did program print
    assert "Congratulations" in captured.out
    assert "Random number was: 50" in captured.out

def test_guessing_too_high_then_correct(monkeypatch, capsys):
    # 1. Change randrange, so it's 50
    monkeypatch.setattr("week_5.guess.Guessing.randrange", lambda a, b: 50)
    # 2. Change input, so input at first would be 100 and then 50
    inputs = iter(["100", "50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    # 3. Launch
    Guessing()
    # 4. Check output
    captured = capsys.readouterr().out
    # 5. Check if program print did "Too high"
    # 6. Check if program print did "Congratulations"
    assert "Too high" in captured
    assert "Congratulations" in captured


def test_guessing_too_low_then_correct(monkeypatch, capsys):
    # 1. Change randrange, so it's 50
    monkeypatch.setattr("week_5.guess.Guessing.randrange", lambda a, b: 50)
    # 2. Change input, so input at first would be 10 and then 50
    inputs = iter(["10", "50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    # 3. Launch
    Guessing()
    # 4. Check output
    captured = capsys.readouterr().out
    # 5. Check if program print did "Too low"
    # 6. Check if program print did "Congratulations"
    assert "Too low" in captured
    assert "Congratulations" in captured


def test_out_of_guess(monkeypatch, capsys):
    # 1. Change randrange, so it's 50
    monkeypatch.setattr("week_5.guess.Guessing.randrange", lambda a, b: 50)
    # 2. Change input, so inputs are 1, 2, 3, 4, 5 to get message "out of guesses"
    inputs = iter(["1", "2", "3", "4", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    # 3. Launch
    Guessing()
    # 4. Check output
    captured = capsys.readouterr().out
    # 5. Check if program print did "Too low"
    # 6. Check if program print did "You are out of guesses"
    # 7. Check if program print did "The number was"
    assert "Too low" in captured
    assert "You are out of guesses" in captured
    assert "The number was" in captured


def test_string_input(monkeypatch, capsys):
    # 1. Change randrange, so it's 50
    monkeypatch.setattr("week_5.guess.Guessing.randrange", lambda a, b: 50)
    # 2. Change input, so inputs are "Bus" and then 50
    inputs = iter(["Bus", "50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    # 3. Launch
    Guessing()
    # 4. Check output
    captured = capsys.readouterr().out
    # 5. Check if program print did "You did not enter a number"
    # 6. Check if program print did "Congratulations"
    assert "You did not enter a number" in captured
    assert "Congratulations" in captured


def test_more_than_100(monkeypatch, capsys):
    # 1. Change randrange, so it's 50
    monkeypatch.setattr("week_5.guess.Guessing.randrange", lambda a, b: 50)
    # 2. Change input, so inputs are 200 then "Bus" and then 50
    inputs = iter(["200", "Bus", "50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    # 3. Launch
    Guessing()
    # 4. Check output
    captured = capsys.readouterr().out
    # 5. Check if program print did "Number must be between 1 and 100"
    # 6. Check if program print did "You did not enter a number"
    # 7. Check if program print did "Congratulations"
    assert "Number must be between 1 and 100" in captured
    assert "You did not enter a number" in captured
    assert "Congratulations" in captured
