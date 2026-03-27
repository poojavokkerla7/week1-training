def group_anagrams(words):
    result = {}

    for word in words:
        key = ''.join(sorted(word))

        if key not in result:
            result[key] = []

        result[key].append(word)

    return list(result.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
