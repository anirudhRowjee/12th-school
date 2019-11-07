from matplotlib import pyplot as plt
import numpy as np

a = [30, 40, 50, 34]
b = [8,9,10,11]
clr = ['red', 'blue', 'green', 'yellow']
ex = [0,0,0,1]

plt.pie(a, labels=b, colors=clr, autopct='%3d%%', explode=ex)
plt.title("Class")

plt.savefig('something.pdf')

plt.show()
