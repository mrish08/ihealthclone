from distutils.log import debug
from flask import Flask, render_template,request, redirect,flash, url_for, session, logging
import os
import psycopg2

app=Flask(__name__,template_folder='template',static_folder='static')
def connection():
    s = 'database-1.c8punsklsimv.ap-southeast-1.rds.amazonaws.com'
    d = 'bms' 
    u = 'postgres' 
    p = 'wew123WEW'
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
	clinic = []
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM ih_clinic_services")
	for row in cursor.fetchall():
		clinic.append({"clinic_services_id": row[0], "clinic_services_name": row[1]})
	conn.close()	
	return render_template("clinic.html", clinic = clinic)


@app.route("/addclinic", methods = ['POST'])
def addclinic():
	if request.method == 'POST':
		clinic_services_name = request.form['clinic_services_name']
	conn = connection()
	cursor = conn.cursor()
	cursor.execute('INSERT INTO ih_clinic_services (clinic_services_name)'' VALUES (%s)', [clinic_services_name])
	conn.commit()
	conn.close()
	return redirect('/clinic')


@app.route('/updateclinic/<int:clinic_services_id>', methods = ['GET', 'POST'])
def updateclinic(clinic_services_id):
	uc = []
	conn = connection()
	cursor = conn.cursor()
	if request.method == 'GET':
		cursor.execute("SELECT * FROM ih_clinic_services WHERE clinic_services_id = %s", (str(clinic_services_id)))
		for row in cursor.fetchall():
			uc.append({"clinic_services_id": row[0], "clinic_services_name": row[1]})
		conn.close()
		return render_template("updateclinic.html", clinic = uc[0])
	if request.method == 'POST':
		clinic_services_name = str(request.form["clinic_services_name"])
		cursor.execute("UPDATE clinic_services SET clinic_services_name = %s WHERE clinic_services_id = %s", (clinic_services_name, clinic_services_id))
		conn.commit()
		conn.close()
		return redirect('/clinic')



@app.route("/dental")
def dental():
	return render_template("clinic.html")


@app.route("/vaccination")
def vaccination():
	vaccination = []
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM ih_vaccine")
	for row in cursor.fetchall():
		vaccination.append({"vaccine_id": row[0], "vaccine_name": row[1], "lot_name": row[2], "brand_manufacturer": row[3]})
	conn.close()	
	return render_template("vaccination.html", vaccination = vaccination)

@app.route("/addvaccination", methods = ['POST'])
def addvaccination():
	if request.method == 'POST':
		vaccine_name = request.form['vaccine_name']
		lot_name = request.form['lot_name']
		brand_manufacturer = request.form['brand_manufacturer']
	conn = connection()
	cursor = conn.cursor()
	cursor.execute('INSERT INTO ih_vaccine (vaccine_name, lot_name, brand_manufacturer)'' VALUES (%s, %s, %s)', [vaccine_name, lot_name, brand_manufacturer])
	conn.commit()
	conn.close()
	return redirect('/vaccination')


@app.route('/updatevaccination/<int:vaccine_id>', methods = ['GET', 'POST'])
def updatevaccination(vaccine_id):
	uv = []
	conn = connection()
	cursor = conn.cursor()
	if request.method == 'GET':
		cursor.execute("SELECT * FROM ih_vaccine WHERE vaccine_id = %s", (str(vaccine_id)))
		for row in cursor.fetchall():
			uv.append({"vaccine_id": row[0], "vaccine_name": row[1], "lot_name": row[2], "brand_manufacturer": row[3] })
		conn.close()
		return render_template("updatevaccination.html", vaccination = uv[0])
	if request.method == 'POST':
		vaccine_name = str(request.form["vaccine_name"])
		lot_name = str(request.form["lot_name"])
		brand_manufacturer = str(request.form["brand_manufacturer"])
		cursor.execute("UPDATE vaccine SET (vaccine_name, lot_name, brand_manufacturer) = (%s,%s,%s)  WHERE vaccine_id =(%s)", (vaccine_name, lot_name, brand_manufacturer, vaccine_id))
		conn.commit()
		conn.close()
		return redirect('/vaccination')

@app.route("/schedule")
def schedule():
	return render_template("schedule.html")



@app.route("/addschedule", methods = ['GET', 'POST'])
def addschedule():
	return redirect('/schedule')


@app.route('/updateschedule/<int:clinic_sched_id>', methods = ['GET', 'POST'])
def updateschedule(clinic_sched_id):
		return redirect('/schedule')


@app.route("/medicine")
def medicine():
	return render_template("medicine.html")
	
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

@app.route("/indexstaff")
def indexstaff():
	return render_template("indexstaff.html")

@app.route("/schedulestaff")
def schedulestaff():
	return render_template("schedulestaff.html")

@app.route("/clinicstaff")
def clinicstaff():
	clinicstaff = []
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM ih_appointment")
	for row in cursor.fetchall():
		clinicstaff.append({"appt_id": row[0], "appt_type": row[1],"remarks": row[2],"date": row[3],"time": row[4],"status": row[5]})
	conn.close()	
	return render_template("clinicstaff.html", clinicstaff = clinicstaff)

@app.route("/medicinestaff")
def medicinestaff():
	return render_template("medicinestaff.html")

@app.route("/vaccinationstaff")
def vaccinationstaff():
	vaccinationstaff = []
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM ih_appointment")
	for row in cursor.fetchall():
		vaccinationstaff.append({"appt_id": row[0], "appt_type": row[1],"remarks": row[2],"date": row[3],"time": row[4],"status": row[5]})
	conn.close()	
	return render_template("vaccinationstaff.html", vaccinationstaff = vaccinationstaff)


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