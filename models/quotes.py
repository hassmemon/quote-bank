import database

def insert_quote(quote, quote_author, user_id):
    database.sql_write("INSERT into quotes (quote, quote_author, user_id) VALUES (%s, %s, %s);", [
        quote,
        quote_author,
        user_id
    ])

def get_quote(id):
    results = database.sql_select('SELECT * FROM quotes WHERE id = %s', [id])
    result = results[0]
    return result

def get_all_quotes():
    results = database.sql_select("SELECT quotes.*, users.name as user_name FROM quotes LEFT JOIN users ON quotes.user_id = users.id", [])
    return results

def get_user_id():
    results = database.sql_select("SELECT user_id FROM quotes", [])
    return results
##!!! NEED HELP ON THIS ONE!!

def get_user_quotes(user_id):
    results = database.sql_select("SELECT * FROM quotes WHERE user_id = %s", [user_id])
    return results

def update_quote(id, quote, quote_author):
    database.sql_write("UPDATE quotes set quote = %s, quote_author = %s WHERE id = %s", [
        quote,
        quote_author,
        id
    ])

def delete_quote(id):
    database.sql_write("DELETE FROM quotes WHERE id = %s", [id])