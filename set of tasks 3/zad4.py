class AhoCorasick:
    def __init__(self):
        self.children = {}
        self.output = []
        self.fail = None


def searching(keywords):

    root = AhoCorasick()

    for keyword in keywords:
        node = root

        for char in keyword:
            node = node.children.setdefault(char, AhoCorasick())
        node.output.append(keyword)

    table = []

    for node in root.children.values():
        table.append(node)
        node.fail = root

    while table:
        current_node = table.pop(0)
        for key, next_node in current_node.children.items():
            table.append(next_node)
            fail_node = current_node.fail

            while fail_node and key not in fail_node.children:
                fail_node = fail_node.fail

            next_node.fail = fail_node.children[key] if fail_node else root
            next_node.output += next_node.fail.output

    return root


def find_in_text(text, keywords):
    root = searching(keywords)
    result = {keyword: [] for keyword in keywords}

    current_node = root
    for i, char in enumerate(text):

        while current_node and char not in current_node.children:
            current_node = current_node.fail

        if not current_node:
            current_node = root
            continue

        # Move to the next node based on current character
        current_node = current_node.children[char]
        # Record matches found at this position
        for keyword in current_node.output:
            result[keyword].append(i - len(keyword) + 1)

    return result


# przykład użycia
text1 = "eciepecie"
arr1 = ["e", "cie", "pe"]
result1 = find_in_text(text1, arr1)
print(result1)
