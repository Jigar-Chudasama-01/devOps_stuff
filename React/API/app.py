import requests

def get_cat_fact():
    url = "https://meowfacts.herokuapp.com/"
    response = requests.get(url)
    if response.status_code == 200:
        fact = response.json().get("data", ["No fact available"])[0]
        print("Cat Fact:", fact)
    else:
        print("Failed to fetch cat fact")

if __name__ == "__main__":
    get_cat_fact()
