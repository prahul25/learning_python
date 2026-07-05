import json



def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(video):
    for index, video in enumerate(video,start = 1):
        print(f"{index}. {video['name']}, Duration: {video['length']}")

def add_new_video(video):
    name = input("Enter video name: ")
    length = input("Enter video length: ")
    video.append({"name":name,"length":length})
    save_data_helper(video)

def update_video(video):
    list_all_videos(video)
    index = int(input("Enter video number to update: "))
    if 1 <= index <= len(video):
        new_name = input("Enter new name for the video: ")
        new_len = input("Enter new video length for the video: ")
        video[index-1] = {"name":new_name,"length":new_len}
        save_data_helper(video)
        print("Here is updated video list")
        list_all_videos(video)
    else:
        print("Invalid index selected ")

def delete_video(video):
    list_all_videos(video)
    index = int(input('Enter index number to delete video: '))

    if 1 <= index <= len(video):
        del video[index-1]
        save_data_helper(video)
        print("Here is updated video list")
        list_all_videos(video)
    else:
        print("Invalid index selected ")

def main():

    video = load_data()
    while True:
        print("\n--- YouTube Video Manager ---")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update video details")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        # print(video)
        match choice:
            case "1":
                list_all_videos(video)
            case "2":
                add_new_video(video)
            case "3":
                update_video(video)
            case "4":
                delete_video(video)
            case "5":
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()