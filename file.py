import re
import csv
import operator

per_error = {}
per_user = {}
per_info = {}
with open('syslog.log','r') as log:
  line = log.readlines()
  for l in line :
    if  re.search(r"ticky: ERROR ([\w ]*)", l) is not None:
      e=re.search(r"ticky: ERROR ([\w ]*)", l).group(1)
      if(e not in per_error.keys()):
        per_error[e]=1
      else:
        per_error[e]+=1
      if   re.search(r"(\([\w]*\))$", l) is not None:
        user= re.search(r"(\([\w]*\))$", l).group(1)[1:-1]
        if user not in per_user.keys():
            per_user[user] = 1
        else
            per_user[user] +=1
    if  re.search(r"ticky: INFO ([\w ]*)", l) is not None:
         if   re.search(r"(\([\w]*\))$", l) is not None:
           user= re.search(r"(\([\w]*\))$", l).group(1)[1:-1]
           if user not in per_info.keys():
               per_info[user] = 1
           else
               per_info[user] +=1


with open('error_message.csv','w',newline='') as e:
    fieldnames = ['Error', 'Count']
    writer = csv.DictWriter(e, fieldnames=fieldnames)
    writer.writeheader()

    for key,value in per_error.enumerate():
        writer.writerow({'Error': key, 'Count': value})

with open('user_statistics.csv','w',newline='') as e:
    fieldnames = ['Username', 'INFO','ERROR']
    writer = csv.DictWriter(e, fieldnames=fieldnames)
    writer.writeheader()

    for key in per_user.keys():
        if key in per_info.keys():
            in = per_info[key]
        else:
            in =0
        if key in per_user.keys():
            out = per_user[key]
        else:
            out =0
        writer.writerow({'Username': key, 'INFO': in , 'ERROR' : out})
