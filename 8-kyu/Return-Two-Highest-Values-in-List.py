# test.assert_equals(two_highest([15, 20, 20, 17]), [20, 17])

def two_highest(arg1):
    return sorted(set(arg1), reverse=True)[:2]
