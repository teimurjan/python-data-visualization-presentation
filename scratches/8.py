labels = ['sleeping', 'eating', 'working']
sleeping = 5
eating =   3
working =  16

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
ax.pie([sleeping, eating, working])
ax.set_title('A typical software engineer\'s working day.')
ax.legend(labels, loc='upper left')
ax.set_aspect(1)

fig.show()