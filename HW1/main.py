import random
import time
import os
#-------------------------------------------------------------------------------
def generate_part_of_a_number(size, base):
    test = range(0, base)

    B = [str(e) for e in test]


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

def generate_all_of_number(size_n, size_m, base):

    numbers_n = generate_part_of_a_number(size_n + 1, base)

    numbers_m = generate_part_of_a_number(size_m, base)

    numbers = []

    for element_n in numbers_n:
        for element_m in numbers_m:
            test = element_n + "/" + element_m 
            numbers.append(test)

    
    return numbers
    
#-------------------------------------------------------------------------------

def Computing_main(size_n, size_m, base):
    dict_test = {} 
    all_number = generate_all_of_number(size_n , size_m, base)

    for element in all_number:
        two_number = element.split("/")

        value = Computing_sub(two_number[0], 2) + Computing_sub(two_number[1], 0.5)
        test_dic = {element : value}
        dict_test.update(test_dic)
    count = 1
    for key, value in dict_test.items():
        print(f"{count} --> number is +-{key} and value is {value}")   
        print("-----------------------------------------------------------------------")
        time.sleep(1)
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

def main():

    base = int(input("please entered a Base : "))
    n = int(input("entered a N : "))

    m = int(input("entered a M : "))

    print(f"F(base, m , n) ----> F({base} , {m} , {n})")

    time.sleep(2)

    Computing_main(n, m, base)


#--------------------------------------------------------------------------------

main()
    
        

    







