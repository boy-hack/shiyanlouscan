#!/usr/bin/env python
# __author__= 'w8ay'
import re
from lib.core import outputer
output = outputer.outputer()

class spider:
    def run(self,url,html):
        #print(html)
        pattern = re.compile(r'([\w-]+@[\w-]+\.[\w-]+)+')
        email_list = re.findall(pattern, html)
        if(email_list):
            print(email_list)
            for email in email_list:
                output.add_list("email",email)
            return True
        return False