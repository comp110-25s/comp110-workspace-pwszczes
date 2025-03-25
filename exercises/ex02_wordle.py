"""Program for the Wordle game"""

__author__ = "730643202"


def contains_char(word: str, char: str) -> bool:
    """Determines whether char is found in word"""
    assert len(char) == 1, f"len('{char}') is not 1"
    idx: int = 0
    while idx < len(word):
        if word[idx] == char:
            return True
        idx += 1
    return False


def emojified(guess: str, actual: str) -> str:
    """See if guess word is same as actual word"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(actual), "Guess must be same length as secret"
    idx: int = 0
    value: str = ""
    while idx < len(actual):
        if contains_char(actual, guess[idx]):
            if actual[idx] == guess[idx]:
                value = value + GREEN_BOX
            else:
                value = value + YELLOW_BOX
        else:
            value = value + WHITE_BOX
        idx += 1
    return value


def input_guess(length: int) -> str:
    "Prompt user for guess and prompt until they have guess of expected length" ""
    word = input(f"Enter a {length} character word")
    while len(word) != length:
        word = input(f"That wasn't {length} chars! Try again:")
    return word


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    max_turns: int = 6
    word_length: int = len(secret)
    hasWon: bool = False
    while not hasWon and turns < max_turns + 1:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess = input_guess(word_length)
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turns}/{max_turns} turns!")
            hasWon = True
        elif turns == max_turns:
            print("X/6 - Sorry, try again tomorrow!")
        turns += 1


if __name__ == "__main__":
    main(secret="codes")
