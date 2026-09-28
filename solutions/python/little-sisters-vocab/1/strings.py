"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.
        str: Root word prepended with 'un'.
    """
    return 'un' +word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words.
    Returns:
        str: Prefix followed by vocabulary words with prefix applied.
    """
    separator = (" :: ")+str(vocab_words[0])
    vocab_words = separator.join(vocab_words)
    return vocab_words


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.
    Returns:
        str: Word with suffix removed & spelling adjusted.
    """

    if word.endswith("iness"):
        return word[:-5] + "y"
    return word.removesuffix("ness")


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.
    """
    return sentence.split()[index].strip(".")+'en'