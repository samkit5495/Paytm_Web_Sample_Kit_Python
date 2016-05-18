# Introduction
This sample kit is ready to be deployed and tested.

# Instructions
 1. Copy the *pythonKit* folder(according to your python version) into the root folder of your server (like /var/www/html)
 2. **Mandatory Step**: For each test transaction, please change the value of the parameter "ORDER_ID" in the test.cgi file.

# Usage Description
The *pythonKit* folder has the following files:
 1. CheckSum.py – This file has the logic for checksum generation and verification.
 2. test.cgi – This file will initiate the sample test transaction through the Paytm gateway. Paytm parameters need to be added in this file.
 3. response.cgi – This file has the logic for processing PG response after the transaction processing.
