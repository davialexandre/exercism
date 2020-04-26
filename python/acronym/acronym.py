import re


def abbreviate(words):
    cleaned_words = re.findall(r'[a-zA-Z0-9]+\'?[a-zA-Z0-9]|[a-zA-Z0-9]', words)
    initials = [word[0].upper() for word in cleaned_words]

    return ''.join(initials)
