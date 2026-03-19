#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

# -----------------------------
# Create Flask app
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Updated in-memory "database"
# -----------------------------
contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]

customers = ["bob", "bill", "john", "sarah"]  # Sensitive info not returned

# -----------------------------
# Route: /contract/<id>
# -----------------------------
@app.route("/contract/<int:contract_id>", methods=["GET"])
def get_contract(contract_id):
    # Find contract by id
    contract = next((c for c in contracts if c["id"] == contract_id), None)
    if contract:
        # 200 OK with contract info
        return contract, 200
    else:
        # 404 Not Found
        return make_response({"error": "Contract not found"}, 404)

# -----------------------------
# Route: /customer/<customer_name>
# -----------------------------

@app.route("/customer/<customer_name>", methods=["GET"])
def get_customer(customer_name):
    name_lower = customer_name.lower()
    if name_lower in customers:
        return f"Customer {customer_name} exists!", 200
    else:
        return make_response({"error": "Customer not found"}, 404)

# -----------------------------
# Optional root route
# -----------------------------
@app.route("/", methods=["GET"])
def home():
    return "Contracts API is running!"

# -----------------------------
# Run the app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5555)
