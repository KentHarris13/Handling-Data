cupcake = open("Cupcakeinvoices.csv")

total = 0
for line in cupcake:
    # print(line)

    line = line.rstrip('\n').split(',')
    print(line[2])
    line[3]= int(line[3])
    line[4] = float(line[4])
    line.append(line[3]*line[4])
    print(line)
    total += line[5]
total = "{:.2f}".format(total)
print(total)

cupcake.close()

import matplotlib.pyplot as plt

data = [23, 45, 56, 78, 213]
plt.bar([1,2,3,4,5], data)
plt.show()
