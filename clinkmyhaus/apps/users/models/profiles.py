"""Profile model."""

# Django
from django.db import models

# Utilities
from clinkmyhaus.apps.utils.models import CHouseModel


class Profile(CHouseModel):
    """Profile model.
    A profile holds a user's public data like biography, picture,
    and statistics.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
