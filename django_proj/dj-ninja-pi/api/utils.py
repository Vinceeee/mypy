def sorted_by_key(arr: list[dict], key:str):
    """ update d2 to d1
    """
    arr.sort(key=lambda x:x[key])
