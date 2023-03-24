from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        return value
    excluded_words = ['сука', 'блять', 'жопа']
    for word in excluded_words:
        value = value.replace(word, '*' * len(word))
    return value

