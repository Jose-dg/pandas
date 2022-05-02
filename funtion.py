import pandas as pd

dates=['April-10', 'April-11', 'April-12', 'April-13']
fruits=['Apple', 'Papaya', 'Banana', 'Mango']
prices=[3, 1, 2, 4]

df = pd.DataFrame({'Date':dates ,
                   'Fruit':fruits ,
                   'Price': prices})

new_df=df.assign(Profit=6)
print(new_df)