import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = np.where((df['weight'] / ((df['height'] / 100) ** 2)) > 25, 1, 0)

# 3
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0) 

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars='cardio', value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7
    plot = sns.catplot(data=df_cat, x='variable', y='total', hue='value', kind='bar', col='cardio')


    # 8
    fig = plot.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()
    corr = corr.round(1)
    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))


    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, mask=mask, annot=True, annot_kws={"size":5}, fmt=".1f", center=0, vmax=0.32, vmin=-0.16, cbar_kws={"ticks":[0.24, 0.16, 0.08, 0, -0.08]}, ax=ax)


    # 16
    fig.savefig('heatmap.png')
    return fig
