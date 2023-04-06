
from service import retrieveStoicQuote, retrieveNotionDatabase
import utils
from tokens import SECRETS
from send_email import send_email
import html_email as html
import datetime
from datetime import timezone
# Notion api config
password = f"Bearer {SECRETS['notion_test_token']}"
headers = {
    "Authorization": password,
    "Notion-version": "2021-05-13"
}

tomorrow = (
    datetime.datetime.now(timezone.utc) +
    datetime.timedelta(days=1)
).astimezone().isoformat()
query = {
    "filter": {
        # "and": [
        #     {
        #         "property": "Done",
        #         "checkbox": {
        #             "equals": False
        #         }
        #     },
        #     {
        #         "property": "Due",
        #         "date": {
        #             "before": tomorrow
        #         }
        #     }
        # ]
    },
    "sorts": [
        # {
        #     "property": "Due",
        #     "direction": "ascending"
        # },
        # {
        #     "property": "State",
        #     "direction": "descending"
        # }
    ]
}

# Notion api database block http request
database = retrieveNotionDatabase.retrieveDatabase(
    databaseId=SECRETS['database_id'],
    headers=headers,
    save_to_json=False,
    # query=query
)

# Print retrieve database data
# utils.debugDatabaseObject(database)

# Get data we want from database.json object
database_list = utils.decodeDatabase(database)
dbProperties = utils.databaseProperties(database_list)

# Filter columns of the database
dbProperties = ['State', 'Task', 'Api-projects', 'Due',
                'Kanban - State', 'Priority', 'Type']
# Data to html table
title = "\n".join(html.html_table_column(dbProperties))
rows = "\n".join(html.html_table_row(
    database_list,
    dbProperties
))
table_html = html.construct_html_table(title, rows)

# Get random stoic quote
author, stoic_quote = retrieveStoicQuote.random_stoic_quote()

html_msg = html.construct_html_msg(
    table_html,
    html.style,
    html.quote_html(author, stoic_quote)  # Format stoic quote to html
)

# utils.save_html(html_msg)

# Send email with html msg
send_email(
    html_msg,
    SECRETS['email_from'],
    SECRETS['email_to'],
    SECRETS['gmail_password']
)
