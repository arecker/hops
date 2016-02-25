from uuid import uuid4

from django.db import models


def generate_uuid_pk():
    return models.UUIDField(primary_key=True,
                            default=uuid4,
                            unique=True,
                            editable=False)
