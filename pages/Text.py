import streamlit as st
import pydeck as pdk
import pandas as pd
import plotly.express as px
from DistanceAlgo.nn import NearestNeighbor  # Import NearestNeighbor class

def main():
    """
    Streamlit app for TSP visualization with location fetching.
    """

    # Title and description
    st.title("TripBlazer")
    # st.text("Enter city names and visualize the route.")

    # # City input form
    # city_form = st.form("city_input")
    # City input form (multi-line text input)
    city_names = st.text_area("Enter City Names (comma-separated)", height=100)
    submit_button = st.button("Submit")

    # Process city names only after clicking submit
    cities = []
    if submit_button:
        if city_names:
            cities = city_names.strip().split(",")
            cities = [city.strip() for city in cities]  # Remove leading/trailing whitespace

            # Load location data from Excel (error handling included)
            try:
                location_data = pd.read_excel("temp_map/IN_capitals.xlsx")
            except FileNotFoundError:
                st.error("Error: DB file not found. Please ensure it exists in the same directory.")
                return
            # location_data['name'] = location_data['name'].str.lower()
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
            st.write("Route:", route)
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
                # height=50
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




if __name__ == "__main__":
    main()
