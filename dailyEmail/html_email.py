def html_table_column(lista_titulos):
    yield "\t    <tr>"
    for columna in lista_titulos:
        yield f"\t\t<th>{columna}</th>"
    yield "\t    </tr>\n"


def html_table_row(lista_filas, lista_columns):
    for fila in lista_filas:
        yield "\t    <tr>"
        for columna in lista_columns:
            if columna not in fila:
                fila[columna] = ""
            if columna in fila and columna == 'Task':
                href = "href=\"" + fila['url'] + "\""
                yield f"\t\t<td><a {href}>{fila[columna]}</a></td>"
            else:
                yield f"\t\t<td>{fila[columna]}</td>"
        yield "\t    </tr>"


def construct_html_table(columnas, filas):
    return '<table class="styled-table">\n' + columnas + filas + "\n\t</table>"


def construct_html_msg(table, style, quote):
    html_template = f"""\
<html>
    <head>
    <style>
{style}
    </style>
    </head>
    <body>
        <h1>Tareas del dia ✅</h1>
        {table}
        <h1>Frase del dia 🧠</h1>
        {quote}
    </body>
</html>
"""
    return html_template


# Reference https://dev.to/dcodeyt/creating-beautiful-html-tables-with-css-428l
style = """\
        .styled-table {
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 0.9em;
            font-family: sans-serif;
            min-width: 400px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        }

        .styled-table thead tr {
            background-color: #009879;
            color: #ffffff;
            text-align: left;
        }

        .styled-table th,
        .styled-table td {
            padding: 12px 15px;
        }

        .styled-table tbody tr {
            border-bottom: 1px solid #dddddd;
        }

        .styled-table tbody tr:nth-of-type(even) {
            background-color: #f3f3f3;
        }

        .styled-table tbody tr:last-of-type {
            border-bottom: 2px solid #009879;
        }

        .styled-table tbody tr.active-row {
            font-weight: bold;
            color: #009879;
        }

        h1 {
            color: #009879;
            font-family: arial, sans-serif;
            font-size: 16px;
            font-weight: bold;
            margin-top: 0px;
            margin-bottom: 1px;
        }
"""


def quote_html(author, quote):
    quote_html = f"""\
<div>
    <blockquote>
        <p>{quote}</p>
        <cite>{author}</cite>
    </blockquote>
</div>
"""
    return quote_html
