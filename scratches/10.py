fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
col_label = 'petal length (cm)'
is_setosa = iris_df['target_name'] == 'setosa'
col = iris_df[is_setosa][[col_label]]
data = np.hstack(col.values)
ax.set_xlabel(col_label)
ax.set_ylabel('quantity')
ax.hist(data)

fig.show()