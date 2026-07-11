import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://palrahulkumar2002_db_user:MRF1EZ6eLx0nilfj@cluster0.ldufkym.mongodb.net")

db = client["user_for_python_learning"]
video_collection = db["videos"]

def list_all_videos():
    videos = list(video_collection.find())
    if len(videos) == 0:
        print("Videos are not uploaded yet")
    for video in videos:
        print(f"ID: {video["_id"]}, Name: {video["name"]}, Time: {video["time"]}")

def add_video(name,time):
    video_collection.insert_one({"name":name, "time":time})
    print("Video added successfully.")

def update_video(id,name,time):
    video_collection.update_one({"_id":ObjectId(id)},{"$set":{"name":name, "time":time}})

def delete_video(id):
    video_collection.delete_one({"_id":ObjectId(id)})
    print("Video deleted successfully.")


def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List all videos")
        print("2. Add videos")
        print("3. Update video info")
        print("4. Delete video")
        print("5. Exit app")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            list_all_videos()
        elif choice == 2:
            name  = input("Enter video name: ")
            time  = input("Enter video time: ")
            add_video(name,time)
        elif choice == 3:
            list_all_videos()
            id = input("Enter video id to update: ")
            name  = input("Enter updated video name: ")
            time  = input("Enter updated video time: ")
            update_video(id,name,time)
        elif choice == 4:
            list_all_videos()
            id = input("Enter video id to delete: ")
            delete_video(id)
        elif choice == 5:
            break
        else:
            print("Enter valid option")

if __name__ == "__main__":
    main()
