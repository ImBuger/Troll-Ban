def disemvowel(string_):
    vowels = ['a','e','i','u','o','A','E','I','O','U']
    chars = list(string_)
    print(chars)
    for i in vowels:
        for j in chars:
            if i == j:
                chars.remove(j)


    newString = "".join(chars)
    print(newString)
    return string_

disemvowel("No offense but,Your writing is among the worst I've ever read")