-- Database: iHealth_database

-- DROP DATABASE IF EXISTS "iHealth_database";

CREATE DATABASE "iHealth_database"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
create table roles (
role_id SERIAL PRIMARY KEY NOT NULL,
role_name varchar (250) not null
);

create table users (
user_id SERIAL PRIMARY KEY NOT NULL,
email varchar (250) not null,
password varchar (250) not null,
role_id int references roles(role_id)
);


create table staff (
staff_id SERIAL PRIMARY KEY NOT NULL,
first_name varchar (250) not null,
middle_name varchar (250) not null,
last_name varchar (250) not null,
contact int not null,
user_id int references users(user_id)
);

create table comorbidity (
comorbidity_id SERIAL PRIMARY KEY NOT NULL,
comorbidity_name varchar (250) not null
);

create table priority_group (
prio_group_id SERIAL PRIMARY KEY NOT NULL,
prio_group_name varchar (250) not null,
comorbidity_id int references comorbidity(comorbidity_id)
);

create table resident (
resident_id SERIAL PRIMARY KEY NOT NULL,
first_name varchar (250) not null,
middle_name varchar (250) null,
last_name varchar (250) not null,
suffix varchar (25) null,
birth_date date not null,
birth_place varchar (250) not null,
age int not null,
gender varchar (25) not null, 
contact_no int not null,
house_no varchar (250) null,
street varchar (250) not null,
barangay varchar (250) not null,
city varchar (250) not null,
province varchar (250) not null,
zip_code int not null,
civil_status varchar (250) not null,
blood_type varchar (25) null,
religion varchar (25) null,
prio_group_id int references priority_group(prio_group_id),
user_id int references users(user_id)
);

create table clinic_sched (
clinic_sched_id SERIAL PRIMARY KEY NOT NULL,
schedule timestamp not null,
schedule_name varchar (250) not null
);

create table vaccine (
vaccine_id SERIAL PRIMARY KEY NOT NULL,
vaccine_name varchar (250) not null,
lot_name varchar (250) not null,
brand_manufacturer varchar (250) not null
);

create table clinic_appt_status (
clinic_appt_status_id SERIAL PRIMARY KEY NOT NULL,
clinic_appt_status varchar (250) not null
);

create table clinic_services (
clinic_services_id SERIAL PRIMARY KEY NOT NULL,
clinic_services_name varchar (250) not null
);

create table medicine ( 
medicine_id SERIAL PRIMARY KEY NOT NULL,
medicine_name varchar (250) not null
);

create table med_pickup_appointment (
med_pickup_appointment_id SERIAL PRIMARY KEY NOT NULL,
date date not null,
resident_id int references resident(resident_id),
medicine_id int references medicine(medicine_id),
clinic_sched_id int references clinic_sched(clinic_sched_id),
clinic_appt_status_id int references clinic_appt_status(clinic_appt_status_id)  
);

create table dental_clinic_appointment (
dental_appt_id SERIAL PRIMARY KEY NOT NULL,
date date not null,	
resident_id int references resident(resident_id),
clinic_sched_id int references clinic_sched(clinic_sched_id), 
clinic_appt_status_id int references clinic_appt_status(clinic_appt_status_id)  	
);

create table clinic_appointment (
clinic_appt_id SERIAL PRIMARY KEY NOT NULL,
date date not null,
resident_id int references resident(resident_id),
clinic_services_id int references clinic_services(clinic_services_id),
clinic_sched_id int references clinic_sched(clinic_sched_id), 
clinic_appt_status_id int references clinic_appt_status(clinic_appt_status_id)
);

create table resident_diagnosis (
resident_diagnosis_id SERIAL PRIMARY KEY NOT NULL,
diagnosis varchar (250) not null,
prescription varchar (250) null,
med_cert varchar (250) null,
recommendation	varchar (250) null,
clinic_appt_id int references clinic_appointment(clinic_appt_id)
);

create table vax_appointment (
vax_appt_id SERIAL PRIMARY KEY NOT NULL,
date date not null,
resident_id int references resident(resident_id),
vaccine_id int references vaccine(vaccine_id),
clinic_sched_id int references clinic_sched(clinic_sched_id), 
clinic_appt_status_id int references clinic_appt_status(clinic_appt_status_id)
);


	
