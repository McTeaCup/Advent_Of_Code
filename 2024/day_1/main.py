def get_abs(input_1:int, input_2:int):
    """
    Takes two integers, subtract them and returns the absolute value
    """
    return abs(input_1 - input_2)

def get_data():
    with open('data', 'r') as file:
        left_list = []
        right_list = []

        line: str
        for line in file.readlines():
            left_list.append(int(line.split('   ')[0]))
            right_list.append(int(line.split('   ')[1].replace('\n', '')))

    return [sorted(left_list), sorted(right_list)]


def answer_part_1(right_list, left_list):
    total_value = 0
    
    for line in range(1000):
        total_value += get_abs(right_list[line], left_list[line])
    
    return total_value


def answer_part_2(right_list, left_list):
    total_count = 0
    
    for number in left_list:
        
        instance_count =  right_list.count(number)
        total_count += instance_count * number
    
    return total_count

print(f'Part 1: {answer_part_1(get_data()[0], get_data()[1])}')
print(f'Part 2: {answer_part_2(get_data()[0], get_data()[1])}')