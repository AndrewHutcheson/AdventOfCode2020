#####part one#####
stream = open("Input.txt")
lines = stream.readlines()

def is_password_valid(minimum,maximum,requirement,password):
    count = 0
    for i in password: 
        if i == requirement: 
            count = count + 1

    #print(f"minimum {minimum} maximum {maximum} count {count} password {password} requirement is {requirement}")
    if ((count <= maximum) and (count >= minimum)):
        return True
    else:
        return False

count = 0
for line in lines:
    #parse the info
    position = line.index(':')
    policy = line[0:position]
    position2 = policy.index('-')
    position3 = policy.index(' ')
    minimum = line[0:position2]
    maximum = line[position2+1:position3]
    requirement = line[position3+1:position]
    password = line[position+2:].rstrip()
    #print(f"minimum {minimum} maximum {maximum} requirement {requirement} password {password}")
    #print(is_password_valid(int(minimum),int(maximum),requirement,password))
    
    if(is_password_valid(int(minimum),int(maximum),requirement,password)):
        count = count+1

print(count)

#####part two#####
def is_password_valid2(position1,position2,requirement,password):
    #indexing by definition for the problem starts at one, not zero
    requirements_met = 0
    #check first position
    if(password[position1-1] == requirement):
        requirements_met = requirements_met +1
    if(password[position2-1] == requirement):
        requirements_met = requirements_met +1
    if(requirements_met == 1):
        return True
    else:
        return False

count = 0
for line in lines:
    #parse the info
    position = line.index(':')
    policy = line[0:position]
    position2 = policy.index('-')
    position3 = policy.index(' ')
    minimum = line[0:position2]
    maximum = line[position2+1:position3]
    requirement = line[position3+1:position]
    password = line[position+2:].rstrip()

    if(is_password_valid2(int(minimum),int(maximum),requirement,password)):
        count = count+1

print(count)