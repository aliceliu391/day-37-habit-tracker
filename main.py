import requests

USERNAME = "YOUR_USER"
TOKEN = "YOUR_TOKEN"
GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN,
}


def create_new_user():
    user_parameters = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=pixela_endpoint, json=user_parameters)
    print(response.text)


def create_graph():
    graph_parameters = {
        "id": GRAPH_ID,
        "name": "Coding Habits",
        "unit": "mins",
        "type": "int",
        "color": "ajisai"
    }

    response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
    print(response.text)


def update_pixel():
    update_parameters = {
        "quantity": f"{input("How many minutes did you code?: ")}",
    }
    response = requests.put(url=update_endpoint, json=update_parameters, headers=headers)
    print(response.text)


def delete_pixel():
    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)


def configure_profile():
    user_configure_endpoint = f"https://pixe.la/@{USERNAME}"
    user_configure_parameters = {
        "displayName": "Alice ♡",
        "timezone": "Canada/Eastern",
        "pinnedGraphID": GRAPH_ID
    }
    response = requests.put(url=user_configure_endpoint, json=user_configure_parameters, headers=headers)
    print(response.text)


pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

still_editing = True
while still_editing:
    choice = input("What do you want to do? Delete pixel (d), update pixel (u), or exit (e)? ").lower()
    if choice == "e":
        print("Bye bye! Hope to see you again soon.")
        still_editing = False
    else:
        formatted_date = input("Enter the date you wish to alter (yyyyMMdd): ")
        update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
        delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
        if choice == "d":
            delete_pixel()
        elif choice == "u":
            update_pixel()
        else:
            print("Invalid Choice")
