import pandas as pd
data = [
    [999,
     'Switzerland'],
    [113,
     'Switzerland'],
    [112,
     'Japan'],
    [112,
     'Switzerland'],
    [113,
     'Canada'],
    [114,
     'Japan'],
    [100,
     'Germany'],
    [114,
     'Japan'],
    [115,
     'Germany']
]

df = pd.DataFrame(data, columns=["code","Countries"])
print(df)