tips = sns.load_dataset('tips')

sns.stripplot(x="day", y="tip", data=tips, jitter=False)
plt.ylabel('tip ($)')

plt.show()