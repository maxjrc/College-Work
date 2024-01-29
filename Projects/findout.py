import requests


def lookup():
    print("Please enter a name: ")
    name = input()
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    querystring = {"term":name}
    headers = {
	"X-RapidAPI-Key": "47c1ba099cmsh8f1a4063990aa11p1b58a0jsn203cd995d18b",
	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    json_object = response.json()
    about = json_object["list"][0]["definition"]
    print("Here is what " + name + " is all about" + about)

lookup()
        