def PropertyEntity(item) -> dict:
    return {
        "property_id": str(item['_id']),
        'property_name': item['property_name'],
        'address': item['address'],
        'city': item['city'],
        'state': item['state']
    }

def PropertiesEntity(entity) -> list:
    return [PropertyEntity(item) for item in entity]