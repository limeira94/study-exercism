"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    for idx , _ in enumerate(words):
        words[idx] = prefix + words[idx]
    
    return prefix + " :: " + " :: ".join(words)


def remove_suffix_ness(word):
    word = word[:-4]
    if word[-1] == "i":
        word = word[:-1] + "y"
    return word

def adjective_to_verb(sentence, index):
    phrase = sentence.replace(".", "")
    words = phrase.split(" ")
    return words[index] + "en"

if __name__ == '__main__':
    make_word_groups(["en", "sad", "angry", "jealous"])