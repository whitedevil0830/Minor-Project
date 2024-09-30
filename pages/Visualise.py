import streamlit as st
import plotly.express as px
import pandas as pd
import os
from DistanceAlgo.nn import NearestNeighbor
path = "C:/Users/KIIT/OneDrive/Desktop/codes set/MY CODES/MINOR PROJECT/bucket lists/"

def algo_submit(opt,opt1):
    with st.sidebar:
        st.write("selected options:")
        st.write(f"Algorithm: {opt}")
        st.write(f"List: {opt1}")

files = os.listdir(path)
lists = []
for file in files:
    lists.append(file.strip().split(".txt"))
list_names = []
for i in lists:   
    list_names.append(i[0])


with st.sidebar:
    option = st.selectbox(label="Choose an algo...",options=["NN algo"])
    option1 = st.selectbox(label="Choose a list...",options=list_names)
    if st.button(label="Visualize"):
        algo_submit(option,option1)

def nn_algo():
    """
    Streamlit app for TSP visualization with location fetching.
    """

    # Title and description
    st.title("TripBlazer")
    st.text(f"List of city names in '{option1}' :")
    city_names = []
    
    with open(path + option1 + ".txt","r") as f:
        city_names = f.readlines()
        count = 0
        for i in city_names:
            count += 1
            st.write(count,") ",i.capitalize())
    submit_button = st.button("Submit")

    # Process city names only after clicking submit
    cities = []
    if submit_button:
        if city_names:
            cities = [city.strip() for city in city_names]  # Remove leading/trailing whitespace

            # Load location data from Excel (error handling included)
            try:
                location_data = pd.read_excel("temp_map/IN_capitals.xlsx")
            except FileNotFoundError:
                st.error("Error: DB file not found. Please ensure it exists in the same directory.")
                return

            cities = [name.capitalize() for name in cities]
            # Ensure city names exist in the Excel data (error handling)
            valid_cities = []
            for city in cities:
                if city in location_data["name"].tolist():
                    valid_cities.append(city)
                else:
                    st.warning(f"Warning: City '{city}' not found in DB. Skipping.")

            if not valid_cities:
                st.error("No valid cities found. Please check city names and 'IN.xlsx' data.")
                return

            # Extract valid city locations from Excel
            city_data = []
            for city in valid_cities:
                city_row = location_data[location_data["name"] == city]
                latitude = city_row["latitude"].values[0]
                longitude = city_row["longitude"].values[0]
                city_data.append((city, (latitude, longitude)))

            # Solve using NN algorithm
            nn = NearestNeighbor(city_data)
            route, total_distance = nn.solve()

            # Display results
            st.subheader("Results:")
            st.write("Route (in order):")
            cnt = 0
            for i in route:
                cnt += 1
                st.write(cnt,") ",i)
            st.write("Total Route Length:", total_distance)

            c1, c = zip(*city_data)
            c2, c3 = zip(*c)
            city_df = pd.DataFrame({'name': c1, 'latitude': c2, 'longitude': c3})

            fig = px.scatter_mapbox(
                city_df,
                lat="latitude",
                lon="longitude",
                hover_name="name",
                zoom=3,
                mapbox_style="open-street-map",
            )

            city_df.sort_values(by="name", key=lambda column: column.map(lambda e: route.index(e)), inplace=True)
            
            fig.add_trace(
                px.line_mapbox(
                    city_df,
                    lat="latitude",
                    lon="longitude",
                    hover_name = city_df["name"],
                    # color = city_df["name"],
                ).data[0]
            )

            st.plotly_chart(fig)
        
        else:
            st.error("Please enter some city names before submitting.")

if option == "NN algo":
    nn_algo()
elif option == "K-fold":
    pass
else:
    pass