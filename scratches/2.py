INITIAL_X, INITIAL_Y = 0, 0
WIDTH, HEIGHT = 1, 1

fig = plt.figure()
ax = fig.add_axes((INITIAL_X, INITIAL_Y, WIDTH, HEIGHT))
ax.plot([1, 2], [3, 4])
fig.show()