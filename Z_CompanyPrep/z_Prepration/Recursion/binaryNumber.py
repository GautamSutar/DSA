def binary(number) -> float:
    result = []

    def convertBinary(curr_string):
        if len(curr_string) == number:
            result.append(curr_string)
            return
        convertBinary(curr_string + "0")

        if len(curr_string) == 0 or curr_string[-1] != "1":
            convertBinary(curr_string + "1")

    convertBinary("")
    return result


print(binary(3))
