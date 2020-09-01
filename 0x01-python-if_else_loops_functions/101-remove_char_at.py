def remove_char_at(str, n):
    word = ""
    for i, c in enumerate(str):
        if i != n:
            word += c
    return word
