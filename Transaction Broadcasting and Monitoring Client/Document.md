Transaction Broadcasting and Monitoring Client Document


This document describes a Python client module for a mock stock price broadcast system. The module allows users to submit stock price data and track the status of the transaction.

Running the Script
    - python client.py

Transaction Status:
    - If successful (status code 200), the script will display the transaction hash and repeatedly check the transaction status using the check API endpoint (https://mock-node-wgqbnxruha-as.a.run.app/check/).
    - The script will continue checking until the transaction status is confirmed, failed, or "DNE" (does not exist).
    - For successful transactions, the script will display the confirmation message.
    - For failed transactions, the script will display the error message.
    - For non-existent transactions, the script will display an error message.

    Example:
        Input Sympol: AAPL
        Input Price: 150
        Status Code: 200
        Data sent successfully!
        Transaction Hash: abc123
        Transaction Status: PENDING
        Transaction Status: PENDING
        Transaction Status: CONFIRMED

