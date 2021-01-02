import pymongo
import xml.etree.ElementTree as ET

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["school"]
mycol = mydb["students"]

tree = ET.parse('Tags.xml')

stud = tree.findall('tags')

for ep in stud:
    RowID = ep.find('row Id').text
    TagName = ep.find('TagName').text
    Count = ep.find('Count').text
    PostID = ep.find('ExcerptPostId').text
    WikiPostId = ep.find('WikiPostId').text

    tag_dict = [
                {'Row ID': RowID, 'TagName': TagName, 'Count': Count, 'PostID': PostID, 'WikiPostId': WikiPostId}                
               ]

    x = mycol.insert(tag_dict)    

for y in mycol.find():
  print(y)
