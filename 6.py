fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x1, y1 = [1, 2, 3, 4], [5, 7, 9, 11]
ax.plot(x1, y1, c="darkblue", linestyle="--")

ax.set_xlabel('I am xlabel')
ax.set_ylabel('I am ylabel')
ax.set_title('I am title')
ax.legend(
    ['Straight line with some meaning'], 
    loc="upper center"
)
ax.set_xticks(x1)
ax.set_yticks(y1)

fig.tight_layout()
fig.savefig('3.png', transparent=True)