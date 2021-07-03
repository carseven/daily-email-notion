import datetime


def decodeDatabase(database: dict) -> list[dict[str, str]]:
    db = []
    for row in database["results"]:
        row_properties = {}
        for column in row["properties"].keys():
            row_properties[column] = retrievePropertyValue(
                column,
                row
            )
        db.append(row_properties)
    return db


def retrievePropertyValue(property: str, row: dict) -> str:
    value = ""
    if row["properties"][property]["type"] == "checkbox":
        value = row["properties"][property]["checkbox"]

    if row["properties"][property]["type"] == "title":
        if row["properties"][property]["title"]:
            value = row["properties"][property]["title"][0]["plain_text"]

    if row["properties"][property]["type"] == "rich_text":
        if row["properties"][property]["rich_text"]:
            value = row["properties"][property]["rich_text"][0]["plain_text"]

    if row["properties"][property]["type"] == "number":
        value = row["properties"][property]["number"]

    if row["properties"][property]["type"] == "date":
        date = row["properties"][property]["date"]["start"]
        try:
            # TODO: Formatear correctamente la fecha
            date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
        except ValueError:
            value = date

    if row["properties"][property]["type"] == "select":
        value = row["properties"][property]["select"]["name"]

    return str(value)


def debugDatabaseObject(database, flag=False):
    count = 0
    for row in database["results"]:
        print("----------------")
        print(f"Fila {count}")
        print("----------------")
        for columna in row["properties"].keys():
            if flag:
                print(row["properties"][columna])
            column_value = ""
            if row["properties"][columna]["type"] == "checkbox":
                column_value = row["properties"][columna]["checkbox"]

            if row["properties"][columna]["type"] == "number":
                column_value = row["properties"][columna]["number"]

            if row["properties"][columna]["type"] == "title":
                if row["properties"][columna]["title"]:
                    column_value = row["properties"][columna]["title"][0]["plain_text"]

            if row["properties"][columna]["type"] == "rich_text":
                if row["properties"][columna]["rich_text"]:
                    column_value = row["properties"][columna]["rich_text"][0]["plain_text"]

            if row["properties"][columna]["type"] == "date":
                column_value = row["properties"][columna]["date"]["start"]
            print(f"{columna} -> {column_value}")

        print("----------------\n")
        count += 1


def databaseProperties(database: list) -> list[str]:
    databaseProperties = []
    for row in database:
        for property in row.keys():
            if property not in databaseProperties:
                databaseProperties.append(property)
    return databaseProperties


def save_html(html_msg: str):
    with open("./daily-email/saved-data/email-msg.html", "w", encoding="utf8") as f:
        f.write(html_msg)
        f.close()
