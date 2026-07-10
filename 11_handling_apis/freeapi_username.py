import requests

def fetch_random_user_from_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else :
        raise Exception("Failed to fetch user data")
    
def fetch_youtube_video_data_from_freeapi():
    url = "https://api.freeapi.app/api/v1/public/youtube/videos"
    response = requests.get(url)
    data = response.json()

    list_of_video_info = []
    if data["success"] and data["data"]:
        for list in data["data"]["data"]:
            list_of_video_info.append({"video_title":list["items"]["snippet"]["title"],"views":list["items"]["statistics"]["viewCount"],"likes":list["items"]["statistics"]["likeCount"]})
        return list_of_video_info
    else:
        raise Exception("Failed to fetch video data")

# POST Request for saving user https://api.freeapi.app/api/v1/users/register
def save_user_info_to_freeapi():
    url = "https://api.freeapi.app/api/v1/users/register"
    headers = {
        "accept":"application/json",
        "content-Type":"application/json"
    }
    payload = {
        "email": "raheudl3.email@domain.com",
        "password":"Pata nahi",
        "role":"ADMIN",
        "username":"taheud3l.232"
    }
    response = requests.post(url,headers=headers,json=payload)
    # print(response.json())
    data = response.json()

    if data["success"] and data["data"]:
        messages = data["message"]
        return messages
    else:
        raise Exception("Failed to add user")



def main():
    try:
        # username, country = fetch_random_user_from_freeapi()
        # print(f"Username: {username}\nCountry: {country}")
        # list_of_video = fetch_youtube_video_data_from_freeapi()
        # print(list_of_video)
        messages = save_user_info_to_freeapi()
        print(messages)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()