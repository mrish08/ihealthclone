from distutils.log import debug
from flask import Flask, render_template,request, redirect,request, url_for, session, logging
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

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/clinic")
def clinic():

	return render_template("clinic.html")


@app.route("/addclinic", methods = ['POST'])
def addclinic():
	
	return redirect('/clinic')


@app.route('/updateclinic/<int:clinic_services_id>', methods = ['GET', 'POST'])
def updateclinic(clinic_services_id):
	
		return redirect('/clinic')



@app.route("/dental")
def dental():
	return render_template("clinic.html")


@app.route("/vaccination")
def vaccination():
	
	return render_template("vaccination.html")

@app.route("/addvaccination", methods = ['POST'])
def addvaccination():
	
	return redirect('/vaccination')


@app.route('/updatevaccination/<int:vaccine_id>', methods = ['GET', 'POST'])
def updatevaccination(vaccine_id):
	
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

@app.route("/adminaptvax")
def adminaptvax():
	return render_template("admin-apt-vax.html")

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

	return render_template("clinicstaff.html")

@app.route("/medicinestaff")
def medicinestaff():
	return render_template("medicinestaff.html")

@app.route('/updatemedicinestaff/<int:medicine_id>', methods = ['GET', 'POST'])
def updatemedicinestaff(medicine_id):
		return redirect('/medicinestaff')

@app.route("/vaccinationstaff")
def vaccinationstaff():
	
	return render_template("vaccinationstaff.html")

@app.route('/updatevaccinationstaff/<int:vaccine_id>', methods = ['GET', 'POST'])
def updatevaccinationstaff(vaccine_id):
		return redirect('/vaccinationstaff')

@app.route("/dentalstaff")
def dentalstaff():
	return render_template("dentalstaff.html")

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