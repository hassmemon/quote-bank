from email.quoprimime import quote
from flask import Blueprint, request, session, redirect, render_template
# from models.quotes import get_all_quotes, delete_quote
from models.quotes import delete_quote, get_all_quotes, get_quote, insert_quote, update_quote, get_user_quotes, get_user_id
from models.user import get_user_by_id

quotes_controller = Blueprint("quotes_controller", __name__, template_folder="../templates/quotes")

@quotes_controller.route('/quotes', methods=["GET"])
def quotes():
    user_id = session.get('user_id')
    my_quotes = get_user_quotes(user_id)
    
    return render_template('main.html', my_quotes = my_quotes)

@quotes_controller.route('/quotes/show', methods=["GET"])
def show_all_quotes():
    all_quotes = get_all_quotes()
    # id = 'user_id'
    
    # !!!!NEED HELP HERE!!!
    return render_template('show.html', all_quotes = all_quotes)

@quotes_controller.route('/quotes/create')
def create():
    if not session.get('user_id'):
        return redirect('/login')
    return render_template('create.html')
        
@quotes_controller.route('/quotes', methods=["POST"])
def insert():
    if not session.get('user_id'):
        return redirect('/login')
    user_id = session.get('user_id')
    insert_quote(
        request.form.get("quote"),
        request.form.get("quote_author"),
        user_id
    )
    return redirect('/')

@quotes_controller.route('/quotes/<id>')
def show(id):
    quote = get_quote(id)
    return render_template('show.html', quote=quote)

@quotes_controller.route('/quotes/<id>/edit')
def edit(id):
    if not session.get('user_id'):
        return redirect('/login')
    quote = get_quote(id)
    # user = get_user(session.get('user_id'))
    return render_template('edit.html', quote=quote, user_id = session.get('user_id'))

@quotes_controller.route('/quotes/<id>', methods=["POST"])
def update(id):
    if not session.get('user_id'):
        return redirect('/login')
    quote = request.form.get("quote")
    quote_author = request.form.get("quote_author")
    print(id)
    update_quote(id, quote, quote_author)
   

    return redirect('/')

@quotes_controller.route('/quotes/<id>/delete')
def delete(id):
    if not session.get('user_id'):
        return redirect('/login')
    delete_quote(id)
    return redirect('/')