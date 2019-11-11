#!/usr/bin/python3

import os
import json

class FileStorage:

    __file_path = "file.json"
    __objects = {}


    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def reload(self):
        
        if not os.path.isfile(FileStorage.__file_path):
            return FileStorage.__objects

        with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
            strjson = f.read()

            FileStorage.__objects = json.loads(strjson)

            from models.base_model import BaseModel 
            for key, obj_json in FileStorage.__objects.items():
                FileStorage.__objects[key] = BaseModel(**obj_json)
            
        return FileStorage.__objects




    def save(self):

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            f.write("{")
            i = 0
            for key, value in FileStorage.__objects.items():
                json_obj = json.dumps(value.to_dict())
                if i == 0:
                    f.write("\""+value.__class__.__name__ + "."+value.id+"\"" +":"+json_obj)
                else:
                    f.write(",\""+value.__class__.__name__ + "."+value.id+"\"" +":"+json_obj)
                i += 1
            f.write("}")

