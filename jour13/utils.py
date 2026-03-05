import re


def highlight(text, pattern):

    regex = re.compile(pattern, re.IGNORECASE)

    return regex.sub(lambda m: f"\033[92m{m.group(0)}\033[0m", text)


def snippet(text, match, window=70):

    start = max(match.start() - window, 0)

    end = min(match.end() + window, len(text))

    snippet = text[start:end]

    return snippet.replace("\n", " ")