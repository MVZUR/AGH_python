import json
from dataclasses import dataclass

@dataclass

class Person:
    name:str
    surname:str
    address:str
    postal_code:str
    pesel:int


    def json_write(self):
        data_w = [self.name, self.surname, self.address, self.postal_code, self.pesel]
        with open("data.json", 'w') as f:
            json.dump(data_w, f)


    def json_read(self):
        with open('data.json') as f:
            data_r = json.load(f)
            print (data_r)

Person1 = Person("Gzib", "Kowalski","Adama Mickiewicza 30", "30-059", 82022181183)




Person.json_write(Person1)
Person.json_read(Person1)