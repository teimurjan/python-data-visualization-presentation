tips = sns.load_dataset('tips')

sns.swarmplot(x="day", y="tip", data=tips, hue="sex")
plt.ylabel('tip ($)')

plt.show()