tips = sns.load_dataset('tips')

sns.violinplot(x="day", y="tip", data=tips, color="lightgray", inner=None)
sns.stripplot(x="day", y="tip", data=tips, jitter=True, size=3)
plt.ylabel('tip ($)')

plt.show()