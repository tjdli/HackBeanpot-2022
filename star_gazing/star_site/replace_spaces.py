from django import template

register = template.Library()

@register.filter(name='replace_space')
def replace_space(value):
    """
    Returns the value turned into a list.
  """
    return "https://www.google.com/maps/embed/v1/place?key=AIzaSyDV6nqMJ7_iY1nU3reiUDrltej_Laf5BCw &q=" + value.replace(" ", "+")
