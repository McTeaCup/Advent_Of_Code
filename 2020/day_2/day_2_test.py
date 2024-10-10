import day_2_main as main

# TESTS
def test_check_policy():
    assert main.check_password_corruption("""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".splitlines()) == 2

def test_check_new_password_corruption():
    assert main.check_new_password_corruption("""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".splitlines()) == 1