'''import pandas as pd

data  = { 'Name': ['aung', 'kyaw', 'zaww'], 'Age': [21, 22, 23], 'Adress': ['1road', '2road', '3road', ], 'Qualification' : ['BA', 'MA', 'MSC']}

    df = pd.Dataframe(data)

    print(df[['Name', 'Qualification']])'''

# Import pandas package
import pandas as pd

# Define a dictionary containing Students data
    data = {"Name": ["Jai", "Princi", "Gaurav", "Anuj"], "Height": [5.1, 6.2, 5.1, 5.2],"Qualification": ["Msc", "MA", "Msc", "Msc"]}

    # Convert the dictionary into DataFrame
    df = pd.DataFrame(data)

    # Declare a list that is to be converted into a column
    address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']

    # Using 'Address' as the column name
    # and equating it to the list
    df['Address'] = address

    # Observe the result
    print(df)
