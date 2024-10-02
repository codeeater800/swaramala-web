from flask import Blueprint, request, jsonify, render_template
from .search import simple_search, complex_search, load_dictionary

main = Blueprint('main', __name__)

# Load dictionary on startup
dictionary = load_dictionary()

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        search_type = request.form.get('search_type')
        position = request.form.get('position')

        if search_type == 'starts_with':
            results, count = simple_search(search_term, dictionary)
        elif search_type == 'ends_with':
            results = complex_search(search_term, search_type='end')
        elif search_type == 'select_position' and position:
            results = complex_search(search_term, position=int(position), search_type='position')

        return jsonify(results=results)

    return render_template('index.html')
