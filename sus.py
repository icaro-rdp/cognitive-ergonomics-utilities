import pandas as pd

pd = pd.read_csv('sus.csv')


def calculateSusYear(year):
    pd_year = pd['Year'] == year
    pd_year_sus = pd[pd_year].iloc[:, 2:12]
    pd_year_sus_odd = pd_year_sus.iloc[:, 0::2].sum(axis=1) -5 
    pd_year_sus_even = 25 - pd_year_sus.iloc[:, 1::2].sum(axis=1)
    pd_year_sus_total = (pd_year_sus_odd + pd_year_sus_even) * 2.5
    return {'Year': year, 'SUS': pd_year_sus_total.mean(), 'SD': pd_year_sus_total.std().round(2)}


def calculateUmUx(year):
    pd_year = pd['Year'] == year
    pd_year_sus = pd[pd_year].iloc[:, 13:15]
    um_ux_lite_score = pd_year_sus.apply(lambda x:x-1).sum(axis=1) / 12 * 100
    um_ux_lite_to_sus = 0.65 * um_ux_lite_score + 22.9
    return {'Year': year, 'UM_UX': um_ux_lite_score.mean().round(2), "SUS": um_ux_lite_to_sus.mean().round(2)}


print(calculateUmUx(2024))
print(calculateSusYear(2024))
