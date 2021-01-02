import xml.etree.ElementTree as ET
import pymongo

# https://www.etutorialspoint.com/index.php/292-how-to-insert-xml-data-to-mongodb-using-python
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["StackOverflow"]
mycol = mydb["Tags"]

tree = ET.parse('Tags.xml')

tag = tree.findall('tags')

for i in tag:
    RowID = i.find('row Id').text
    TagName = i.find('TagName').text
    Count = i.find('Count').text
    PostID = i.find('ExcerptPostId').text
    WikiPostId = i.find('WikiPostId').text

    tag_dict = [
                {'Row ID': RowID, 'TagName': TagName, 'Count': Count, 'PostID': PostID, 'WikiPostId': WikiPostId}                
               ]

    x = mycol.insert(tag_dict)    

for y in mycol.find():
  print(y)
