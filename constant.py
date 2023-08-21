def solve(s):
    vowels = "aeiou"
    consonant_substrings = []
    current_substring = ""
    highest_value = 0

    for char in s:
        if char not in vowels:
            current_substring += char
        else:
            if current_substring != "":
                value = sum(ord(c) - ord('a') + 1 for c in current_substring)
                consonant_substrings.append(value)
                current_substring = ""

    if current_substring != "":
        value = sum(ord(c) - ord('a') + 1 for c in current_substring)
        consonant_substrings.append(value)

    if consonant_substrings:
        highest_value = max(consonant_substrings)

    return highest_value

print(solve("zodiacs"))   # Output: 26
print(solve("strength"))  # Output: 57