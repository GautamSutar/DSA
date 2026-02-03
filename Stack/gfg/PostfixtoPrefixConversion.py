def isOperator(c):
    if c == "+" or c == "-" or c == "*" or c == "/" or c == "^":
        return True
    else:
        return False


def postToPre(post_exp):
    st = []
    length = len(post_exp)
    for i in range(length):
        if isOperator(post_exp[i]):
            op1 = st[-1]
            st.pop()
            op2 = st[-1]
            st.pop()
            temp = post_exp[i] + op2 + op1
            st.append(temp)
        else:
            st.append(post_exp[i])

    ans = ""
    for i in st:
        ans += i
    return ans


post_exp = "AB+CD-*"
print("prefix : ", postToPre(post_exp))
