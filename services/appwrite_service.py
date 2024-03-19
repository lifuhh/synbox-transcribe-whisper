
from dotenv import load_dotenv
import os
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID

load_dotenv()

class AppwriteService:

  def __init__(self):
    self.client = Client()
    self.project_id = os.getenv("APPWRITE_PROJECT_ID")
    self.api_secret = os.getenv("APPWRITE_KEY")
    self.collection_id = os.getenv("APPWRITE_COLLECTION_ID")
    self.database_id = os.getenv("APPWRITE_DB_ID")
    self.client.set_endpoint('https://cloud.appwrite.io/v1')
    self.client.set_project(self.project_id)
    self.client.set_key(self.api_secret)
    self.databases = Databases(self.client)

    # self.client.set_project(os.getenv("APPWRITE_PROJECT"))
    # self.client.set_key(os.getenv("APPWRITE_SECRET"))
    # self.storage = Storage(self.client)


  def upload_lyrics(self, video_id, data):

    print("upload_database - video_id received: ", video_id)
    print("upload_database - data received: ", data)

    placeholder_vid_id = 'VyvhvlYvRnc'      

    placeholder_data = {
      "visit_count":0,
      "full_lyrics":"full_lyrics_yapyap",
      "kanji_annotation":"kanji_yapyap",
      "romaji":"romaji_yapyap",
      "eng_translation":"eng_yapyap",
      "chi_translation":"chi_yapyap", 
    }

    self.databases.create_document(
      database_id=self.database_id,
      collection_id=self.collection_id,
      document_id=placeholder_vid_id,
      # document_id=video_id,
      data=placeholder_data
    )

  def edit_lyrics(self, video_id, data):

    print("edit_database - video_id received: ", video_id)
    print("edit_database - data received: ", data)

    self.databases.update_document(
      database_id=self.database_id,
      collection_id=self.collection_id,
      document_id=video_id,
      data=data
    )

  def get_lyrics(self, video_id):
      
      print("get_lyrics - video_id received: ", video_id)

      document = self.databases.get_document(
        database_id=self.database_id,
        collection_id=self.collection_id,
        document_id=video_id
      )

      print("get_lyrics - document received: ", document)

      return document

  def update_lyrics(self, video_id, field, data):
        
      print("update_lyrics - video_id received: ", video_id)
      print("update_lyrics - field received: ", field)
      print("update_lyrics - data received: ", data)

      if(field == "visit_count"):
        self.databases.update_document(
            database_id=self.database_id,
            collection_id=self.collection_id,
            document_id=video_id,
            data={field: data+1}
          )

      else:
        self.databases.update_document(
          database_id=self.database_id,
          collection_id=self.collection_id,
          document_id=video_id,
          data={field: data}
        )


# db_access = AppwriteService()
# # db_access.upload_lyrics('VyvhvlYvRnc', 'test')
# print("PART 1")
# db_access.update_lyrics('VyvhvlYvRnc', 'full_lyrics', 'test_replace_v2')
# db_access.get_lyrics('VyvhvlYvRnc')
# print("PART 2")
# db_access.update_lyrics('VyvhvlYvRnc', 'visit_count', 5)
# db_access.get_lyrics('VyvhvlYvRnc')
# print("PART 3")
# db_access.update_lyrics('VyvhvlYvRnc', 'romaji', 'romaji_test_replace_v1')
# db_access.get_lyrics('VyvhvlYvRnc')
# print("ALL DONE")
    
  