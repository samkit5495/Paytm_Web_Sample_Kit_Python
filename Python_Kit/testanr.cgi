#!/usr/bin/python

import Checksum
import requests
import base64
import json
print "Content-type: text/html\n"
 
print "Hello, world!"
MERCHANT_KEY = 'kbzk1DSbJiV_O3p5';
data_dict = {
            'MID':'WorldP64425807474247',
            'ORDER_ID':'vidi45Dss4',
            'TXN_AMOUNT':'1',
            'CUST_ID':'acfff@paytm.com',
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'worldpressplg',
            'CHANNEL_ID':'WEB',
	    'THEME' : 'merchant',
	    'CALLBACK_URL':'http://localhost/pythonKit/response.cgi',
        }

#print data_dict;
param_dict = {}
checkSum = Checksum.generate_checksum(data_dict, MERCHANT_KEY)

param_dict['CHECKSUMHASH'] = checkSum
param_dict['ORDER_ID'] = data_dict['ORDER_ID']
param_dict['payt_STATUS'] = '1'

print json.dumps(param_dict, separators=(',', ':'))
