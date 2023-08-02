import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee[["salary"]].drop_duplicates()
    if N > len(employee):
        return pd.DataFrame({'getNthHighestSalary(2)': [None]})
    return employee.sort_values(by=['salary'], ascending=False, na_position='last').head(N).tail(1)
    
    
    