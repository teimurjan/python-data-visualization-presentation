fig = plt.figure()

ax1 = fig.add_subplot(2, 1, 1)
x, h, w = 2, 7, 1
ax1.bar(x, h, w)
ax1.set_xlim(0, 10)

ax2 = fig.add_subplot(2, 1, 2)
y, w, h = 2, 7, 1
ax2.barh(y, w, h, color='red')
ax2.set_ylim(0, 10)

fig.tight_layout()
fig.show()