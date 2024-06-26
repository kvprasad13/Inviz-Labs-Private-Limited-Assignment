# 1) create_new_property
# 	Input: property name, address, city, and state.
# 	Output: list of properties with all details.
# 2) fetch_property_details
# 	Input: city name.
# 	Output: a list of all properties that belong to the city name passed in the input
# 3) update_property_details
# 	Input: property_id, property name, address, city, state
# 	Output: same as create_new_property API with updated information
# 4) Additional but non-mandatory APIs:
# 		Extra points will be awarded if you complete the below APIs
# 			a) find_cities_by_state: 
# 				Input: state_id or state_name
# 				Output: all city names that belong with the state
# 			b) find_similar_properties
# 		Input: property_id
# 		Output: list of all properties that belong to the same city as that of given property_id


from fastapi import FastAPI,Path

from routes.property import property

app = FastAPI()
app.include_router(property)

