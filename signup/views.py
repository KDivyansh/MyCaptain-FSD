from django.shortcuts import render

import mysql.connector as sql

first_name = ""
last_name = ""
gender = ""
dob = "" #dd/mm/yyyy
email = ""
pwd = ""

def signup_action(request):
    global first_name,last_name,gender,dob,email,pwd
    if request.method  == "POST":
        m = sql.connect(host="localhost",user="root",passwd="divyansh26",database = "website")
        cursor = m.cursor()
        d = request.POST
        for k,v in d.items():
            if k == "first_name":
                first_name = v
            if k == "last_name":
                last_name = v
            if k == "gender":
                gender = v
            if k == "dob":
                dob = v
            if k == "email":
                email = v
            if k == "password":
                pwd = v
        c = "insert into users values('{}','{}','{}','{}','{}','{}')".format(first_name,last_name,gender,dob,email,pwd)

        cursor.execute(c)
        m.commit()
    return render(request, 'signup/signup_page.html')