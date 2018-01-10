import re


patterns4change_and_replacements = [
    # replace quotes ''/"" to «»
    (re.compile(r'[\'\"](.*)[\'\"]', re.DOTALL), r'«\1»'),
    # text without double spaces
    (re.compile(r' {2,}'), ' '),
    # text without space in begin end
    (re.compile(r'^(\s*)|(\s*)$', re.MULTILINE), ''),
    # linking (no break space) between short words/numbers and other words
    (re.compile(r'([\d]+|[a-zA-Z]{1,2}) '), r'\1\\u00A0'),
    # replace hyphen to long dash
    (re.compile(r'() - '), r'\1 — '),
    # replace hyphen to short dash in telephone numbers
    (re.compile(r'(\)|\d+)-'), r'\1–')
]


def replace_quotes(text):
    regex = re.compile(r'[\'\"](.*)[\'\"]', re.DOTALL)
    text_with_changed_quotes = regex.sub(r'«\1»', text)
    return text_with_changed_quotes


def delete_spaces(text):
    text_without_double_spaces = re.sub(r' {2,}', r' ', text)
    regex = re.compile(r'^(\s*)|(\s*)$', re.MULTILINE)
    text_without_space_in_begin_end = regex.sub('', text_without_double_spaces)
    return text_without_space_in_begin_end


def hyphen2dash(text):
    return re.sub(r'(\)|\d+) *- *|() - ', r'\1', text)


def space2no_break_space(text):
    return re.sub(r'([\d]+|[a-zA-Z]{1,2}|) ', r'\1\\u00A0', text)


def handle_text(text):
    for pattern, replacement in patterns4change_and_replacements:
        text = pattern.sub(replacement, text)
    return text
