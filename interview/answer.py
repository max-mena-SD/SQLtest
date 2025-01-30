# import numpy as np
import pandas as pd

# [score, name, years]
employees = [
    [1.3, "Xavier", "3.5"],
    [0.23, "Juan", "1"],
    [12.3, "Pedro", "2"],
    [4.0, "Percy", "9"],
    [11.03, "Roberto", "6"],
    [2.6, "Bryan", "0.333"],
    [2.89, "Adolfo", "10"],
]


def employees_name_filtered_by_year(employees, year):
    df = pd.DataFrame(employees, columns=["score", "name", "years"])
    df["years"] = pd.to_numeric(df["years"])

    year_filtered = df[df["years"] > year]
    result = year_filtered["name"].to_list()

    return result


# Exercise

# 1. Print employee names with more than 3 years in the company.
print(employees_name_filtered_by_year(employees, 3))
