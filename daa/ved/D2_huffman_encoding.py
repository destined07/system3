def make_tree(text):
    frequency = {}

    for ch in text:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    # Each node is [frequency, tree].
    # A leaf tree is a character; an internal tree is a pair of child trees.
    nodes = [[frequency[ch], ch] for ch in frequency]

    while len(nodes) > 1:
        nodes.sort(key=lambda item: item[0])

        left = nodes.pop(0)
        right = nodes.pop(0)

        new_node = [left[0] + right[0], (left[1], right[1])]
        nodes.append(new_node)

    return nodes[0][1]


def create_codes(tree, code, codes):
    if isinstance(tree, str):
        # Give a single unique character the code "0".
        codes[tree] = code if code != "" else "0"
    else:
        create_codes(tree[0], code + "0", codes)
        create_codes(tree[1], code + "1", codes)


text = input("Enter text to encode: ")

if text == "":
    print("Please enter some text.")
else:
    tree = make_tree(text)
    codes = {}
    create_codes(tree, "", codes)

    print("\nHuffman Codes:")
    for ch in codes:
        print(repr(ch), ":", codes[ch])

    encoded_text = ""
    for ch in text:
        encoded_text += codes[ch]

    print("\nEncoded Text:", encoded_text)
