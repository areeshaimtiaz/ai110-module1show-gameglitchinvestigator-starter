from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# --- Tests targeting the swapped higher/lower message bug ---

def test_high_guess_message_says_go_lower():
    # Bug: when guess > secret the message incorrectly said "Go HIGHER!"
    # instead of telling the player to go lower.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message but got: {message!r}"

def test_low_guess_message_says_go_higher():
    # Bug: when guess < secret the message incorrectly said "Go LOWER!"
    # instead of telling the player to go higher.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message but got: {message!r}"

def test_high_guess_message_does_not_say_go_higher():
    # Explicitly guard against the original swapped message.
    _, message = check_guess(99, 1)
    assert "HIGHER" not in message, f"Message should not say HIGHER when guess is too high: {message!r}"

def test_low_guess_message_does_not_say_go_lower():
    # Explicitly guard against the original swapped message.
    _, message = check_guess(1, 99)
    assert "LOWER" not in message, f"Message should not say LOWER when guess is too low: {message!r}"
