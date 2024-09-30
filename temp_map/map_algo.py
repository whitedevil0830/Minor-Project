import pandas as pd, re
def get_city_data(city_names, filename="IN_capitals.xlsx"):

    # Read city data from the Excel spreadsheet
    try:
        df = pd.read_excel(filename, usecols=['name', 'latitude', 'longitude'])
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the file path and try again.")
        return {}

    # Convert city names to lowercase for case-insensitive matching
    df['name'] = df['name'].str.lower()
    city_names = [name.lower() for name in city_names]
    print(city_names)

    # Create a dictionary to store city data
    city_data = {name: None for name in city_names}
    print(city_data)
    # Find data for requested cities
    for name in city_names:
        print(name)
    
        if name in df['name'].values:
            print("-----------------------------------------------")
            city_data[name] = (df[df['name'] == name]['latitude'].values[0], df[df['name'] == name]['longitude'].values[0])
            # print(df['name'].values)
            print(city_data)
    
    return city_data



    # Get user input for city names
city_names = input("Enter comma-separated city names: ").split(", ")
    # Get city data from the dataset
city_data = get_city_data(city_names)

    # Check if any city data was retrieved
if not city_data:
    print("No city data retrieved. Exiting...")
