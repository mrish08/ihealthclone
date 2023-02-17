from distutils.log import debug
from flask import Flask, render_template,request, redirect, session,Response, jsonify
from flask_session import Session
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import datetime
from io import StringIO
import requests
import urllib.parse

app=Flask(__name__,template_folder='template',static_folder='static')
#app.secret_key = 'abandonware-invokes'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
#'https://back-final.brgyit-bot.com/api/v1/
Session(app)
  

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
"""""
@app.route("/")
def authLogins():
	token = session.get('token')
	with requests.Session() as session:
		session.headers['Authorization'] = f'Bearer {token}'
		response = session.get('https://back-final.brgyit-bot.com/api/v1/')
		data = response.json()
		print (data)
		return print
		#return redirect('/success', data=data)

@app.route("/authLogin",methods=['GET'])
def authLogin():
	if request.method=='GET':
		token = request.args.get('token')
		print (token)
		conn = connection() 
		cursor= conn.cursor()
		cursor.execute("SELECT id, user_id FROM ihealth_session_ihealthsession WHERE token = %s AND expiration_date > now()", (urllib.parse.unquote_plus(token),))		
		row = cursor.fetchone()
		if row == None:
			print("There are no results for this query")
			# redirect nyo sa login page ng bitbo
			return urllib.parse.unquote_plus(token) #temporary lang itong return na ito, dapat redirect papunta sa login page ng bitbo
		else:
			conn_user = connection() 
			cursor_user = conn_user.cursor()
			cursor_user.execute("SELECT * FROM users_user WHERE id = %s", (str(row[1]),))
			row_user = cursor_user.fetchone()
			if row_user == None:
				# no user found
				print("There are no results for this query")
				# redirect nyo sa login page ng bitbo
				return "No User found" #temporary lang itong return na ito, dapat redirect papunta sa login page ng bitbo
			else:
				session['row_user']=row_user
				return session
				
				# create session for user where you will be saving the records
				# redirect to index
"""

@app.route("/index")
def index():
	email= "admin@email.com" 
	account_type= "Admin"
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT id,firstname FROM users_user WHERE email = %s AND account_type = %s", (email, account_type))
	user = cursor.fetchone()
	if user is not None:
		user_id, user_firstname = user
		session['user_id'] = user_id
		session['user_firstname'] = user_firstname
	return render_template("index.html")

@app.route("/clinic")
def clinic():
	if('user_id' in session):
		clinic = []
		conn = connection()
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM ih_clinic_services")
		for row in cursor.fetchall():
			clinic.append({"clinic_services_id": row[0], "clinic_services_name": row[1]})
		conn.close()	
		return render_template("clinic.html", clinic = clinic)

@app.route("/adcb")
def adcb():
	return render_template("admin-add-clinicservice.html")

@app.route("/addclinic")
def addclinic():
	if('user_id' in session):
		if request.method == 'POST':
			clinic_services_name = request.form['clinic_services_name']
		conn = connection()
		cursor = conn.cursor()
		cursor.execute('INSERT INTO ih_clinic_services (clinic_services_name)'' VALUES (%s)', [clinic_services_name])
		conn.commit()
		conn.close()
		return render_template("/clinic")

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
		return render_template("updateclinicadmin.html", clinic = uc[0])
	if request.method == 'POST':
		clinic_services_name = str(request.form["clinic_services_name"])
		cursor.execute("UPDATE ih_clinic_services SET clinic_services_name = %s WHERE clinic_services_id = %s", (clinic_services_name, clinic_services_id))
		conn.commit()
		conn.close()
		return redirect('/clinic')

@app.route("/dental")
def dental():
	return render_template("clinic.html")

@app.route("/adminvaccineinv")
def vaccination():
	vaccination = []
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM ih_vaccine")
	for row in cursor.fetchall():
		vaccination.append({"vax_id": row[0], "vax_name": row[1], "vax_brand_manufacturer": row[2], "vax_batch_no": row[3], "vax_lot_no": row[4], "vax_dosage": row[5], "vax_tech_platform": row[6], "vax_ph_fda_approval": row[7], "vax_storage_req": row[8], "vax_efficiency": row[9], "vax_side_effect": row[10],"stock": row[11]})
	conn.close()	
	return render_template("adminvaccineinv.html", vaccination = vaccination)

@app.route("/addvaccination", methods = ['POST'])
def addvaccination():
	if request.method == 'POST':
		vax_name = request.form['vax_name']
		vax_brand_manufacturer = request.form['vax_brand_manufacturer']
		vax_batch_no = request.form['vax_batch_no']
		vax_lot_no = request.form['vax_lot_no']
		vax_dosage  = request.form['vax_dosage']
		vax_tech_platform = request.form['vax_tech_platform']
		vax_ph_fda_approval = request.form['vax_ph_fda_approval']
		vax_storage_req  = request.form['vax_storage_req']
		vax_efficiency  = request.form['vax_efficiency']
		vax_side_effect  = request.form['vax_side_effect']
		stock  = request.form['stock']
	conn = connection()
	cursor = conn.cursor()
	cursor.execute('INSERT INTO ih_vaccine (vax_name, vax_brand_manufacturer, vax_batch_no, vax_lot_no, vax_dosage, vax_tech_platform, vax_ph_fda_approval, vax_storage_req, vax_efficiency, vax_side_effect, stock)'' VALUES (%s,%s,%s,%s, %s, %s, %s, %s, %s,%s, %s)', 
	[ vax_name, vax_brand_manufacturer, vax_batch_no, vax_lot_no, vax_dosage, vax_tech_platform, vax_ph_fda_approval, vax_storage_req, vax_efficiency, vax_side_effect, stock])
	conn.commit()
	conn.close()
	return redirect('/adminvaccineinv')

@app.route('/updatevaccination/<int:vax_id>', methods = ['GET', 'POST'])
def updatevaccination(vax_id):
	uv = []
	conn = connection()
	cursor = conn.cursor()
	if request.method == 'GET':
		cursor.execute("SELECT * FROM ih_vaccine WHERE vax_id = %s", (str(vax_id)))
		for row in cursor.fetchall():
			uv.append({"vax_id": row[0], "vax_name": row[1], "vax_brand_manufacturer": row[2], "vax_batch_no": row[3], "vax_lot_no": row[4], "vax_dosage": row[5], "vax_tech_platform": row[6], "vax_ph_fda_approval": row[7], "vax_storage_req": row[8], "vax_efficiency": row[9], "vax_side_effect": row[10],"stock": row[11]})
		conn.close()
		return render_template("updatevaccination.html", vaccination = uv[0])
	if request.method == 'POST':
		vax_name = str(request.form['vax_name'])
		vax_brand_manufacturer = str(request.form['vax_brand_manufacturer'])
		vax_batch_no = str(request.form['vax_batch_no'])
		vax_lot_no = str(request.form['vax_lot_no'])
		vax_dosage = str(request.form['vax_dosage'])
		vax_tech_platform = str(request.form['vax_tech_platform'])
		vax_ph_fda_approval = str(request.form['vax_ph_fda_approval'])
		vax_storage_req = str(request.form['vax_storage_req'])
		vax_efficiency = str(request.form['vax_efficiency'])
		vax_side_effect = str(request.form['vax_side_effect'])
		stock  = int(request.form['stock'])
		cursor.execute("UPDATE ih_vaccine SET (vax_name, vax_brand_manufacturer, vax_batch_no, vax_lot_no, vax_dosage, vax_tech_platform, vax_ph_fda_approval, vax_storage_req, vax_efficiency, vax_side_effect, stock) = (%s,%s,%s, %s, %s, %s, %s, %s,%s, %s,%s)  WHERE vax_id =(%s)", 
		(vax_name,vax_brand_manufacturer,vax_batch_no,vax_lot_no,vax_dosage,vax_tech_platform,vax_ph_fda_approval,vax_storage_req,vax_efficiency,vax_side_effect,stock,vax_id))
		conn.commit()
		conn.close()
		return redirect('/adminvaccineinv')

@app.route("/schedule")
def schedule():
	schedule = []
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM ih_clinic_sched")
	for row in cursor.fetchall():
		schedule.append({"clinic_sched_id": row[0], "schedule_name": row[1], "contact_person": row[2], "maximum_attendees": row[3], "from_to_schedule": row[4]})
	conn.close()	
	return render_template("schedule.html", schedule= schedule)
	
@app.route("/adsb")
def adsb():
	return render_template("admin-add-schedule.html")

@app.route("/addschedule", methods = ['POST'])
def addschedule():
	if request.method == 'POST':
		schedule_name = request.form["schedule_name"]
		contact_person= request.form["contact_person"]
		maximum_attendees = request.form["maximum_attendees"]
		from_to_schedule= request.form["from_to_schedule"]
	conn = connection()
	cursor = conn.cursor()
	cursor.execute('INSERT INTO ih_clinic_sched (schedule_name, contact_person, maximum_attendees, from_to_schedule)'' VALUES (%s,%s,%s,%s)', 
	[schedule_name, contact_person, maximum_attendees, from_to_schedule])
	conn.commit()
	conn.close()
	return redirect('/schedule')

@app.route('/updateschedule/<int:clinic_sched_id>', methods = ['GET', 'POST'])
def updateschedule(clinic_sched_id):
	us =[]
	conn = connection()
	cursor = conn.cursor()
	if request.method == 'GET':
		cursor.execute("SELECT * FROM ih_clinic_sched WHERE clinic_sched_id = %s", (str(clinic_sched_id)))
		for row in cursor.fetchall():
			us.append({"clinic_sched_id": row[0], "schedule_name": row[1], "contact_person": row[2], "maximum_attendees": row[3], "from_to_schedule": row[4]})
		conn.close()
		return render_template("updateschedule.html",  schedule = us[0])
	if request.method == 'POST':
		schedule_name = str(request.form['schedule_name'])
		contact_person= str(request.form['contact_person'])
		maximum_attendees = int(request.form['maximum_attendees'])
		from_to_schedule= str(request.form['from_to_schedule'])
		cursor.execute("UPDATE ih_clinic_sched SET (schedule_name, contact_person, maximum_attendees, from_to_schedule) = (%s,%s,%s,%s) WHERE clinic_sched_id = (%s)", 
		(schedule_name, contact_person, maximum_attendees, from_to_schedule,clinic_sched_id))
		conn.commit()
		conn.close()
		return redirect('/schedule')

@app.route("/adminmedicineinv")
def adminmedicineinv():
	medicine = []
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM ih_medicine")
	for row in cursor.fetchall():
		medicine.append({"medicine_id": row[0], "medicine_name": row[1], "generic_name": row[2], "brand_name": row[3], "manufacturer": row[4], "dosage": row[5], "medicine_type": row[6], "description": row[7],"stock":row[8]})
	conn.close()	
	return render_template("adminmedicineinv.html", medicine = medicine)
	
@app.route("/addmedicine", methods = ['POST'])
def addmedicine():
	if request.method == 'POST':
		#medicine_id = request.form['medicine_id']
		medicine_name = request.form['medicine_name']
		generic_name = request.form['generic_name']
		brand_name = request.form['brand_name']
		manufacturer = request.form['manufacturer']
		dosage  = request.form['dosage']
		medicine_type = request.form['medicine_type']
		description = request.form['description']
		stock = request.form['stock']
	conn = connection()
	cursor = conn.cursor()
	cursor.execute('INSERT INTO ih_medicine (medicine_name, generic_name, brand_name, manufacturer, dosage, medicine_type, description,stock)'' VALUES (%s,%s, %s, %s, %s, %s, %s,%s)', 
	[medicine_name, generic_name, brand_name, manufacturer, dosage, medicine_type, description,stock])
	conn.commit()
	conn.close()
	return redirect('/adminmedicineinv')

@app.route('/updatemedicine/<int:medicine_id>', methods = ['GET', 'POST'])
def updatemedicine(medicine_id):
	um = []
	conn = connection()
	cursor = conn.cursor()
	if request.method == 'GET':
		cursor.execute("SELECT * FROM ih_medicine WHERE medicine_id = %s", (str(medicine_id)))
		for row in cursor.fetchall():
			um.append({"medicine_id": row[0], "medicine_name": row[1], "generic_name": row[2], "brand_name": row[3], "manufacturer": row[4], "dosage": row[5], "medicine_type": row[6], "description": row[7],"stock":row[8]})
		conn.close()
		return render_template("updatemedicine.html", medicine = um[0])
	if request.method == 'POST':
		medicine_name = str(request.form["medicine_name"])
		generic_name = str(request.form["generic_name"])
		brand_name = str(request.form["brand_name"])
		manufacturer = str(request.form["manufacturer"])
		dosage = str(request.form["dosage"])
		medicine_type = str(request.form["medicine_type"])
		description = str(request.form["description"])
		stock = int(request.form["stock"])
		cursor.execute("UPDATE ih_medicine SET (medicine_name, generic_name, brand_name, manufacturer, dosage, medicine_type, description,stock) = (%s,%s,%s, %s, %s, %s, %s, %s)  WHERE medicine_id =(%s)",
		(medicine_name, generic_name, brand_name, manufacturer, dosage, medicine_type,description,stock,medicine_id))
		conn.commit()
		conn.close()
		return redirect('/adminmedicineinv')

@app.route("/adminclinicinv")
def adminclinicinv():
	return render_template("adminclinicinv.html")

@app.route("/adminvc")
def adminvc():
	return render_template("adminh-view-clinic.html")

@app.route("/adminvd")
def adminvd():
	return render_template("adminh-view-dental.html")

@app.route("/adminvm")
def adminvm():
	return render_template("adminh-view-medicine.html")

@app.route("/adminvv")
def adminvv():
	return render_template("adminh-view-vax.html")

@app.route("/adds")
def adds():
	return render_template("admin-add-schedule.html")

@app.route("/addc")
def addc():
	return render_template("admin-add-clinic.html")

@app.route("/addm")
def addm():
	return render_template("admin-add-medicine.html")

@app.route("/addv")
def addv():
	return render_template("admin-add-vax.html")
@app.route("/adminaptvax")
def adminaptvax():
	adminaptvax = []
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM ih_medicine")
	for row in cursor.fetchall():
		adminaptvax.append({"medicine_id": row[0], "medicine_name": row[1], "generic_name": row[2], "brand_name": row[3], "manufacturer": row[4], "dosage": row[5], "medicine_type": row[6], "description": row[7]})
	conn.close()	
	return render_template("admin-apt-vax.html", adminaptvax = adminaptvax)

@app.route("/adminaptdental")
def adminaptdental():
	return render_template("admin-apt-dental.html")

@app.route("/adminaptmedicine")
def adminaptmedicine():
	return render_template("admin-apt-medicine.html")

@app.route("/adminaptclinic")
def adminaptclinic():
	return render_template("admin-apt-clinic.html")

@app.route("/adminaptdentaledit")
def adminaptdentaledit():
	return render_template("admin-apt-dental-edit.html")

@app.route("/adminaptmedicineedit")
def adminaptmedicineedit():
	return render_template("admin-apt-medicine-edit.html")

@app.route("/adminaptclinicedit")
def adminaptclinicedit():
	return render_template("admin-apt-clinic-edit.html")

@app.route("/adminaptvaxedit")
def adminaptvaxedit():
	return render_template("admin-apt-vax-edit.html")

@app.route("/adminhaptvax")
def adminhaptvax():
	return render_template("adminhistory-apt-vax.html")

@app.route("/adminhaptdental")
def adminhaptdental():
	return render_template("adminhistory-apt-dental.html")

@app.route("/adminhaptmedicine")
def adminhaptmedicine():
	return render_template("adminhistory-apt-medicine.html")

@app.route("/adminhaptclinic")
def adminhaptclinic():
	return render_template("adminhistory-apt-clinic.html")


@app.route("/indexstaff")
def indexstaff():
	email= "staff@email.com" 
	account_type= "Staff"
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT id,firstname FROM users_user WHERE email = %s AND account_type = %s", (email, account_type))
	user = cursor.fetchone()
	if user is not None:
		user_id, user_firstname = user
		session['user_id'] = user_id
		session['user_firstname'] = user_firstname
		return render_template("indexstaff.html")

@app.route("/schedulestaff")
def schedulestaff():
	schedulestaff = []
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM ih_clinic_sched")
	for row in cursor.fetchall():
		schedulestaff.append({"clinic_sched_id": row[0], "schedule_name": row[1], "contact_person": row[2], "maximum_attendees": row[3], "from_to_schedule": row[4]})
	conn.close()	
	return render_template("schedulestaff.html",schedulestaff=schedulestaff)

@app.route("/clinicstaff")
def clinicstaff():
	clinicstaff = []
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM ih_appointment")
	for row in cursor.fetchall():
		clinicstaff.append({"appt_id": row[0], "appt_type": row[1],"date": row[2],"remarks": row[3],"status": row[4],"time": row[5],"id": row[7]})
	return render_template("clinicstaff.html", clinicstaff = clinicstaff)

@app.route("/updateclinicstaff/<int:appt_id>", methods = ['GET', 'POST'])
def updateclinicstaff(appt_id):
	ucs = []
	conn = connection()
	cursor = conn.cursor()
	if request.method == 'GET':
		cursor.execute("SELECT * FROM ih_appointment WHERE appt_id = %s", (str(appt_id)))
		for row in cursor.fetchall():
			ucs.append({"appt_id": row[0], "appt_type": row[1],"date": row[2],"remarks": row[3],"status": row[4],"time": row[5],"id": row[7]})
		conn.close()
		return render_template("updateclinicstaff.html", clinicstaff = ucs[0])
	if request.method == 'POST':
		appt_type = str(request.form["appt_type"])
		remarks = str(request.form["remarks"])
		date = str(request.form["date"])
		clinic_sched_id = str(request.form["time"])
		status = str(request.form["status"])
		cursor.execute("UPDATE ih_appointment SET (appt_type, remarks, date, clinic_sched_id, status) = (%s,%s,%s, %s,%s)  WHERE appt_id =(%s)",
		(appt_type, remarks, date, clinic_sched_id, status,appt_id))
		conn.commit()
		conn.close()
		return redirect('/clinicstaff')

@app.route("/medicinestaff")
def medicinestaff():
	return render_template("medicinestaff.html")

@app.route('/updatemedicinestaff/<int:medicine_id>', methods = ['GET', 'POST'])
def updatemedicinestaff(medicine_id):
		return redirect('/medicinestaff')

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

@app.route('/updatevaccinationstaff/<int:vaccine_id>', methods = ['GET', 'POST'])
def updatevaccinationstaff(vaccine_id):
		return redirect('/vaccinationstaff')

@app.route("/dentalstaff")
def dentalstaff():
	dentalstaff = []
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM ih_appointment")
	for row in cursor.fetchall():
		dentalstaff.append({"appt_id": row[0], "appt_type": row[1],"remarks": row[2],"date": row[3],"time": row[4],"status": row[5]})
	conn.close()	
	return render_template("dentalstaff.html", dentalstaff = dentalstaff)

@app.route('/updatedentalstaff/<int:dental_id>', methods = ['GET', 'POST'])
def updatedentalstaff(dental_id):
		return redirect('/dentalstaff')

@app.route("/staffhaptvax")
def staffhaptvax():
	return render_template("staffhistory-apt-vax.html")

@app.route("/staffhviewvax")
def staffhviewaptvax():
	return render_template("staffhistory-view-vaccineh.html")

@app.route("/staffhaptdental")
def staffhaptdental():
	return render_template("staffhistory-apt-dental.html")

@app.route("/staffhviewdental")
def staffhviewdental():
	return render_template("staffhistory-view-dentalh.html")

@app.route("/staffhaptmedicine")
def staffhaptmedicine():
	return render_template("staffhistory-apt-medicine.html")

@app.route("/staffhviewmedicine")
def staffhviewmedicine():
	return render_template("staffhistory-view-medicineh.html")

@app.route("/staffhaptclinic")
def staffhaptclinic():
	return render_template("staffhistory-apt-clinic.html")

@app.route("/staffhviewclinic")
def staffhviewclinic():
	return render_template("staffhistory-view-clinic.html")

@app.route("/indexresident")
def indexresident():
	email= "kylemara@gmail.com" 
	account_type= "Resident"
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT id,firstname FROM users_user WHERE email = %s AND account_type = %s", (email, account_type))
	user = cursor.fetchone()
	if user is not None:
		user_id, user_firstname = user
		session['user_id'] = user_id
		session['user_firstname'] = user_firstname
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

@app.route("/residentas",methods=['GET', 'POST'])
def residentas():
	if('user_id' in session):
		if request.method == 'POST':
			appt_type= request.form['appt_type']
			date=request.form['date']
			clinic_services_id= request.form['clinic_services_id']
			id = session['user_id']
			clinic_sched_id=request.form['clinic_sched_id']		
			conn = connection()
			cursor = conn.cursor()
			cursor.execute('INSERT INTO ih_appointment (appt_type,date,clinic_services_id,id,clinic_sched_id)'' VALUES (%s,%s,%s,%s,%s)', 
			[appt_type,date,clinic_services_id,id,clinic_sched_id])
			conn.commit()
			conn.close()
		return render_template("residentbooking.html")

@app.route("/residentvax", methods=['GET', 'POST'])
def residentvax():
	if('user_id' in session):
		if request.method == 'POST':
			app_type= request.form['app_type']
			date=request.form['date']
			clinic_services_id= request.form['clinic_services_id']
			id = session['user_id']
			clinic_sched_id=request.form['clinic_sched_id']		
			conn = connection()
			cursor = conn.cursor()
			cursor.execute('INSERT INTO ih_appointment (appt_type,date,clinic_services_id,id,clinic_sched_id)'' VALUES (%s,%s,%s,%s,%s)', 
			[app_type,date,clinic_services_id,id,clinic_sched_id])
			conn.commit()
			conn.close()
			return render_template("residentbookingvax.html")



@app.route("/residentmedicine")
def residentmedicine():
	return render_template("residentmedicine.html") 

@app.route("/medicineresident")
def medicineresident():
	return render_template("medicineresident.html")

@app.route("/residenthaptvax")
def residenthaptvax():
	user_name = session['user_firstname']
	residenthaptclinic=[]
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT IH.APPT_TYPE,IH.DATE, IH.STATUS, U.FIRSTNAME, V.VAX_NAME, CSH.SCHEDULE_NAME FROM IH_APPOINTMENT IH INNER JOIN IH_VACCINE V  ON IH.VAX_ID = V.VAX_ID  INNER JOIN IH_CLINIC_SCHED CSH  ON CSH.CLINIC_SCHED_ID = IH.CLINIC_SCHED_ID INNER JOIN USERS_USER U  ON U.ID = IH.ID  WHERE FIRSTNAME= %s", (user_name,))
	for row in cursor.fetchall():
		residenthaptclinic.append({ "appt_type": row[0],"date": row[1],"status": row[2],"firstname": row[3],"Vaccine": row[4],"schedule_name": row[5]})
		conn.close()	
	return render_template("residenthistory-apt-vax.html")

@app.route("/reshistoryviewvax")
def reshistoryviewvax():
	return render_template("reshistory-view-vaccineh.html")

@app.route("/residenthaptdental")
def residenthaptdental():
	return render_template("residenthistory-apt-dental.html")

@app.route("/reshistoryviewdent")
def reshistoryviewdent():
	return render_template("reshistory-view-dentalh.html")

@app.route("/residenthaptmedicine")
def residenthaptmedicine():
	return render_template("residenthistory-apt-medicine.html")

@app.route("/reshistoryviewmed")
def reshistoryviewmed():
	return render_template("reshistory-view-medicineh.html")

@app.route("/residenthaptclinic")
def residenthaptclinic():
		user_name = session['user_firstname']
		residenthaptclinic=[]
		conn = connection()
		cursor = conn.cursor()
		cursor.execute("SELECT IH.APPT_TYPE,IH.DATE, IH.STATUS, U.FIRSTNAME, CSV.CLINIC_SERVICES_NAME, CSH.SCHEDULE_NAME FROM IH_APPOINTMENT IH INNER JOIN IH_CLINIC_SERVICES CSV ON IH.CLINIC_SERVICES_ID = CSV.CLINIC_SERVICES_ID INNER JOIN IH_CLINIC_SCHED CSH ON CSH.CLINIC_SCHED_ID = IH.CLINIC_SCHED_ID INNER JOIN USERS_USER U ON U.ID = IH.ID WHERE FIRSTNAME= %s", (user_name,))
		for row in cursor.fetchall():
			residenthaptclinic.append({ "appt_type": row[0],"date": row[1],"status": row[2],"firstname": row[3],"clinic_services_name": row[4],"schedule_name": row[5]})
		conn.close()	
		return render_template("residenthistory-apt-clinic.html",residenthaptclinic=residenthaptclinic)

@app.route("/reshistoryviewclinic")
def reshistoryviewclinic():
	return render_template("reshistory-view-clinic.html")

@app.route("/portal")
def portal():
    	return render_template("residentportal.html")

@app.route('/approve_status', methods=['POST'])
def approve_status():
	status = request.form['status']
	# Update the status in the database
	# # ...
	return jsonify({'message': 'Status approved'})

@app.route('/reject_status', methods=['POST'])
def reject_status():
	status = request.form['status']
	# Update the status in the databas
	# # ...
	return jsonify({'message': 'Status rejected'})
if __name__== '__main__':
	app.run(debug=True)
	