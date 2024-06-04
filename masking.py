import re

log = """
--- Request ---
**Time:** 2024-06-04T16:11:00Z
**Method:** GET
**URL:** /api/v1/products/98765
**Headers:**
  - Content-Type: application/json
  - Authorization: Bearer gibberish_auth_token_123

--- Response ---
**Status Code:** 200 OK
**Headers:**
  - Content-Type: application/json
  - Server: nginx/1.23.4

**Body:**
{
  "id": 98765,
  "name": "Mystery Widget",
  "description": "This widget does something mysterious. Couldn't make a call to 9888883330.",
  "price": 12.34
}

--- Request ---
**Time:** 2024-06-04T16:12:00Z
**Method:** POST
**URL:** /api/v1/orders
**Headers:**
  - Content-Type: application/json
  - Authorization: Bearer gibberish_auth_token_123

**Body:**
{
  "customer_id": "XX123-YYY456-ZZZ789",  **Simulated PII (customer ID)**
  "items": [
    { "product_id": 98765, "quantity": 2 }
  ]
}

--- Response ---
**Status Code:** 201 Created
**Headers:**
  - Location: /api/v1/orders/zyxwvutsr  **Simulated order ID**
  - Content-Type: application/json

**Body:**
{
  "id": "zyxwvutsr",  **Simulated order ID**
  "customer_id": "XX123-YYY456-ZZZ789",  **Simulated PII (customer ID)**
  "status": "pending",
  "total_price": 24.68,
  "message":"test@test.com is not found"
}

"""

mobile_number = re.findall(r'\bcall\s\bto\b\s(.*\d)', log)
print(mobile_number)
mobile_number_obscured = ["******" + mobile_number[0][6:10] for no in mobile_number]
print(mobile_number_obscured)

email = re.findall(r'\bmessage\":\"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', log)
obscured_email = [re.sub(r'[^@]', '*', em.split('@')[0]) + '@' + em.split('@')[1] for em in email]
print("Obscured Email:", obscured_email)

# Extracting the customer ID from the log
customer_id_pattern = r'\bcustomer_id\":\s\"([A-Z0-9-]+)\"'
customer_ids = re.findall(customer_id_pattern, log)

# Obscuring the customer ID (keeping only the last 4 characters visible)
obscured_customer_ids = ["****-****-****-" + cid[-4:] for cid in customer_ids]
print("Obscured Customer IDs:", obscured_customer_ids)

for original, obscured in zip(mobile_number, mobile_number_obscured):
    log = log.replace(original, obscured)

for original, obscured in zip(customer_ids, obscured_customer_ids):
    log = log.replace(original, obscured)

for original, obscured in zip(email, obscured_email):
    log = log.replace(original, obscured)

print(log)
