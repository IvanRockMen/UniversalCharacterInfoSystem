import io
import json

class character():
    def __init__(self):
        self.nickname = ""
        self.first_name = ""
        self.second_name = ""
        self.model_path = ""
        self.material_path = ""
        self.char_sex = ""
        self.char_age = 0
        self.ability  = []

    def create(self, nickname, first_name, second_name, model_path, material_path, char_sex, char_age, ability):
        json_file_data = "{" + "\n"
        json_file_data += '"nickname"' + ":" + '"' + nickname + '"'  + "," + "\n"
        json_file_data += '"first_name"' + ":" + '"' + first_name + '"' + "," + "\n"
        json_file_data += '"second_name"' + ":" +  '"' + second_name + '"' + "," +  "\n"
        json_file_data += '"model_path"' + ":" +  '"' + model_path + '"' + "," + "\n"
        json_file_data += '"material_path"' + ":" +  '"' + material_path + '"' + "," + "\n"
        json_file_data += '"char_sex"' + ":" +  '"' +  char_sex + '"' + "," + "\n"
        json_file_data += '"char_age"' + ":" + str(char_age) + "\n"
        json_file_data += "}"
        
        self.nickname = nickname
        self. first_name = first_name
        self.second_name = second_name
        self.model_path = model_path
        self.material_path = material_path
        self.char_sex = char_sex
        self.char_age = int(char_age)

        f = open("char_info.json", "w")
        f.write(json_file_data)
        f.close()

    def loadInfoFromFile(self, path = "char_info.json"):
        f = open(path, "r")
        json_text = f.read()
        f.close()

        data = json.loads(json_text)

        return data
        

if __name__ == "__main__":
    character.create(character, nickname = "test", first_name = "test", second_name = "test", model_path = "/test/", material_path = "/test/", char_sex = "male", char_age = 20, ability = [])
    print(character.loadInfoFromFile(self = character)['first_name'])