import json
import xml.etree.ElementTree as ET

class DisplayService:

    _instance = None

    @staticmethod
    def getInstance():
        if DisplayService._instance is None:
            DisplayService._instance = DisplayService()
        return DisplayService._instance

    def display(self, json_data):
        print("Displaying Data")
        print(json.dumps(json_data, indent=4))


class Database:

    def getXML(self):

        return """
        <news>
            <title>TechPrysm Launches AI Platform</title>
            <author>Ikhlas Ahmad</author>
            <text>TechPrysm officially launched its AI-powered learning platform.</text>
        </news>
        """


class XMLToJSONAdapter:

    def convert(self, xml_data):

        root = ET.fromstring(xml_data)

        json_data = {
            "title": root.find("title").text,
            "author": root.find("author").text,
            "text": root.find("text").text
        }

        return json_data


def main():

    database = Database()

    adapter = XMLToJSONAdapter()

    display = DisplayService.getInstance()

    xml_data = database.getXML()

    json_data = adapter.convert(xml_data)

    display.display(json_data)


if __name__ == "__main__":
    main()