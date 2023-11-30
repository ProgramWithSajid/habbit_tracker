import requests
import datetime as dt


username = "sajidali"
token = "jiaoorgnoaro4404nga"
graphid = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
parameter = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint, json=parameter)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"


graph_config = {
    "id": graphid,
    "name": "Coding Hour",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN" : token
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixelo = f"{graph_endpoint}/{graphid}"

today = dt.datetime.now()                   #year=2023, month=11, day=29

post_param = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many minutes you code today?: "),
}

response = requests.post(post_pixelo, json=post_param, headers=headers)
print(response.text)


#put request
# new_put_pixelo = f"{post_pixelo}/{today.strftime('%Y%m%d')}"
# new_put_param = {
#     "quantity":"25"
# }
# response = requests.put(new_put_pixelo, json=new_put_param, headers=headers)
# print(response.text)