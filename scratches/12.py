tips = sns.load_dataset('tips')
sns.relplot(x="total_bill", y="tip", data=tips, hue="day", col="time")
plt.show()