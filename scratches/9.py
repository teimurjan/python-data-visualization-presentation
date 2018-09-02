days = [1, 2, 3, 4, 5]

sleeping = [5, 6, 4, 5, 5]
eating =   [3, 5, 4, 2, 3]
working =  [16, 13, 16, 17, 16]

labels = ['sleeping', 'eating', 'working']

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
ax.stackplot(days, sleeping, eating, working)
ax.set_title('A typical software engineer\'s working week.')
ax.legend(labels, loc='upper left')

fig.show()