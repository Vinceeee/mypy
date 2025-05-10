def test_gen():
    def add_two(a, b):
        return a + b

    def gen():
        for i in range(4):
            yield i

    _iter = gen()
    # 需要注意的是,迭代器递归是深度优先
    for i in [1, 10, 9]:
        _iter = (add_two(i, n) for n in _iter)

    assert list(_iter) == [9 * 3, 9 * 3 + 1, 9 * 3 + 2, 9 * 3 + 3]
