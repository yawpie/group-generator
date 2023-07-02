import os
import json


class ReadJsonData:
    NAME = "*.json"
    jsonLoad = {}

    def filename(self, name="*.json"):
        self.NAME = name
        FILENAME = os.getcwd()+"\\"+self.NAME
        try:
            file = open(FILENAME, "r")
        except:
            print("Error: Could not open",
                  self.NAME, "file didn't exist!")
            return

        try:
            self.jsonLoad.update(json.load(file))
        except:
            print("Error: JSON Error")
            return
        print("operation success")
        file.close()

        return self.jsonLoad

# todo buat supaya dia bisa memecah data yang ada di json


def main():
    ReadJsonData().filename("data.json")


if __name__ == "__main__":
    main()
