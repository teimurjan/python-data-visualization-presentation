tips = sns.load_dataset('tips')

sns.violinplot(x="day", y="tip", data=tips)
plt.ylabel('tip ($)')

plt.show()