
#!/usr/bin/env python3

from flask import Flask,request,current_app,g, make_response

# -----------------------------
# Create Flask app
# -----------------------------
app = Flask(__name__)

# -----------------------------
# In-memory "database"
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
@app.route("/contract/<int:id>", methods=["GET"])
def get_contract(id):
    # Look for contract by id
    contract = next((c for c in contracts if c["id"] == id), None)
    if contract:
        # Contract found → 200 with contract information only
        return contract["contract_information"], 200
    else:
        # Contract not found → 404
        return make_response({"error": "Contract not found"}, 404)

# -----------------------------
# Route: /customer/<customer_name>
# -----------------------------
@app.route("/customer/<customer_name>", methods=["GET"])
@app.route("/customer/<customer_name>/", methods=["GET"])  # optional trailing slash
def get_customer(customer_name):
    # Check if customer exists
    if customer_name.lower() in customers:
        # Customer found → 204 No Content, empty body
        return "", 204
    else:
        # Customer not found → 404
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
