def replace_vowel(s):
    vowel = "aeiouAEIOU"
    result = ""
    for ch in s:
        if ch in vowel:
            result += "$"
        else:
            result += ch
    return result


def replace_consonats(s):
    vowel = "aeiouAEIOU"
    result = ""
    for ch in s:
        if ch.isalpha() and ch not in vowel:
            result += "#"
        else:
            result += ch
    return result


def toggle_case(s):
    result = ""
    for ch in s:
        if ch.islower():
            result += ch.upper()
        elif ch.isupper():
            result += ch.lower()
        else:
            result += ch
    return result


s1 = input()
s2 = input()
s3 = input()

a = replace_vowel(s1)
b = replace_consonats(s2)
c = toggle_case(s3)

print(a, b, c)
