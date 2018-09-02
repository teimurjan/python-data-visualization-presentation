tips = sns.load_dataset('tips')

sns.stripplot(x="day", y="tip", data=tips, jitter=True, size=2)
plt.ylabel('tip ($)')

plt.show()