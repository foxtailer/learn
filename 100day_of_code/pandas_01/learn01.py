import pandas as pd

user_data  = pd.read_csv(r'E:\GIT\learn\100day_of_code\pandas_01\Simada.csv')

data = {
    'Name': ['Hardik', 'Pollard', 'Bravo'],
    'Run': [50, 63, 15],
    'Wicket': [0, 2, 3],
    'Catch': [4, 2, 1]
}
 
# Make data frame of above data
df = pd.DataFrame(data)
 
# append data frame to CSV file
df.to_csv(r'E:\GIT\learn\100day_of_code\pandas_01\Simada.csv', mode='a', index=False, header=False)
print(user_data)