import json
from jsonschema import validate
schema_file = {
    "type":"object",
    "properties":{
        "id":{"type":"number"},
        "name":{"type":"string"},
        "homephone":{
            "type":"number"
        },
        "cellphone":{
            "type":"number"
        },
        "workphone":{
            "type":"number"
        },
        "birthdate":{"type":"string"},
        "govid":{"type":"string"},
        "gender":{
            "type":"string",
        },
        "day":{
            "type":"string",
            "enum":["SU","MO","TU","WE","TH","FR","SA"]
        }
    },
    "required":["id","name"],
    "anyOf":[
            {"required":["homephone"]},
            {"required":["cellphone"]},
            {"required":["workphone"]},
    ],
    "oneOf":[
        {"required":["birthdate"]},
        {"required":["govid"]},
    ],
    "additionalItems":False,
}

json_data = """{"id":1, "name":"Ram",
             "birthdate":"01/12/2002",
             "homephone":6789543267, 
             "gender":"M",
             "day":"SU"}"""
class jsonvalidator:
    @staticmethod
    def validate_schema(json_file,schema_file):
        try:
            js=json.loads(json_file)
            validate(js,schema_file)
        except Exception as e:
            print(e)
            return False
        return True
k = jsonvalidator()
valid=k.validate_schema(json_data,schema_file)
if valid:
    #print(json_data)
    print("Given json data is valid")
else:
    #print(json_data)
    print("Given json data is invalid")



