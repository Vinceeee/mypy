def joseph_ring(size: int, n: int) -> int:
    """
    Joseph Problem Destription
    People are standing in a circle waiting to be executed. Counting begins at a
    specified point in the circle and proceeds around the circle in a specified
    direction. After a specified number of people are skipped, the next person is
    executed. The procedure is repeated with the remaining people, starting with
    the next person, going in the same direction and skipping the same number of
    people, until only one person remains, and is freed.
    模拟法
    """
    q1 = [0] * size
    last_one = -1
    dropped = 0
    idx = 0
    countdown = n
    while dropped < size:
        if idx == size:
            idx = 0
        if q1[idx] == 0:
            countdown -= 1
            if countdown == 0:
                q1[idx] = 1
                last_one = idx
                countdown = n
                dropped += 1
                print(f"number : {idx+1} died in the {dropped} cycle")
        idx += 1

    return last_one


def joseph_ring_v2(size: int, n: int) -> int:
    """递推法"""
    p = 0
    for i in range(2, size + 1):
        p = (p + n) % i
    return p


def test_joseph_ring():
    the_one = joseph_ring(11, 3)
    assert the_one == 6
    assert the_one == joseph_ring_v2(11, 3)
    print(f"the one who left in the end is number: {the_one+1}")


test_joseph_ring()

