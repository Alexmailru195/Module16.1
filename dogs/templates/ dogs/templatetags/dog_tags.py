from django import template

register = template.Library()

@register.simple_tag
def breed_name(dog):
    return dog.breed.name
