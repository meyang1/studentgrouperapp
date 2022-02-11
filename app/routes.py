from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory, safe_join, abort
from app import app, classClass
import os
import pandas as pd
import xlwt
 
headings = ("Row Number", "Student 1", "Student 2")

@app.route('/')
@app.route('/index')
def index():  
    # Creates a default class on startup
    myClass = classClass.Class()
    myClass.loadFromFile("app\static\excel\\0a52730597fb4ffa01fc117d9e71e3a9.xlsx")
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    myClass.loadFromFile(files)
    data = myClass.getNames()

    #return render_template('index.html', title='Student Grouper Main', data=data, extra=str(myClass.getNames()))   
    return render_template('index.html', title='Student Grouper', headings=headings)
     
    



# Gets a file from the user using a form
@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method=="POST": 
        upload_excel=request.files['upload_excel']
        if upload_excel.filename != '':
            # Gets file and updates data
            filepath=os.path.join(app.config["UPLOAD_FOLDER"], upload_excel.filename)
            upload_excel.save(filepath)
            myClass = classClass.Class()
            myClass.loadFromFile("app\static\excel\\" + upload_excel.filename)
            files = os.listdir(app.config['UPLOAD_FOLDER'])
            #myClass.loadFromFile(files)
            #myClass.loadFromFile("app\static\excel\\"+files[0])
            data = myClass.getNames()
        print(data)
        # Refreshes files to prevent them from saving in code for now
        if os.path.exists("app\static\excel\\" + upload_excel.filename):
            os.remove("app\static\excel\\" + upload_excel.filename)
    
    exportFile = Workbook() 
    sheet1 = exportFile.add_sheet('Sheet 1')
    countGroup = 0
    countName = 0 
    # Manual input (add for groups later)
    sheet1.write(countGroup, 0, "Groups")
    sheet1.write(countGroup, 1, "Partner 1")
    sheet1.write(countGroup, 2, "Partner 2")

    # Adds people into groups with numbers
    for group in data:
        for name in group:
            n=str(name)
            space = " "  
            sheet1.write(countGroup+1, countName, n+space)
            countName+=1
        countGroup+=1
        countName=0
    
    newFileName = "group_" + upload_excel.filename[0:(len(upload_excel.filename)-5)] + ".xls"
    exportFile.save("app\static\\" + newFileName )
    #return render_template('index.html', title='Student Grouper Main', headings=headings)
    #return render_template('index.html')
    #return url_for('index')
    return render_template('index.html', title='Student Grouper', data=data, extra=data)   

"""
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
"""
