def lengthOfLastWord(s: str) -> int:
    cleaned_text = s.strip()
    i = len(cleaned_text) - 1
    print(cleaned_text)
    print(i)
    if i == 0:
        return 1
    count = 0
    while i >= 0:
        if cleaned_text[i] == " ":
            break
        count += 1
        i -= 1
    return count    


print(lengthOfLastWord("    day"))

# ⏱️ Time Complexity - O(n) + O(n) -> O(n)
# ⏱️ Space Complexity - O(1) 
