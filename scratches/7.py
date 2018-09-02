fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
x, y = 2, 4
ax.axvline(x)
ax.axhline(y, color='darkred')
ax.set_ylim(0, 10)
ax.set_xlim(0, 10)

fig.tight_layout()
fig.show()