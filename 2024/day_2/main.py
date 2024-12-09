def load_data():
    with open('data', 'r') as file:
       
        total_line = []
        for line in file.readlines():
            number_line = line.split(' ')
            temp_line = []
            
            for number in number_line:
                temp_line.append(int(number))
        
            total_line.append(temp_line)

    return total_line 

def is_safe(input_list:list[int]):
    index = 0

    for _ in input_list:
        if(index > len(input_list)): #If index is bigger than list, leave foor loop
            break
        
        elif(input_list[index] > input_list[index + 1]): #If previous index has a higher value: unsafe 
            print(f'decreese {input_list}')
            return 0
        
        elif(input_list[index] - input_list[index + 1] == 0):
            print(f'is zero {input_list}')
            return 0

        elif(input_list[index] - input_list[index + 1] > 3) :
            print(f'bigger than 3 {input_list}')
            return 0
        
    return 1
            
    

def part_1():
    data = load_data()
    value = 0
    for line in data:
        value += is_safe(line)
    
    return value
            
print(part_1())