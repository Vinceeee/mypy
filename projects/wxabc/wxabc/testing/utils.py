"""通用的测试工具方法"""

import importlib.util


def is_module_exist(package: str) -> bool:
    return importlib.util.find_spec(package) is not None
