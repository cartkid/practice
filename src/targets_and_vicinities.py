def getTV(actual: str, guess: str):
    # fill in
    targets: int = 0
    vicinities: int = 0

    matches_removed_actual = []
    matches_removed_guess = []

    for idx, guessed in enumerate(guess):
        if guessed == actual[idx]:
            targets += 1
        else:
            matches_removed_actual.append(actual[idx])
            matches_removed_guess.append(guessed)

    for idx, guessed in enumerate(matches_removed_guess):
        if guessed in matches_removed_actual:
            vicinities += 1

    return f"{targets}T{vicinities}V"
