from django.shortcuts import render
import mysql.connector as sql

first_name = ""
last_name = ""
gender = ""
dob = "" #dd/mm/yyyy
email = ""
pwd = ""

def login_action(request):
    global email,pwd
    if request.method == "POST":
        m = sql.connect(host="localhost",user="root",passwd="divyansh26",database = "website")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                email = value
            if key == "password":
                pwd = value
        c = "select * from users where email = '{}' and password = '{}' ".format(email,pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request,'myapp/error.html')
            # print("Error")
        else:
            return render(request,'myapp/welcome.html',{
                'first_name' : t[0][0] , 'last_name': t[0][1]
            })
            # print("Logged In")
    
    return render(request, 'myapp/login_page.html')