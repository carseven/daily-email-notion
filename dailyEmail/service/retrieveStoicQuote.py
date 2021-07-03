import random
import requests


def random_stoic_quote() -> tuple[str, str]:
    # url contract
    random_id = random.randint(0, 1000)
    url = f"https://stoic-server.herokuapp.com/quotes/{random_id}"

    # GET
    response = requests.get(url=url)

    if response.status_code == 200:
        return response.json()[0]["author"], response.json()[0]["body"]
    else:
        return "Error", "Error en random_stoic_quote"
