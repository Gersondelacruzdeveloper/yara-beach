# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def truncate_from_to(value, args):
    """
    Truncates the text starting from a specific word index and ends at a specified word count.
    Usage: {{ post.content|truncate_from_to:"10,20" }}
    """
    try:
        start, length = map(int, args.split(','))
        words = value.split()
        return ' '.join(words[start:start+length]) + '...'
    except (ValueError, TypeError):
        return value  # If there’s an error, return the original value


# myapp/templatetags/truncate_filters.py

# from django import template

# register = template.Library()

# @register.filter(name='truncate_from_to')
# def truncate_from_to(value, arg):
#     """Extracts a substring from index 'start' to 'end'."""
#     try:
#         start, end = map(int, arg.split(','))
#         return value[start:end]
#     except (ValueError, TypeError):
#         return value  # return the original value if something goes wrong
