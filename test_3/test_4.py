import requests, json

user_list=[("diegovidal4","password","diegovidal4@gmail.com"),("diegovidal4","paword"),("diegovidal4","ssword"),("diegovidal4","passwor"),("diegovidal4","passw")]

def checkPortales(user_list):
    github_url = "https://api.github.com/user/repos"
    for user in user_list:
        data = json.dumps({'name':'test', 'description':'some test repo'})
        r = requests.post(github_url, data, auth=user
        if not r.status_code == requests.codes.ok:
            print "Credencial invalida"
            sendmail(user[2])
