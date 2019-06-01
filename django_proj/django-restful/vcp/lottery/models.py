from django.db import models


class Candidate(models.Model):
    c_id = models.IntegerField(primary_key=True, editable=False)
    c_name = models.CharField(max_length=200, null=False)
    c_description = models.CharField(max_length=200, default="")


class Price(models.Model):
    p_id = models.IntegerField(primary_key=True, editable=False)
    p_name = models.CharField(max_length=200, null=False)
    p_level = models.IntegerField(default=5)
    p_pic = models.FileField(upload_to='media/')
    p_istaken = models.IntegerField(default=0)


class Winner(models.Model):
    POLICY_UNIQUE = 0
    POLICY_NOUNIQUE = 1

    w_id = models.IntegerField(primary_key=True, auto_created=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    policy = models.IntegerField(default=POLICY_UNIQUE)

    def save(self, *args, **kwargs):
        if self.policy == 0:
            pass
        super(Winner, self).save(*args, **kwargs)
