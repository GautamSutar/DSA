def longest_substring(s):
    result = ""
    c = 0
    for ch in s:
        if ch not in result:
            result += ch
            c += 1

    return c


print(longest_substring("abcabcbb"))
