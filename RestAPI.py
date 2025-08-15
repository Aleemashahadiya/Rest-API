from flask import Flask, jsonify, request
app = Flask(__name__)
smartphones = [{"id": 1, "brand": "Apple", "model": "iPhone 14", "price": 130000},
    {"id": 2, "brand": "Oneplus", "model": "OnePlus 11", "price": 30000}]
@app.route('/smartphones',methods=['GET'])
def get_smartphones():
    return jsonify(smartphones)

@app.route('/smartphones/<int:id>',methods=['GET'])
def get_smartphonesbyID(id):
    phone = next((item for item in smartphones if item["id"]== id),None)
    if phone:
        return jsonify(phone)
    return jsonify({"message":"smartphones not found"}),404


# Create a smartphone
@app.route('/smartphones', methods=['POST'])
def add_smartphone():
    data = request.get_json()
    if not data or "brand" not in data or "model" not in data or "price" not in data:
        return jsonify({"message": "Invalid Data"}), 400

    new_id = max((phone["id"] for phone in smartphones), default=0) + 1
    new_phone = {"id": new_id, **data}
    smartphones.append(new_phone)
    return jsonify(new_phone), 201


# Update a smartphone
@app.route('/smartphones/<int:id>', methods=['PUT'])
def update_smartphone(id):
    data = request.get_json()
    phone = next((item for item in smartphones if item["id"] == id), None)
    if not phone:
        return jsonify({"message": "smartphone not found"}), 404
    phone.update(data)
    return jsonify(phone)



@app.route('/smartphones/<int:id>', methods=['DELETE'])
def delete_smartphone(id):
    global smartphones
    smartphones = [phone for phone in smartphones if phone["id"] != id]
    return jsonify({"message": "smartphone deleted successfully"}), 200

if __name__=="__main__":
    app.run(debug=True)