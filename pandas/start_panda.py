import pandas as pd

# df = pd.read_csv("C:\\Users\\PoojashreeMC\\Documents\\Python\\learn_pandas\\orders.csv")
# df = pd.read_csv("C:\\Users\\PoojashreeMC\\Documents\\Python\\learn_pandas\\annual_enterprise.csv")

# print(df)

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Country': ['USA', 'Canada', 'UK']
}

df = pd.DataFrame(data)
print(df)