import random
#-------------------------------------------------------------------------------
def generate_part_of_a_number(size):
    B = ["0", "1"]

    numbers = [] 
    while True:
        temp = ""

        for repeat in range(0, size):
            temp += random.choice(B)


        if temp not in numbers:
            numbers.append(temp)
        

        if len(numbers) == 2 ** size:
            return numbers
            break
            
#--------------------------------------------------------------------------------

def generate_all_of_number(size_n, size_m):

    numbers_n = generate_part_of_a_number(size_n + 1)

    numbers_m = generate_part_of_a_number(size_m)

    numbers = []

    for element_n in numbers_n:
        for element_m in numbers_m:
            test = element_n + "/" + element_m 
            numbers.append(test)

    
    return numbers
    
#-------------------------------------------------------------------------------

def Computing_main(size_n, size_m):
    dict_test = {} 
    all_number = generate_all_of_number(size_n , size_m)

    for element in all_number:
        two_number = element.split("/")

        value = Computing_sub(two_number[0], 2) + Computing_sub(two_number[1], 0.5)
        test_dic = {element : value}
        dict_test.update(test_dic)
    count = 1
    for key, value in dict_test.items():
        print(f"{count} --> number is {key} and value is {value}")   
        count += 1   

#-------------------------------------------------------------------------------- 

def Computing_sub(num, temp):
    result = 0
    while True:
        result += float(num[0]) *  (temp ** (len(num) - 1))
        num = num[1 : : ]

        if len(num) == 0:
            return result
            break

#-------------------------------------------------------------------------------


n = int(input("entered a N : "))

m = int(input("entered a M : "))

Computing_main(n, m)


#--------------------------------------------------------------------------------
    
        

    



