from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for initial tourist places
places = [
    {"id": 1, "name": "Eiffel Tower", "location": "Paris"},
    {"id": 2, "name": "Statue of Liberty", "location": "New York"},
    {"id": 3, "name": "Taj Mahal", "location": "Agra"}
]

@app.route('/')
def index():
    return render_template('index.html', places=places)

@app.route('/add', methods=['GET', 'POST'])
def add_place():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        places.append({"id": len(places) + 1, "name": name, "location": location})
        return redirect(url_for('index'))
    return render_template('add_place.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_place(id):
    place = next((p for p in places if p['id'] == id), None)
    if request.method == 'POST':
        place['name'] = request.form['name']
        place['location'] = request.form['location']
        return redirect(url_for('index'))
    return render_template('edit_place.html', place=place)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_place(id):
    global places
    places = [p for p in places if p['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
