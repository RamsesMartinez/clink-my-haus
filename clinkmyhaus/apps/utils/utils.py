import random

from django.utils.text import slugify


def random_pic(a: int, b: int):
    random_num = str(random.randint(a, b))
    if len(random_num) < 2:
        return '0%s' % random_num
    return random_num


def unique_slug_generator(model_instance, title, slug_field):
    """
    Slug generator.

    :param model_instance:
    :param title:
    :param slug_field:
    :return:
    """
    slug = slugify(title)
    model_class = model_instance.__class__

    while model_class ._default_manager.filter(slug=slug).exists():
        object_pk = model_class._default_manager.latest('pk').pk
        object_pk = object_pk + 1
        slug = '{}-{}'.format(slug, object_pk)
    return slug
