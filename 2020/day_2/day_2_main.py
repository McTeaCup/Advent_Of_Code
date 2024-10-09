# TESTS
def test_check_policy():
    assert check_password_corruption("""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".splitlines()) == 2

def test_check_new_password_corruption():
    assert check_new_password_corruption("""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".splitlines()) == 1

def check_password_corruption(password_list):
    valid_password_count = 0

    for entry in password_list:
        split_entry = entry.split(" ")
        f_entry = {
            'least_count'   : int(split_entry[0].split('-')[0]),
            'most_count'    : int(split_entry[0].split('-')[-1]),
            'letter'        : split_entry[1].replace(':', ''),
            'password'      : split_entry[2].replace('\n', '')
        }
        letter_count = f_entry['password'].count(f_entry['letter'])

        if(letter_count >= f_entry['least_count'] and letter_count <= f_entry['most_count']):
            valid_password_count = valid_password_count + 1
    
    return valid_password_count

def check_new_password_corruption(password_list):
    valid_password_count = 0

    for entry in password_list:
        split_entry = entry.split(" ")
        f_entry = {
            'expected_index'      : int(split_entry[0].split('-')[0]) - 1,
            'not_expected_index'  : int(split_entry[0].split('-')[1]) - 1,
            'letter'            : split_entry[1].replace(':', ''),
            'password'          : split_entry[2].replace('\n', '')
        }
        expected_index = f_entry['expected_index']
        not_expected_index = f_entry['not_expected_index']
        
        if(f_entry['password'][expected_index] == f_entry['letter']
        and f_entry['password'][not_expected_index] != f_entry['letter']):
            valid_password_count = valid_password_count + 1

        elif(f_entry['password'][expected_index] != f_entry['letter']
        and f_entry['password'][not_expected_index] == f_entry['letter']):
            valid_password_count = valid_password_count + 1
    
    return valid_password_count

if __name__ == '__main__': 
    with open('password_data') as file:
        data = file.readlines()
    print(f'Valid password with old policy: {check_password_corruption(data)}')
    print(f'Valid password with new policy: {check_new_password_corruption(data)}')