x1, y1 = [1, 2, 3, 4], [10, 20, 30, 40]
x2, y2 = [2, 3, 4, 5], [10, 20, 30, 40]

# Using matplotlib instances
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x1, y1)
ax.scatter(x2, y2, color='red')
ax.set_xlim(0, 5.5)
plt.show()

# Using matplotlib.pyplot functions
plt.plot(x1, y1)
plt.scatter(x2, y2, color='red')
plt.xlim(0, 5.5)
plt.show()