def largestTimeFromDigits(arr: list[int]) -> str:
    ans = ["0", "0", ":", "0", "0"]
    h = 0
    for i in arr:
        if i > h and i < 3:
            h = i
    arr.remove(h)
    h2 = 0
    for i in arr:
        if i > h2 and i <= 9:
            h2 = i
    arr.remove(h2)
    m = 0
    for i in arr:
        if i > m and i < 3:
            m = i
    arr.remove(m)
    m2 = 0
    for i in arr:
        if i > m2 and i <= 9:
            m2 = i
    arr.remove(m2)
    ans[0] = str(h)
    ans[1] = str(h2)
    ans[3] = str(m)
    ans[4] = str(m2)


def test_latest_time():
    # Example test cases

    assert largestTimeFromDigits([1, 2, 3, 4]) == "23:41"
    assert largestTimeFromDigits([5, 5, 5, 5]) == ""

    # Additional test cases
    assert largestTimeFromDigits([0, 0, 0, 0]) == "00:00"
    assert largestTimeFromDigits([0, 0, 1, 0]) == "10:00"
    assert largestTimeFromDigits([0, 1, 0, 0]) == "10:00"
    assert largestTimeFromDigits([1, 0, 0, 0]) == "10:00"
    assert largestTimeFromDigits([9, 9, 9, 9]) == ""
    assert largestTimeFromDigits([0, 0, 1, 2]) == "20:10"
    assert largestTimeFromDigits([9, 5, 2, 1]) == "19:52"
    assert largestTimeFromDigits([2, 4, 5, 9]) == "23:59"
    assert largestTimeFromDigits([1, 9, 9, 9]) == "19:59"

    print("All test cases pass")


print(largestTimeFromDigits([1, 2, 3, 4]))

test_latest_time()
