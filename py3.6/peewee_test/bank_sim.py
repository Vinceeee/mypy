#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import traceback
import logging
from peewee import Model, FixedCharField, DecimalField, CharField, SqliteDatabase, SQL

logger = logging.getLogger(__name__)
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
logger.setLevel(logging.INFO)
logger.addHandler(sh)

db = SqliteDatabase("mydb-v2.db")


class InsufficentBalanceException(Exception):
    pass


class BaseModel(Model):
    class Meta:
        database = db


class Account(BaseModel):
    ac_id = FixedCharField(18, unique=True)
    ac_type = FixedCharField(3, default="SAV")
    ac_cur = FixedCharField(3, default="CNY")
    ac_balance = DecimalField(default=0.00)
    username = CharField()
    password = CharField()

    def __str__(self):
        return "{}/{}/{}/{}/{}".format(self.ac_id, self.ac_cur, self.ac_type,
                                       self.ac_balance, self.username)


    def tran(self,amount):
        """
        transfer amount from this account
        :amount: transaction amount (float , positive for credit , negatie for debit)
        :return: 0 for successful , 1 for insufficent amount , 2 for other error
        """
        try:
            with db.atomic():
                if self.ac_balance + amount < 0:
                    raise InsufficentBalanceException(u"您的余额不足")
                self.ac_balance += amount
#               logger.info("Succeessfully transfer amount {} ".format(amount))
                self.save()
        except InsufficentBalanceException as e:
            logger.warn(e)
            return 1
        except Exception:
            logger.warn(traceback.format_exc())
            return 2


def create_record():
    Account.create(
        ac_id="6222623602093528298",
        username=u"交通银行2",
        password=u'abcdefg',
    )

    for each in Account.select():
        print(each)


def gen_random_amount():
    import random
    while True:
        yield random.randrange(-9, 1900)


def multi_update():
    ac_id = "6222623602093528298"
    random_amount_generator = gen_random_amount()
#   account = Account.select().where(Account.ac_id == ac_id)
    account = Account.get(ac_id=ac_id)

    logger.info("[Before]balance for account {} is {}".format(account.ac_id ,  account.ac_balance))
    thread_lst = []
    sum = 0
    for i in range(100):
        amount = random_amount_generator.send(None)
#       print("transfer amount {} to {}".format(amount, ac_id))
#       account.tran(amount)
        sum += amount
        thread_lst.append(threading.Thread(target=account.tran,args=(amount,)))

    print("total amount : {}".format(sum))
    for t in thread_lst:
        t.start()

    for t in thread_lst:
        t.join()

    logger.info("[After]balance for account {} is {}".format(account.ac_id ,  account.ac_balance))


if __name__ == "__main__":
    db.connect()
    with db:
        db.create_tables([Account])

    multi_update()
