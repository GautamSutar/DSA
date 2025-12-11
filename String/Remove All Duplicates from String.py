def removeDuplicates(s):
    result = ""
    seen = set()

    for ch in s:
        if ch not in seen:
            result += ch
            seen.add(ch)

    return result


print(removeDuplicates("aabbccdd"))
