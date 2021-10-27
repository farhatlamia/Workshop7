import subprocess
import os
import simplejson as json

#command = "cd Downloads; cd ML-CODE; find . | xargs bandit -f json"
path = './ML-CODE'
os.chdir(path)

command = "find . | xargs bandit -f json"
ret = subprocess.run(command, capture_output=True, shell=True)
x = ret.stdout.decode()
#print(x)

main_list = json.loads(x)
result= main_list["results"]
print(result)

mylist = []

for i in result:
    temp= {}
    temp["FILE"] = path+ i["filename"]
    alerts = {}
    alerts["SEVERITY"] = i["issue_severity"]
    alerts["CONFIDENCE"]= i["issue_confidence"]
    alerts["NAME"]= i["test_name"]
    alerts["LINE_NO"]= i["line_number"]
    temp["ALERTS"] = alerts
    mylist.append(temp)

with open("sample.json", "w") as fhandle:
    json.dump(mylist, fhandle, indent=4)





