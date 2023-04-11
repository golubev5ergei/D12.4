from django import template
from . import custom_filters


register = template.Library()
register.filter('exclude_words', custom_filters.censor)