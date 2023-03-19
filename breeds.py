import requests

response = requests.get("https://api.thedogapi.com/v1/breeds/2")

n = int(input("Enter the number of breeds : "))

for i in range(1,n):
    i = str(i)
    response = requests.get("https://api.thedogapi.com/v1/breeds/"+i)
    with open('dogBreeds.txt',"a") as file:
        file.write(response.json()["name"] + "\n")