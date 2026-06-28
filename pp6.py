import pandas as pd
    
data={
    "name": ["ram", "raj", "shayam",None],
    "age": [23,34,19,None],
    "salary": [12000,18000,34000,None],
    "score": [89,None,69,None]
}
df = pd.DataFrame(data)

# df.drop(columns= ["score"], inplace= True)
print(df.isnull())
print(df.isnull().sum())