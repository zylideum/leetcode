def isValid(s: str) -> bool:
    symbolMap = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    pairs = []

    for symbol in s:
        if symbol in symbolMap:
            pairs.append(symbol)
        elif pairs and symbol == symbolMap[pairs[-1]]:
            pairs.pop()
        else:
            return False
    if pairs:
        return False
    return True

print(isValid("(())"))
        