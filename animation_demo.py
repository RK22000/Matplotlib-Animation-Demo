import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.animation as anime
import pandas as pd
import numpy as np

def main():
    df = pd.read_csv('data/WPP2022_Demographic_Indicators_Medium.csv')
    df2 = df.loc[df.LocTypeName=='Country/Area']
    fig, ax = plt.subplots()
    def topPopulations(year, present_year):
        n=10
        ax.clear()
        ax.set_title(f'{"Prediction: " if present_year < year else ""}{year}')
        sns.barplot(ax=ax, data=df2.loc[df2.Time==year, ['TPopulation1Jan','Location']].sort_values(by='TPopulation1Jan', ascending=False).iloc[:n], x='TPopulation1Jan', y='Location')
        fig.tight_layout()

    ani = anime.FuncAnimation(
        fig=fig,
        func=topPopulations,
        frames=df2.Time.unique(),
        fargs=(2023,)
    )
    plt.show()

if __name__=='__main__':
    main()