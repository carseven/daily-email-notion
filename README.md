
    
<h2 style="
    text-align: center;
    font-weight:200;
    font-size: 28px;
    text-transform: uppercase;
">Daily e-mail from notion database</h2>
<p align="center">
    <img width="40%" src="doc/logo.png"/>
</p>

Add lincense icon and linkedin icon

## Table of contents
<!-- <summary>Table of Contents</summary> -->
<ol>
    <li>
        <a href="#about-the-project">About the project</a>
    </li>
    <li>
        <a href="#configuration">Configuration</a>
        <ul>
            <li><a href="#installing-dependencies">Installing dependencies</a></li>
            <li><a href="#installation">Notion configuration</a></li>
            <li><a href="#tokens-secret-file">Tokens secret file</a></li>
            <li><a href="#github-action">Github action</a></li>
        </ul>
    </li>
    <li>
        <a href="#usage-and-personalization">Usage and presonalization</a>
        <ul>
            <li><a href="#installing-dependencies">Installing dependencies</a></li>
            <li><a href="#notion-api-query">Notion api query</a></li>
            <li><a href="#email-personalization">Email personalization</a></li>
        </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#references">References</a></li>
</ol>

## About The Project
Explicar las funcionalidades que se han añadido y explicar el sistema de notion. Hacer referencia al video de 
<span>
    <p align="center">
        <img src="doc/email-result-black.png" alt="email-result-black" width="40%"/>
        <img src="doc/email-result-white.png" alt="email-result-white" width="40%"/>
    <p>
</span>
## Configuration

### Installing dependencies
Update pip:
```sh
python -m pip install --upgrade pip
```

Install dependencias via pip:
```sh
pip install requests python-dateutil
```
### Notion configuration
1. Created notion integration
2. Invite integration
    * ⚠ Warning: Also relation databases, to have access to their information
3. Get database id from url
### Tokens secret file
Generated ```dailyEmail/tokens.py``` file with ```SECRET``` dictionary with the sensible information.

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
### Github action
1. Codificar con base64
2. Como decodificar y como añadir el secreto tokens.py
3. Como editar cada cuando se lanza el email

## Usage and personalization

### Notion api query

### Email personalization

***Table information:***
By default the email table will print all the columns/properties from the notion database. If we need just to print some of the columns set the ```dbProperties``` list with the name of the columns we want to print.

Be aware of the order, beacause it will be use the order from the list. We could re-order the list if we want.
```python
dbProperties = ['State', 'Task', 'Api-projects', 'Due', 'Kanban - State', 'Priority', 'Type']
```

***Style:***
If we want to change the style of the table you could modify the style string from ```dailyEmail/html.py```. In my case, I use the following tutorial as a  [reference](https://dev.to/dcodeyt/creating-beautiful-html-tables-with-css-428l)


## Contributing
## Contact
## References
<!-- Referencia https://raw.githubusercontent.com/othneildrew/Best-README-Template/master/README.md -->