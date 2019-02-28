import logging
from hashlib import sha256
from django.db import models

logger = logging.getLogger("django")


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=200, null=False, unique=True)
    user_passwd = models.CharField(max_length=255, null=False)
    user_crediential = models.CharField(max_length=128)
    user_regtime = models.DateTimeField(auto_now=True)

    @staticmethod
    def auth() -> bool:
        """auth a user and grant token
        :returns: result
        """
        res = False
        return res

    def save(self, *args, **kwargs):
        self.user_passwd = User.hashing(self.user_name, self.user_passwd)
        super().save(*args, **kwargs)

    @staticmethod
    def hashing(user_name, user_passwd):
        logger.info("get hashing ...")
        s256 = sha256()
        s256.update(str(user_name).encode('utf8'))
        s256.update(str(user_passwd).encode('utf8'))
        return s256.hexdigest()
