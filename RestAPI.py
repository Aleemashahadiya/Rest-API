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

# @app.route('/smartphones/create',methods=['POST'])
# def add_smartphones():
#     data=request.get_json()
#     if not data or "brand" not in data or "price" not in data or "model" not in data:
#         return jsonify({"message":"Invalid Data"}),400

#     new_id=max((phone["id"] for phone in smartphones)) +1 if smartphones else 1
#     new_phone={"id":new_id,**data}
#     smartphones.append(new_phone)
#     return jsonify(smartphones),201

@app.route('/smartphones/create')
def add_smartphones():
    brand = request.args.get("brand")
    model = request.args.get("model")
    price = request.args.get("price", type=int)

    if not brand or not model or not price:
        return jsonify({"message": "Invalid Data"}), 400

    new_id = max((phone["id"] for phone in smartphones), default=0) + 1
    new_phone = {"id": new_id, "brand": brand, "model": model, "price": price}
    smartphones.append(new_phone)
    return jsonify(smartphones), 201



# @app.route('/smartphones/update/<int:id>',methods=['PUT'])
# def update_smartphones(id):
#     data=request.get_json()
#     phone = next((item for item in smartphones if item["id"] == id),None)
#     if not phone:
#          return jsonify({"message":"smartphones not found"}),400
#     phone.update(data)
#     return jsonify(phone)


@app.route('/smartphones/update/<int:id>')
def update_smartphones(id):
    brand = request.args.get("brand")
    model = request.args.get("model")
    price = request.args.get("price", type=int)

    phone = next((item for item in smartphones if item["id"] == id), None)
    if not phone:
        return jsonify({"message": "smartphone not found"}), 404

    if brand:
        phone["brand"] = brand
    if model:
        phone["model"] = model
    if price:
        phone["price"] = price

    return jsonify({"message": "smartphone updated", "data": phone})


@app.route('/smartphones/delete/<int:id>')
def delete_smartphones(id):
    global smartphones
    smartphones=[phone for phone in smartphones if phone["id"]!=id]
    return jsonify({"message":"smartphones Deleted successfully"}),200

if __name__=="__main__":
    app.run(debug=True)