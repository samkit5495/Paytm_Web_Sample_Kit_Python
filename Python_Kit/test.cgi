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
	    #'CALLBACK_URL':'http://localhost/pythonKit/response.cgi',
        }

print data_dict;
param_dict = data_dict  
param_dict['CHECKSUMHASH'] =Checksum.generate_checksum(data_dict, MERCHANT_KEY)

print param_dict;

for key in param_dict:
    print key.strip()+param_dict[key].strip()

print '<h1>Merchant Check Out Page</h1></br>'
print '<form method="post" action="https://pguat.paytm.com/oltp-web/processTransaction" name="f1">'
print '<table border="1">'
print '<tbody>'
for key in param_dict:
    print '<input type="hidden" name="'+key.strip()+'"value="'+param_dict[key].strip()+'">'
print '</tbody>'
print '</table>'
print '<script type="text/javascript">'
#print 'document.f1.submit();'
print '</script>'
print '</form>'


