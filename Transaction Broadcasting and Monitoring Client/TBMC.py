import requests
import json
import time

url = "https://mock-node-wgqbnxruha-as.a.run.app/broadcast"
url_check = "https://mock-node-wgqbnxruha-as.a.run.app/check/"

current_time_seconds = int(time.time())

symbol_input = input("Input Sympol: ")
price_input = int(input("Input Price: "))

data = {
    "symbol": symbol_input,
    "price": price_input,
    "timestamp": current_time_seconds, 
}

payload = json.dumps(data)

response = requests.post(url, headers={"Content-Type": "application/json"}, data=payload)

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    response_data = response.json()
    print("Data sent successfully!")
    tx_hash = response_data['tx_hash']
    print("Transaction Hash:", tx_hash)

    while True:
      check_url = url_check + tx_hash

      check_response = requests.get(check_url)

      if check_response.status_code == 200:
        status_data = check_response.text
        data = json.loads(status_data)
        print("Transaction Status:", data["tx_status"])

        if data["tx_status"] in ["CONFIRMED", "FAILED", "DNE"]:
          break

        time.sleep(3)
    else:
      print("Error: Transaction hash not found in response.")
else:
    print(f"Error sending data: {response.text}")
