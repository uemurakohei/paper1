import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys
import matplotlib.colors

args = sys.argv

x_path = args[1]
y_path = args[2]
pos_length = int(args[3])


with open(x_path, 'r') as fx:
    x = fx.read().split('\n')
    print(x)
print(x.pop())

x = [int(i) for i in x] # ここでリストの中の値をint型へ変換しています。
print(x)


with open(y_path, 'r') as fy:
    y = fy.read().split('\n')
    print(y)
print(y.pop())

y = [float(i) for i in y] # ここでリストの中の値をint型へ変換しています。
print(y)

print(pos_length)

fig = plt.figure()
ax = fig.add_subplot(111)

H = ax.hist2d(x,y, bins=[np.linspace(pos_length*-1,pos_length,int(pos_length/40)),np.linspace(-2.4, -1.3, 51)]
,cmap=cm.jet)
#ax.set_title('')
#ax.set_xlabel('x')
#ax.set_ylabel('y')
fig.colorbar(H[3],ax=ax)
plt.show()

filenanme = str(pos_length) + "_img.pdf"
fig.savefig(filenanme)
