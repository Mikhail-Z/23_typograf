import re

non_breaking_space = '\u00A0'


patterns4change_and_replacements = [
    # replace quotes ''/"" to «»
    (re.compile(r'[\'\"](.*)[\'\"]', re.DOTALL), r'«\1»'),
    # text without double spaces
    (re.compile(r' {2,}'), ' '),
    # text without space in begin end
    (re.compile(r'^(\s*)|(\s*)$', re.MULTILINE), ''),
    # linking (no break space) between short words/numbers and other words
    (re.compile(r'((^|\s|\b)(\d+|[a-zA-Za-яА-Я]{1,2})) '),
     r'\1{}'.format(non_breaking_space)),
    # replace hyphen to long dash
    (re.compile(r' - '), r' — '),
    # replace hyphen to short dash in telephone numbers
    (re.compile(r'(\)|\d+)-'), r'\1–')
]


def handle_text(text):
    for pattern, replacement in patterns4change_and_replacements:
        text = pattern.sub(replacement, text)
    return text
