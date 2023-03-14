from django import template

register = template.Library()

@register.filter()
def censor(text):

    BAD_WORDS = ['отказ', 'что', 'жизель', 'маррей']

    if not isinstance(text, str):
        raise TypeError(f'{type(text)} Не является строкой!')

    for b_word in text.split():
        if b_word.lower() in BAD_WORDS:
            text = text.replace(b_word, f'{b_word[0]}{"*" *(len(b_word)-1)}')
    return text

from django import template

register = template.Library()

@register.filter()
def censor(text):

    BAD_WORDS = ['отказ', 'что', 'жизель', 'маррей']

    if not isinstance(text, str):
        raise TypeError(f'{type(text)} Не является строкой!')

    for b_word in text.split():
        if b_word.lower() in BAD_WORDS:
            text = text.replace(b_word, f'{b_word[0]}{"*" *(len(b_word)-1)}')
    return text

