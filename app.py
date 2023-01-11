from distutils.log import debug
from flask import Flask, render_template,request, redirect,request, jsonify, url_for, session, logging
import os
import psycopg2
from flask import session

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

@app.route("/loginadmin")
def loginadmin():
    if request.method == 'POST':
        session.pop('user',None)
        if request.form['password'] == 'password':
            session['user'] = request.form['email']
            return redirect(url_for('protected'))
    return render_template('loginadmin.html')

@app.route('/protected')
def protected():
    if g.user:
        return render_template('protected.html',user=session['user'])
    return redirect(url_for('loginadmin'))

@app.route('/dropsession')
def dropsession():
    session.pop('user',None)
    return render_template('loginadmin.html')

@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']
	
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('email', None)
    return redirect(url_for('loginadmin'))


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
		vaccination.append({"vax_id": row[0], "vax_name": row[1], "vax_brand_manufacturer": row[2], "vax_batch_no": row[3], "vax_lot_no": row[4], "vax_dosage": row[5], "vax_tech_platform": row[6], "vax_ph_fda_approval": row[7], "vax_storage_req": row[8], "vax_efficiency": row[9], "vax_side_effect": row[10]})
	conn.close()	
	return render_template("vaccination.html", vaccination = vaccination)

@app.route("/addvaccination", methods = ['POST'])
def addvaccination():
	if request.method == 'POST':
		vax_id = request.form['vax_id']
		vax_name = request.form['vax_name']
		vax_brand_manufacturer = request.form['vax_brand_manufacturer']
		vax_batch_no = request.form['vax_batch_no']
		vax_lot_no = request.form['vax_lot_no']
		vax_dosage  = request.form['vax_dosage ']
		vax_tech_platform = request.form['vax_tech_platform']
		vax_ph_fda_approval = request.form['vax_ph_fda_approval']
		vax_storage_req  = request.form['vax_storage_req ']
		vax_efficiency  = request.form['vax_efficiency ']
		vax_side_effect  = request.form['vax_side_effect ']
	conn = connection()
	cursor = conn.cursor()
	cursor.execute('INSERT INTO ih_vaccine (vax_id, vax_name, vax_brand_manufacturer, vax_batch_no, vax_lot_no, vax_dosage, vax_tech_platform, vax_ph_fda_approval, vax_storage_req, vax_efficiency, vax_side_effect)'' VALUES (%s,%s,%s, %s, %s, %s, %s, %s,%s, %s, %s)', 
	[vax_id, vax_name, vax_brand_manufacturer, vax_batch_no, vax_lot_no, vax_dosage, vax_tech_platform, vax_ph_fda_approval, vax_storage_req, vax_efficiency, vax_side_effect])
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
			uv.append({"vax_id": row[0], "vax_name": row[1], "vax_brand_manufacturer": row[2], "vax_batch_no": row[3], "vax_lot_no": row[4], "vax_dosage": row[5], "vax_tech_platform": row[6], "vax_ph_fda_approval": row[7], "vax_storage_req": row[8], "vax_efficiency": row[9], "vax_side_effect": row[10]})
		conn.close()
		return render_template("updatevaccination.html", vaccination = uv[0])
	if request.method == 'POST':
		vax_id = str(request.form["vax_id"])
		vax_name = str(request.form["vax_name"])
		vax_brand_manufacturer = str(request.form["vax_brand_manufacturer"])
		vax_batch_no = str(request.form["vax_batch_no"])
		vax_lot_no = str(request.form["vax_lot_no"])
		vax_dosage = str(request.form["vax_dosage"])
		vax_tech_platform = str(request.form["vax_tech_platform"])
		vax_ph_fda_approval = str(request.form["vax_ph_fda_approval"])
		vax_storage_req = str(request.form["vax_storage_req"])
		vax_efficiency = str(request.form["vax_efficiency"])
		vax_side_effect = str(request.form["vax_side_effect"])
		cursor.execute("UPDATE vaccine SET (vax_id, vax_name, vax_brand_manufacturer, vax_batch_no, vax_lot_no, vax_dosage, vax_tech_platform, vax_ph_fda_approval, vax_storage_req, vax_efficiency, vax_side_effect) = (%s,%s,%s, %s, %s, %s, %s, %s,%s, %s, %s)  WHERE vaccine_id =(%s)", (vax_id, vax_name, vax_brand_manufacturer, vax_batch_no, vax_lot_no, vax_dosage, vax_tech_platform, vax_ph_fda_approval, vax_storage_req, vax_efficiency, vax_side_effect))
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
	medicine = []
	conn = connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM ih_medicine")
	for row in cursor.fetchall():
		medicine.append({"medicine_id": row[0], "medicine_name": row[1], "generic_name": row[2], "brand_name": row[3], "manufacturer": row[4], "dosage": row[5], "medicine_type": row[6], "description": row[7]})
	conn.close()	
	return render_template("medicine.html", medicine = medicine)
	
@app.route("/addmedicine", methods = ['GET', 'POST'])
def addmedicine():
	if request.method == 'POST':
		medicine_id = request.form['medicine_id']
		medicine_name = request.form['medicine_name']
		generic_name = request.form['generic_name']
		brand_name = request.form['brand_name']
		manufacturer = request.form['manufacturer']
		dosage  = request.form['dosage ']
		medicine_type = request.form['medicine_type']
		description = request.form['description']

	conn = connection()
	cursor = conn.cursor()
	cursor.execute('INSERT INTO ih_medicine (medicine_id, medicine_name, generic_name, brand_name, manufacturer, dosage, medicine_type, description)'' VALUES (%s,%s,%s, %s, %s, %s, %s, %s)', 
	[medicine_id, medicine_name, generic_name, brand_name, manufacturer, dosage, medicine_type, description])
	conn.commit()
	conn.close()
	return redirect('/medicine')

@app.route('/updatemedicine/<int:medicine_id>', methods = ['GET', 'POST'])
def updatemedicine(medicine_id):
	um = []
	conn = connection()
	cursor = conn.cursor()
	if request.method == 'GET':
		cursor.execute("SELECT * FROM ih_medicine WHERE medicine_id = %s", (str(medicine_id)))
		for row in cursor.fetchall():
			um.append({"medicine_id": row[0], "medicine_name": row[1], "generic_name": row[2], "brand_name": row[3], "manufacturer": row[4], "dosage": row[5], "medicine_type": row[6], "description": row[7]})
		conn.close()
		return render_template("updatemedicine.html", medicine = um[0])
	if request.method == 'POST':
		medicine_id = str(request.form["medicine_id"])
		medicine_name = str(request.form["medicine_name"])
		generic_name = str(request.form["generic_name"])
		brand_name = str(request.form["brand_name"])
		manufacturer = str(request.form["manufacturer"])
		dosage = str(request.form["dosage"])
		medicine_type = str(request.form["medicine_type"])
		description = str(request.form["description"])
		cursor.execute("UPDATE medicine SET (medicine_id, medicine_name, generic_name, brand_name, manufacturer, dosage, medicine_type, description) = (%s,%s,%s, %s, %s, %s, %s, %s)  WHERE medicine_id =(%s)",
		(medicine_id, medicine_name, generic_name, brand_name, manufacturer, dosage, medicine_type, description))
		conn.commit()
		conn.close()
		return redirect('/medicine')

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

@app.route("/loginadmin", methods=["POST", "GET"])
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

@app.route("/updateclinicstaff")
def updateclinicstaff():
	ucs = []
	conn = connection()
	cursor = conn.cursor()
	if request.method == 'GET':
		cursor.execute("SELECT * FROM ih_appointment WHERE medicine_id = %s", (str(medicine_id)))
		for row in cursor.fetchall():
			ucs.append({"medicine_id": row[0], "medicine_name": row[1], "generic_name": row[2], "brand_name": row[3], "manufacturer": row[4], "dosage": row[5], "medicine_type": row[6], "description": row[7]})
		conn.close()
		return render_template("updatemedicine.html", medicine = ucs[0])
	if request.method == 'POST':
		medicine_id = str(request.form["medicine_id"])
		medicine_name = str(request.form["medicine_name"])
		generic_name = str(request.form["generic_name"])
		brand_name = str(request.form["brand_name"])
		manufacturer = str(request.form["manufacturer"])
		dosage = str(request.form["dosage"])
		medicine_type = str(request.form["medicine_type"])
		description = str(request.form["description"])
		cursor.execute("UPDATE medicine SET (medicine_id, medicine_name, generic_name, brand_name, manufacturer, dosage, medicine_type, description) = (%s,%s,%s, %s, %s, %s, %s, %s)  WHERE medicine_id =(%s)",
		(medicine_id, medicine_name, generic_name, brand_name, manufacturer, dosage, medicine_type, description))
		conn.commit()
		conn.close()
		return redirect('/medicine')

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

@app.route("/residentas")
def residentas():
	if request.method == 'POST':
		medicine_id = request.form['medicine_id']
		medicine_name = request.form['medicine_name']
		generic_name = request.form['generic_name']
		brand_name = request.form['brand_name']
		manufacturer = request.form['manufacturer']
		dosage  = request.form['dosage ']
		medicine_type = request.form['medicine_type']
		description = request.form['description']

	conn = connection()
	cursor = conn.cursor()
	cursor.execute('INSERT INTO ih_medicine (medicine_id, medicine_name, generic_name, brand_name, manufacturer, dosage, medicine_type, description)'' VALUES (%s,%s,%s, %s, %s, %s, %s, %s)', 
	[medicine_id, medicine_name, generic_name, brand_name, manufacturer, dosage, medicine_type, description])
	conn.commit()
	conn.close()
	return render_template("clinicresident.html")

@app.route("/medicineresident")
def medicineresident():
	return render_template("medicineresident.html")

@app.route("/residenthaptvax")
def residenthaptvax():
	return render_template("residenthistory-apt-vax.html")

@app.route("/residenthaptdental")
def residenthaptdental():
	return render_template("residenthistory-apt-dental.html")

@app.route("/residenthaptmedicine")
def residenthaptmedicine():
	return render_template("residenthistory-apt-medicine.html")

@app.route("/residenthaptclinic")
def residenthaptclinic():
	return render_template("residenthistory-apt-clinic.html")

if __name__== '__main__':
	app.debug=True
app.run(debug=True)