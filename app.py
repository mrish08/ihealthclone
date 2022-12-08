from distutils.log import debug
from flask import Flask, render_template,request, redirect,flash, url_for, session, logging
import os
import psycopg2

app=Flask(__name__,template_folder='template',static_folder='static')
def connection():
    s = 'localhost'
    d = 'iHealth_database' 
    u = 'postgres' 
    p = '123'
    conn = psycopg2.connect(host=s, user=u, password=p, database=d)
    with conn:
        with conn.cursor() as curs:
            curs.execute
    return conn


@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/clinic")
def clinic():
	return render_template("clinic.html", clinic = clinic)


@app.route("/addclinic", methods = ['POST'])
def addclinic():
	return redirect('/clinic')


@app.route('/updateclinic/<int:clinic_services_id>', methods = ['GET', 'POST'])
def updateclinic(clinic_services_id):
		return redirect('/clinic')


@app.route("/dental")
def dental():
	return render_template("clinic.html", dental = dental)


@app.route("/vaccination")
def vaccination():
	return render_template("vaccination.html", vaccination = vaccination)

@app.route("/addvaccination", methods = ['POST'])
def addvaccination():
	return redirect('/vaccination')


@app.route('/updatevaccination/<int:vaccine_id>', methods = ['GET', 'POST'])
def updatevaccination(vaccine_id):
		return redirect('/vaccination')


@app.route("/schedule")
def schedule():
	return render_template("schedule.html", schedule = schedule)



@app.route("/addschedule", methods = ['GET', 'POST'])
def addschedule():
	return redirect('/schedule')


@app.route('/updateschedule/<int:clinic_sched_id>', methods = ['GET', 'POST'])
def updateschedule(clinic_sched_id):
		return redirect('/schedule')


@app.route("/medicine")
def medicine():
	return render_template("medicine.html", medicine = medicine)
	
@app.route("/addmedicine", methods = ['GET', 'POST'])
def addmedicine():
	return redirect('/medicine')

@app.route('/updatemedicine/<int:medicine_id>', methods = ['GET', 'POST'])
def updatemedicine(medicine_id):
		return redirect('/medicine')

@app.route("/loginadmin") 
def loginadmin():
	return render_template("loginadmin.html")

@app.route("/loginstaff")
def loginstaff():
	return render_template("loginstaff.html")

@app.route("/loginresident")
def loginresident():
	return render_template("loginresident.html")

@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/indexstaff")
def indexstaff():
	return render_template("indexstaff.html")

@app.route("/schedulestaff")
def schedulestaff():
	return render_template("schedulestaff.html")

@app.route("/clinicstaff")
def clinicstaff():
	return render_template("clinicstaff.html")

@app.route("/medicinestaff")
def medicinestaff():
	return render_template("medicinestaff.html")

@app.route("/vaccinationstaff")
def vaccinationstaff():
	return render_template("vaccinationstaff.html")

@app.route("/dentalstaff")
def dentalstaff():
	return render_template("dentalstaff.html")

@app.route("/indexresident")
def indexresident():
	return render_template("indexresident.html")

@app.route("/scheduleresident")
def scheduleresident():
	return render_template("scheduleresident.html")

@app.route("/dentalresident")
def dentalresident():
	return render_template("dentalresident.html")

@app.route("/vaccinationresident")
def vaccinationresident():
	return render_template("vaccinationresident.html")

@app.route("/clinicresident")
def clinicresident():
	return render_template("clinicresident.html")

@app.route("/medicineresident")
def medicineresident():
	return render_template("medicineresident.html")

if __name__== '__main__':
 app.debug=True
 app.run(debug=True)