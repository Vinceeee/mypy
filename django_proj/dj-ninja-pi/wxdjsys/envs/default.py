# 默认配置
import os
from enum import Enum

DEBUG = True

class EnvEnum(Enum):
    UT = "ut"
    DEV = "dev"
    STAGE = "stage"
    PROD = "prod"



run_env = os.environ.get("RUN_ENV", "dev")

env = EnvEnum(run_env)

if env == EnvEnum.DEV:
    from .dev import * # noqa
elif env == EnvEnum.UT:
    from .ut import * # noqa
else:
    from .dev import * # noqa
