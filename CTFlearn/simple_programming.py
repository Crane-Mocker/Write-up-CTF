f = open("data.dat","r")

lines = f.readlines()
i = 0

for line in lines:
    num0 = line.count("0")
    num1 = line.count("1")
    
    if num0 % 3 == 0:
        i += 1
    elif num1 % 2 == 0:
        i += 1

print(i)
