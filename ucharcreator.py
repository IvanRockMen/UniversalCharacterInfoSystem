import io
import json
import pathlib
import tarfile
import os

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

    def fillAbility(self, abName, abLevel):
        return self.ability.append([abName, abLevel])

    def setNickName(self, nick):
        self.nickname = str(nick)
    
    def setFirstName(self, FN):
        self.first_name = str(FN)

    def setSecondName(self, SN):
        self.second_name = str(SN)

    def setModelPath(self, path, modelName):
        self.model_path = str(path)+str(modelName)

    def setMaterialPath(self, path, materialName):
        self.material_path = str(path)+str(materialName)

    def setCharSex(self, sex):
        self.char_sex = str(sex)
    
    def setCharAge(self, age):
        self.char_age = age

    def create(self):
        json_file_data = "{" + "\n"
        json_file_data += '"nickname"' + ":" + '"' + self.nickname + '"'  + "," + "\n"
        json_file_data += '"first_name"' + ":" + '"' + self.first_name + '"' + "," + "\n"
        json_file_data += '"second_name"' + ":" +  '"' + self.second_name + '"' + "," +  "\n"
        json_file_data += '"model_path"' + ":" +  '"' + self.model_path + '"' + "," + "\n"
        json_file_data += '"material_path"' + ":" +  '"' +self.material_path + '"' + "," + "\n"
        json_file_data += '"char_sex"' + ":" +  '"' +  self.char_sex + '"' + "," + "\n"
        json_file_data += '"char_age"' + ":" + str(self.char_age) + "\n"
        json_file_data += '"ability"' + ":" + "[" + "\n"
        for i in range(len(self.ability)):
            json_file_data += '"' + self.ability[i][0] + '"' + ":" + str(self.ability[i][1]) + "\n"
        json_file_data += "]" + "\n"
        json_file_data += "}"

        f = open("char_info.json", "w")
        f.write(json_file_data)
        f.close()

    def loadInfoFromFile(self, path = "char_info.json"):
        f = open(path, "r")
        json_text = f.read()
        f.close()

        data = json.loads(json_text)

        return data

    def writeCharFile(self, filename="character"):
        tar = tarfile.open(filename+".chrt", "w:gz")
        tar.add('char_info.json')
        try:
            tar.add(self.material_path)
        except FileNotFoundError:
            print('Вы ввели неправильный путь или имя материала')
        try:
            tar.add(self.model_path)
        except FileNotFoundError:
            print('Вы ввели неправильный путь или имя модели')
        tar.close()

    def downloadResourcesFromCharFile(self, filename, output):
        output = os.getcwd()+output
        tar = tarfile.open(str(filename)+".chrt", "r")
        tar.extractall(output)
        tar.close()
        


if __name__ == '__main__':
    mychar = character()
    mychar.setCharAge(18)
    mychar.setCharSex('male')
    mychar.setModelPath('/testpath', 'test.obj')
    mychar.setMaterialPath('/testmatpath', 'test.mat')
    mychar.setNickName('Nagibator3000')
    mychar.setFirstName('Vasya')
    mychar.setSecondName('Pupkin')
    mychar.fillAbility('Pizdabolstvo', 100)
    mychar.create()
    mychar.writeCharFile()
    mychar.downloadResourcesFromCharFile('character', '/mychar')