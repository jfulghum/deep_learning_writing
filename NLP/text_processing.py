"""Count words."""

import re

def count_words(text):
    """Count how many times each unique word occurs in text."""
    counts = dict()
    for word in text.split():
        word = word.lower() 
        word = re.sub(r'[^\w\s]', '', word)
        if counts.get(word) is None:
            counts[word] = 1
        else:
            counts[word] = counts.get(word) + 1

    return counts


def test_run():
    with open("input.txt", "r") as f:
        text = f.read()
        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        
        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))
        
        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()
