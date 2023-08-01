import pandas as pd

# 方法：行过滤
# 利用dataframe["列属性"]：条件语句 来筛选适合的行数据

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world["area"] >= 3000000) | (world["population"] >= 25000000)]
    return df[["name", "population", "area"]]

