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

create table ih_comorbidity (
comorbidity_id SERIAL PRIMARY KEY NOT NULL,
comorbidity_name varchar (250) not null 
);

create table ih_priority_group (
prio_group_id SERIAL PRIMARY KEY NOT NULL,
prio_group_name varchar (250) not null,
comorbidity_id int references comorbidity(comorbidity_id)
);

create table ih_clinic_sched (
clinic_sched_id SERIAL PRIMARY KEY NOT NULL,
from_schedule timestamp not null,
to_schedule timestamp not null,
schedule_name varchar (250) not null
contact_person varchar (250) null
maximum_attendees int null,
clinic_services_id int references clinic_services(clinic_services_id)
);

create table ih_vaccine (
vax_id SERIAL PRIMARY KEY NOT NULL,
vax_name varchar (250) not null,
vax_brand_manufacturer varchar (250) not null
vax_batch_no varchar (250) null,
vax_lot_no varchar (250) null,
vax_dosage varchar (250) not null,
vax_tech_platform varchar (250) not null
vax_ph_fda_approval varchar (250) null
vax_storage_req varchar (250) not null
vax_efficiency varchar (250) null,
vax_side_effect varchar (250) not null
);

create table ih_clinic_services (
clinic_services_id SERIAL PRIMARY KEY NOT NULL,
clinic_services_name varchar (250) not null
);

create table ih_medicine ( 
medicine_id SERIAL PRIMARY KEY NOT NULL,
medicine_name varchar (250) not null,
generic_name varchar (250) not null,
brand_name varchar (250) not null,
manufacturer varchar (250) not null,
dosage varchar (250) not null,
medicine_type varchar (250) not null,
description varchar (250) not null
);

create table ih_appointment (
appt_id SERIAL PRIMARY KEY NOT NULL,
appt_type string,
--(medicine pickup, dental appointemnt, clinic appointment, vaccine appointemnt)
resident_id int not null references resident(resident_id),
medicine_id int references medicine(medicine_id),
clinic_sched_id int references clinic_sched(clinic_sched_id),
vaccine_id int references vaccine(vaccine_id),
remarks varchar (250) null,
processed_by varchar (250) not null,
date date not null,
time timestamp not null,
status string 
)

create table ih_resident_diagnosis (
resident_diagnosis_id SERIAL PRIMARY KEY NOT NULL,
diagnosis varchar (250) not null,
prescription varchar (250) null,
med_cert varchar (250) null,
recommendation	varchar (250) null,
clinic_appt_id int references clinic_appointment(clinic_appt_id)
);