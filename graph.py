#importing the modules
from matplotlib import pyplot as plt

#saving the values of the x and y axis of both lines
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [23, 4, 12, 54, 12, 54, 65, 54, 9] #note that the length of both x and y have to be equal
x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

#plotting the points of the first line
plt.plot(x, y, c = "red", linewidth = 2, label = "Line 1", marker = "*", markerfacecolor = "black")

#plotting points of the second line
plt.plot(x2, y2, c = "blue", linewidth = 2, label = "Line 2", linestyle = "dashed",
marker = "o", markerfacecolor = "green", markersize=5)


#labelling the axes and the plot title
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Random practice graph")

#showing the legend of the 2 lines
plt.legend()

#limiting scale of the axes
plt.xlim(1, 12)
plt.ylim(1, 100)

#showing the plot
plt.show()