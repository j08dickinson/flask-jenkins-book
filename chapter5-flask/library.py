from flask import Flask, jsonify, request
app = Flask(__name__)

library = {}
library['0312551371'] = {
	'name' : 'Enclave',
	'author' : 'Ann_Aguirre'
}

@app.route('/books', methods = ['POST'])
def checkin():
	if request.method == 'POST':
		data = request.get_json()
		library[data["isbn"]] = {
			'name' : data["name"],
			'author' : data["author"]}
		if data:
			return jsonify({"message": "Data received", "data": data}), 200
		else:
			return jsonify({"message": "No JSON data received"}), 400


@app.route('/books/<isbn>', methods = ['GET'])
def checkout(isbn):
	if isbn in library:
		checked = library[isbn]
		return jsonify({'data': checked}), 200
	else:
		checked = "Book not found"
		return jsonify({'data': checked}), 404


# driver function
if __name__ == '__main__':

    app.run(debug = True)
