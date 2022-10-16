import random
import time
import os
import matplotlib.pyplot as plt
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

        value = Computing_sub(two_number[0], base) + Computing_sub(two_number[1], 1 / base)
        #value = 0 + Computing_sub(two_number[1], 0.5)
        test_dic = {element : value}
        dict_test.update(test_dic) 
        dict(sorted(dict_test.items(), key=lambda item: item[1]))

    count = 1
    for key, value in dict_test.items():
        print(f"{count} --> number is +-{key} and value is +-{value}")   
        print("-----------------------------------------------------------------------")
        time.sleep(1)
        count += 1   
    #this is a details     
    time.sleep(2)
    print(f"all of number is {base ** (size_n + size_m + 1)}")
    time.sleep(1)
    print(f"all of value is {2 *(base ** (size_n + size_m + 1)) - 1}")
    time.sleep(1)
    print(f"maximom of value is {(base ** (size_n + 1)) - (base ** (-size_m))}")
    time.sleep(1)
    print(f"minimom of value is {base ** -size_m}")

    return dict_test

#-------------------------------------------------------------------------------- 

def Computing_sub(num, temp):
    result = 0
    while True:

        number = float(num[0])
        if temp == 0.5:
            result += (number) *  (temp ** (len(num)))
        if temp == 2:
            result += (number) *  (temp ** (len(num) - 1))


        num = num[1 : : ]

        if len(num) == 0:
            return result
            break

#------------------------------------------------------------------

def plotting(dic_test):
    list_of_value = []
    Y = []
    for key, value in dic_test.items():
        list_of_value.append(value)
        list_of_value.append(-value)

        Y.append(0)
        Y.append(0)

    
    


    plt.scatter(list_of_value, Y)
    plt.show()
#-------------------------------------------------------------------------------

def main():

    base = int(input("please entered a Base : "))

    n = int(input("entered a N : "))

    m = int(input("entered a M : "))

    print(f"F(base, m , n) ----> F({base} , {m} , {n})")

    time.sleep(2)

    fainal = Computing_main(n, m, base)

    user = input("Would you like to see the chart ? [Y/N] ")

    if user.upper() == "Y":
        plotting(fainal)
        
    elif user.upper() == "N":
        print("good bye :))") 


#--------------------------------------------------------------------------------

main()
    







