
    
<h2 style="
    text-align: center;
    font-weight:200;
    font-size: 28px;
    text-transform: uppercase;
">Daily e-mail from notion database</h2>
<p align="center">
    <img width="40%" src="doc/logo.png"/>
</p>

Añadir link licencia
## Installing dependencies
```bash
python -m pip install --upgrade pip
pip install requests python-dateutil
```
## Notion configuration
1. Created notion integration
2. Invite integration
    * ⚠ Warning: Also relation databases, to have access to their information
3. Get database id from url
## Script configuration
1. Generated ```dailyEmail/tokens.py``` file with ```SECRET``` dictionary with the sensible information.

    Make sure to include this file in the ```.gitignore``` file to avoid upload sensible

```python
SECRETS = {
    'notion_test_token': '',
    'database_id': '',
    'gmail_password': '',
    'email_from': '',
    'email_to': ''
}
```

2. By default the email table will print all the columns/properties from the notion database. If we need just to print some of the columns set the ```dbProperties``` list with the name of the columns we want to print.

    Be aware of the order, beacause it will be use the order from the list. We could re-order the list if we want.
```python
dbProperties = ['State', 'Task', 'Api-projects', 'Due',
                'Kanban - State', 'Priority', 'Type']
```
3. If we want to change the style of the table you could modify the style string from ```dailyEmail/html.py```. In my case, I use the following tutorial as a  [reference](https://dev.to/dcodeyt/creating-beautiful-html-tables-with-css-428l).

## Github action configuration
1. Codificar con base64
2. Como decodificar y como añadir el secreto tokens.py
3. Como editar cada cuando se lanza el email


## Results
Explicar las funcionalidades que se han añadido.
<span>
    <p align="center">
        <img src="doc/email-result-black.png" alt="email-result-black" width="40%"/>
        <img src="doc/email-result-white.png" alt="email-result-white" width="40%"/>
    <p>
</span>

<!-- Referencia https://raw.githubusercontent.com/othneildrew/Best-README-Template/master/README.md -->