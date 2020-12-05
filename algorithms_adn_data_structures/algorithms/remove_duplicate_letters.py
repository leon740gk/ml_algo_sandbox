# https://www.youtube.com/watch?v=2ayws5Y-WM4&list=PLr9zbByiJa3Ua2AgTrdvot6AQ3b4CxWrF&index=41

def remove_duplicate_letters(s: str) -> str:
    result = []
    index_dict = {char: index for char, index in enumerate(s)}
    for index, char in enumerate(s):
        if char not in result:
            while result and index < index_dict[result[-1]] and char < result[-1]:
                result.pop()
            result.append(char)

    return "".join(result)
