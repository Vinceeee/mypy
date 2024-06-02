from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Role(BaseModel):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=1024)
    props = models.JSONField(verbose_name="角色描述")
