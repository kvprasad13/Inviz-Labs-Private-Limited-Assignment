from bson import ObjectId
from fastapi import APIRouter,Path
from models.property import Property
from config.db import conn
from schemas.property import PropertyEntity, PropertiesEntity
from pydantic import BaseModel
from typing import Optional

property =APIRouter()

class UpdateProperty(BaseModel):
    property_id: str
    property_name:Optional[str]=None
    address:Optional[str]=None
    city:Optional[str]=None
    state:Optional[str]=None


db = conn.get_database("InvizLabsAssignment-backend")
property_collection = db.get_collection("property")
@property.get('/')
async def find_all():
    return PropertiesEntity(property_collection.find())
 

@property.get('/get-property-details/{city_name}')
async def fetch_property_details(city_name:str=Path(description="The city name need to give for properties to view")):
    

    return {"properties belongs to the city": PropertiesEntity(property_collection.find({'city':city_name}))}
 
    

@property.get('/get-cities-by-state/{state_name}')
async def fetch_cities_by_state(state_name:str):
    
    cities=[]
    properties =PropertiesEntity(property_collection.find({'state':state_name}))
    for obj in properties:
       
        cities.append(obj['city'])
        
    return {"all city names that belong with the state": set(cities)}
   
    

@property.get('/similar-properties-by-property-id/{property_id}')

async def find_similar_properties(property_id:str):
    

    properties=[]
        
    property =PropertyEntity(property_collection.find_one({'_id':ObjectId(property_id)}))

    for obj in PropertiesEntity(property_collection.find({'city':property['city']})):
            
        properties.append(obj['property_name'])
        
    return {"properties": properties}

 
        

@property.post('/create-new-property')
async def create_new_property(property: Property):
    properties = property_collection.find({
        'city': property.city,
        'state': property.state,
        'property_name': property.property_name,
        'address': property.address
    })

    if len(PropertiesEntity(properties)) > 0:
        return {"Error": "Property details already exist."}

    insert_result = property_collection.insert_one(dict(property))
    inserted_id = insert_result.inserted_id
    return PropertyEntity(property_collection.find_one({'_id': inserted_id}))


@property.put('/update-property-details')
async def update_property_details(updateProperty:UpdateProperty):

    property =  property_collection.find_one({'_id':ObjectId(updateProperty.property_id)})
    if updateProperty.property_name:
        property['property_name'] = updateProperty.property_name
    if updateProperty.address:
        property['address'] = updateProperty.address
    if updateProperty.city:
        property['city'] = updateProperty.city
    if updateProperty.state:
        property['state'] = updateProperty.state

        
    property_collection.find_one_and_update({'_id':ObjectId(updateProperty.property_id)},{
       '$set': {'property_name': property['property_name'], 'address': property['address'],  'city': property['city'],'state': property['state']}
        })

    return  PropertiesEntity(property_collection.find())

    



    
