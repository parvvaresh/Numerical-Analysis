import random
#-------------------------------------------------------
def build_num(base, k, lower, upper):
    test = range(0, base)
    number = [str(element) for element in test]
    
    test = range(lower, upper + 1)
    
    e = [str(element) for element in test]
    
    del test
    
    
    
    
    result = [] #for save the number
    
    while True:
        temp_num = ""
        for repeat in range(0, k):
            temp_num += random.choice(number)
        
        E = random.choice(e)
        
        temp_num = "0." + temp_num + " * " + str(base)+ (" ^ ") + E
        
        if (temp_num[2] != "0" and (temp_num not in result)):
            result.append(temp_num)
        
        if len(result) == (base - 1) * (upper - lower + 1) * (base ** (k - 1)):
            break
    
    return result

#-------------------------------------------------------
def calculate(number, base):
    sum = 0
    power = 1
    for e in number:
        sum += int(e) * ((1 / base) ** power) 
        power += 1 
    return sum      

#-------------------------------------------------------
def value(temp, base):
    for element in temp:
        number = element[2: element.index("*") - 1]
        #print(number)
        value = calculate(number, base)
        #print(value)
        power = int(element[-1])
        
        #print(value * (base ** power))
        value = value * float((base ** power))
        
        print(f"this number --> {element} and value --> {value}")
        
        

#-------------------------------------------------------
def main():
    base = int(input("Base : "))
    K = int(input("K : "))
    L = int(input("L : "))
    U = int(input("U : "))
    
    print(f"F(B, K , L , U) ---> F({base}, {K}, {L}, {U})")
    
    result = build_num(base, K, L, U)
    
    value(result, base)
    
#-------------------------------------------------------

main()