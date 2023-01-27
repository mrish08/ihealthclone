-- Database: iHealth_database

-- DROP DATABASE IF EXISTS "bitbo";

CREATE DATABASE "bitbo"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE IF NOT EXISTS public.account_emailaddress
(
    id integer NOT NULL DEFAULT nextval('account_emailaddress_id_seq'::regclass),
    email character varying(254) COLLATE pg_catalog."default" NOT NULL,
    verified boolean NOT NULL,
    "primary" boolean NOT NULL,
    user_id bigint NOT NULL,
    CONSTRAINT account_emailaddress_pkey PRIMARY KEY (id),
    CONSTRAINT account_emailaddress_email_key UNIQUE (email)
);

CREATE TABLE IF NOT EXISTS public.account_emailconfirmation
(
    id integer NOT NULL DEFAULT nextval('account_emailconfirmation_id_seq'::regclass),
    created timestamp with time zone NOT NULL,
    sent timestamp with time zone,
    key character varying(64) COLLATE pg_catalog."default" NOT NULL,
    email_address_id integer NOT NULL,
    CONSTRAINT account_emailconfirmation_pkey PRIMARY KEY (id),
    CONSTRAINT account_emailconfirmation_key_key UNIQUE (key)
);

CREATE TABLE IF NOT EXISTS public.auth_group
(
    id integer NOT NULL DEFAULT nextval('auth_group_id_seq'::regclass),
    name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT auth_group_pkey PRIMARY KEY (id),
    CONSTRAINT auth_group_name_key UNIQUE (name)
);

CREATE TABLE IF NOT EXISTS public.auth_group_permissions
(
    id bigint NOT NULL DEFAULT nextval('auth_group_permissions_id_seq'::regclass),
    group_id integer NOT NULL,
    permission_id integer NOT NULL,
    CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id),
    CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id)
);

CREATE TABLE IF NOT EXISTS public.auth_permission
(
    id integer NOT NULL DEFAULT nextval('auth_permission_id_seq'::regclass),
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT auth_permission_pkey PRIMARY KEY (id),
    CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename)
);

CREATE TABLE IF NOT EXISTS public.authtoken_token
(
    key character varying(40) COLLATE pg_catalog."default" NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id bigint NOT NULL,
    CONSTRAINT authtoken_token_pkey PRIMARY KEY (key),
    CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id)
);

CREATE TABLE IF NOT EXISTS public.blotter_blotter
(
    id bigint NOT NULL DEFAULT nextval('blotter_blotter_id_seq'::regclass),
    complaint character varying(255) COLLATE pg_catalog."default",
    status character varying(255) COLLATE pg_catalog."default",
    complainant character varying(255) COLLATE pg_catalog."default",
    date_recorded timestamp with time zone NOT NULL,
    blotter_id uuid NOT NULL,
    complainant_address character varying(255) COLLATE pg_catalog."default",
    complainant_age character varying(255) COLLATE pg_catalog."default",
    complainant_contact character varying(255) COLLATE pg_catalog."default",
    defendant character varying(255) COLLATE pg_catalog."default",
    defendant_address character varying(255) COLLATE pg_catalog."default",
    defendant_age character varying(255) COLLATE pg_catalog."default",
    defendant_contact character varying(255) COLLATE pg_catalog."default",
    complainant_id character varying(255) COLLATE pg_catalog."default",
    defendant_id character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT blotter_blotter_pkey PRIMARY KEY (id),
    CONSTRAINT blotter_blotter_blotter_id_93f6717d_uniq UNIQUE (blotter_id)
);

CREATE TABLE IF NOT EXISTS public.brgy_id_barangayid
(
    id bigint NOT NULL DEFAULT nextval('brgy_id_barangayid_id_seq'::regclass),
    id_no uuid NOT NULL,
    tin character varying(255) COLLATE pg_catalog."default",
    sss character varying(255) COLLATE pg_catalog."default",
    purok character varying(255) COLLATE pg_catalog."default",
    street character varying(255) COLLATE pg_catalog."default",
    lastname character varying(255) COLLATE pg_catalog."default",
    middlename character varying(255) COLLATE pg_catalog."default",
    firstname character varying(255) COLLATE pg_catalog."default",
    birthdate timestamp with time zone NOT NULL,
    date_created timestamp with time zone NOT NULL,
    image character varying(100) COLLATE pg_catalog."default" NOT NULL,
    contact_number character varying(255) COLLATE pg_catalog."default",
    barangay character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT brgy_id_barangayid_pkey PRIMARY KEY (id),
    CONSTRAINT brgy_id_barangayid_id_no_key UNIQUE (id_no)
);

CREATE TABLE IF NOT EXISTS public.certificate_certificate
(
    id bigint NOT NULL DEFAULT nextval('certificate_certificate_id_seq'::regclass),
    certificate_name character varying(255) COLLATE pg_catalog."default",
    amount character varying(255) COLLATE pg_catalog."default",
    image character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT certificate_certificate_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.django_admin_log
(
    id integer NOT NULL DEFAULT nextval('django_admin_log_id_seq'::regclass),
    action_time timestamp with time zone NOT NULL,
    object_id text COLLATE pg_catalog."default",
    object_repr character varying(200) COLLATE pg_catalog."default" NOT NULL,
    action_flag smallint NOT NULL,
    change_message text COLLATE pg_catalog."default" NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.django_content_type
(
    id integer NOT NULL DEFAULT nextval('django_content_type_id_seq'::regclass),
    app_label character varying(100) COLLATE pg_catalog."default" NOT NULL,
    model character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT django_content_type_pkey PRIMARY KEY (id),
    CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model)
);

CREATE TABLE IF NOT EXISTS public.django_migrations
(
    id bigint NOT NULL DEFAULT nextval('django_migrations_id_seq'::regclass),
    app character varying(255) COLLATE pg_catalog."default" NOT NULL,
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    applied timestamp with time zone NOT NULL,
    CONSTRAINT django_migrations_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.django_session
(
    session_key character varying(40) COLLATE pg_catalog."default" NOT NULL,
    session_data text COLLATE pg_catalog."default" NOT NULL,
    expire_date timestamp with time zone NOT NULL,
    CONSTRAINT django_session_pkey PRIMARY KEY (session_key)
);

CREATE TABLE IF NOT EXISTS public.events_event
(
    id bigint NOT NULL DEFAULT nextval('events_event_id_seq'::regclass),
    event_name character varying(255) COLLATE pg_catalog."default",
    event_type character varying(255) COLLATE pg_catalog."default",
    theme character varying(255) COLLATE pg_catalog."default",
    date timestamp with time zone NOT NULL,
    image character varying(100) COLLATE pg_catalog."default" NOT NULL,
    descriptions character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT events_event_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.household_household
(
    id bigint NOT NULL DEFAULT nextval('household_household_id_seq'::regclass),
    no_people integer NOT NULL,
    length_residence integer NOT NULL,
    firstname character varying(255) COLLATE pg_catalog."default",
    middlename character varying(255) COLLATE pg_catalog."default",
    family_type character varying(255) COLLATE pg_catalog."default",
    resident_id integer NOT NULL,
    lastname character varying(255) COLLATE pg_catalog."default",
    blood_type character varying(255) COLLATE pg_catalog."default",
    civil_status character varying(255) COLLATE pg_catalog."default",
    educational_attainment character varying(255) COLLATE pg_catalog."default",
    gender character varying(255) COLLATE pg_catalog."default",
    height character varying(255) COLLATE pg_catalog."default",
    occupation character varying(255) COLLATE pg_catalog."default",
    weight character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT household_household_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.i_clinic_clinic
(
    id bigint NOT NULL DEFAULT nextval('i_clinic_clinic_id_seq'::regclass),
    service_name character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT i_clinic_clinic_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.i_medicine_medicine
(
    id bigint NOT NULL DEFAULT nextval('i_medicine_medicine_id_seq'::regclass),
    medicine_name character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT i_medicine_medicine_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.i_schedule_schedule
(
    id bigint NOT NULL DEFAULT nextval('i_schedule_schedule_id_seq'::regclass),
    schedule_name character varying(255) COLLATE pg_catalog."default",
    "time" character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT i_schedule_schedule_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.i_vaccination_vaccine
(
    id bigint NOT NULL DEFAULT nextval('i_vaccination_vaccine_id_seq'::regclass),
    vaccine_name character varying(255) COLLATE pg_catalog."default",
    lot_name character varying(255) COLLATE pg_catalog."default",
    brand character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT i_vaccination_vaccine_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.ih_appointment
(
    appt_id integer NOT NULL DEFAULT nextval('ih_appointment_appt_id_seq'::regclass),
    appt_type character varying(255) COLLATE pg_catalog."default",
    date date NOT NULL,
    remarks character varying(255) COLLATE pg_catalog."default",
    status character varying(255) COLLATE pg_catalog."default" DEFAULT 'pending'::character varying,
    clinic_services_id integer,
    resident_diagnosis_id integer,
    id integer,
    clinic_sched_id integer,
    vax_id integer,
    CONSTRAINT ih_appointment_pkey PRIMARY KEY (appt_id)
);

CREATE TABLE IF NOT EXISTS public.ih_clinic_sched
(
    clinic_sched_id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    schedule_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    contact_person character varying(255) COLLATE pg_catalog."default",
    maximum_attendees integer,
    from_to_schedule character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT ih_clinic_sched_pkey PRIMARY KEY (clinic_sched_id)
);

CREATE TABLE IF NOT EXISTS public.ih_clinic_services
(
    clinic_services_id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    clinic_services_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT ih_clinic_services_pkey PRIMARY KEY (clinic_services_id)
);

CREATE TABLE IF NOT EXISTS public.ih_clinic_supply
(
    clinic_supp_id integer NOT NULL DEFAULT nextval('ih_clinic_supply_clinic_supp_id_seq'::regclass),
    item_name character varying(255) COLLATE pg_catalog."default",
    description character varying(255) COLLATE pg_catalog."default",
    qty integer,
    CONSTRAINT ih_clinic_supply_pkey PRIMARY KEY (clinic_supp_id)
);

CREATE TABLE IF NOT EXISTS public.ih_comorbidity
(
    comorbidity_id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    comorbidity_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT ih_comorbidity_pkey PRIMARY KEY (comorbidity_id)
);

CREATE TABLE IF NOT EXISTS public.ih_medicine
(
    medicine_id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    medicine_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    generic_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    brand_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    manufacturer character varying(255) COLLATE pg_catalog."default" NOT NULL,
    dosage character varying(255) COLLATE pg_catalog."default" NOT NULL,
    medicine_type character varying(255) COLLATE pg_catalog."default" NOT NULL,
    description character varying(255) COLLATE pg_catalog."default" NOT NULL,
    stock integer NOT NULL,
    CONSTRAINT ih_medicine_pkey PRIMARY KEY (medicine_id)
);

CREATE TABLE IF NOT EXISTS public.ih_medicine_appointment
(
    med_appt_id integer NOT NULL DEFAULT nextval('ih_medicine_appointment_med_appt_id_seq'::regclass),
    appt_type character varying(255) COLLATE pg_catalog."default" DEFAULT 'Medicine Pick-up'::character varying,
    date date NOT NULL,
    remarks character varying(255) COLLATE pg_catalog."default",
    status character varying(255) COLLATE pg_catalog."default" DEFAULT 'pending'::character varying,
    qty integer,
    id integer,
    clinic_sched_id integer,
    medicine_id integer,
    CONSTRAINT ih_medicine_appointment_pkey PRIMARY KEY (med_appt_id)
);

CREATE TABLE IF NOT EXISTS public.ih_priority_group
(
    prio_group_id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    prio_group_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    comorbidity_id_id bigint,
    CONSTRAINT ih_priority_group_pkey PRIMARY KEY (prio_group_id)
);

CREATE TABLE IF NOT EXISTS public.ih_resident_diagnosis
(
    resident_diagnosis_id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    diagnosis character varying(255) COLLATE pg_catalog."default" NOT NULL,
    prescription character varying(255) COLLATE pg_catalog."default" NOT NULL,
    med_cert character varying(255) COLLATE pg_catalog."default",
    recommendation character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT ih_resident_diagnosis_pkey PRIMARY KEY (resident_diagnosis_id)
);

CREATE TABLE IF NOT EXISTS public.ih_vaccine
(
    vax_id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    vax_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    vax_brand_manufacturer character varying(255) COLLATE pg_catalog."default" NOT NULL,
    vax_batch_no character varying(255) COLLATE pg_catalog."default",
    vax_lot_no character varying(255) COLLATE pg_catalog."default" NOT NULL,
    vax_dosage character varying(255) COLLATE pg_catalog."default" NOT NULL,
    vax_tech_platform character varying(255) COLLATE pg_catalog."default" NOT NULL,
    vax_ph_fda_approval character varying(255) COLLATE pg_catalog."default",
    vax_storage_req character varying(255) COLLATE pg_catalog."default" NOT NULL,
    vax_efficiency character varying(255) COLLATE pg_catalog."default",
    vax_side_effect character varying(255) COLLATE pg_catalog."default" NOT NULL,
    stock integer NOT NULL,
    CONSTRAINT ih_vaccine_pkey PRIMARY KEY (vax_id)
);

CREATE TABLE IF NOT EXISTS public.login_ihealth
(
    resident_id integer NOT NULL DEFAULT nextval('login_ihealth_resident_id_seq'::regclass),
    res_type character varying(255) COLLATE pg_catalog."default",
    email character varying(255) COLLATE pg_catalog."default",
    password character varying(255) COLLATE pg_catalog."default",
    age integer,
    address character varying(255) COLLATE pg_catalog."default",
    gender character varying(255) COLLATE pg_catalog."default",
    bday date,
    CONSTRAINT login_ihealth_pkey PRIMARY KEY (resident_id)
);

CREATE TABLE IF NOT EXISTS public.logs_logs
(
    id bigint NOT NULL DEFAULT nextval('logs_logs_id_seq'::regclass),
    user_id character varying(255) COLLATE pg_catalog."default",
    activity character varying(255) COLLATE pg_catalog."default",
    date_created timestamp with time zone NOT NULL,
    account_type character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT logs_logs_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.measure_measure
(
    id bigint NOT NULL DEFAULT nextval('measure_measure_id_seq'::regclass),
    description text COLLATE pg_catalog."default",
    title text COLLATE pg_catalog."default",
    created_date timestamp with time zone NOT NULL,
    is_featured boolean NOT NULL,
    image character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT measure_measure_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.ordinance_ordinance
(
    id bigint NOT NULL DEFAULT nextval('ordinance_ordinance_id_seq'::regclass),
    code character varying(255) COLLATE pg_catalog."default",
    title character varying(255) COLLATE pg_catalog."default",
    description character varying(255) COLLATE pg_catalog."default",
    date_posted timestamp with time zone NOT NULL,
    files character varying(100) COLLATE pg_catalog."default" NOT NULL,
    is_featured boolean NOT NULL,
    CONSTRAINT ordinance_ordinance_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.register_registerevent
(
    id bigint NOT NULL DEFAULT nextval('register_registerevent_id_seq'::regclass),
    user_id integer NOT NULL,
    event_id integer NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    status character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT register_registerevent_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.resolution_resolution
(
    id bigint NOT NULL DEFAULT nextval('resolution_resolution_id_seq'::regclass),
    description text COLLATE pg_catalog."default",
    title text COLLATE pg_catalog."default",
    created_date timestamp with time zone NOT NULL,
    image character varying(100) COLLATE pg_catalog."default" NOT NULL,
    is_featured boolean NOT NULL,
    CONSTRAINT resolution_resolution_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.services_services
(
    id bigint NOT NULL DEFAULT nextval('services_services_id_seq'::regclass),
    request_id character varying(255) COLLATE pg_catalog."default",
    "user" character varying(255) COLLATE pg_catalog."default",
    certificate_type character varying(255) COLLATE pg_catalog."default",
    findings character varying(255) COLLATE pg_catalog."default",
    purpose character varying(255) COLLATE pg_catalog."default",
    date_issued timestamp with time zone NOT NULL,
    status character varying(255) COLLATE pg_catalog."default",
    receipt_number character varying(255) COLLATE pg_catalog."default",
    remark character varying(255) COLLATE pg_catalog."default",
    business_name character varying(255) COLLATE pg_catalog."default",
    business_status character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT services_services_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.settings_settings
(
    id bigint NOT NULL DEFAULT nextval('settings_settings_id_seq'::regclass),
    barangay_description character varying(255) COLLATE pg_catalog."default",
    barangay_name character varying(255) COLLATE pg_catalog."default",
    barangay_purok character varying(255) COLLATE pg_catalog."default",
    files character varying(100) COLLATE pg_catalog."default" NOT NULL,
    contact_number character varying(255) COLLATE pg_catalog."default",
    email character varying(255) COLLATE pg_catalog."default",
    office_hours character varying(255) COLLATE pg_catalog."default",
    barangay_province character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT settings_settings_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.socialaccount_socialaccount
(
    id integer NOT NULL DEFAULT nextval('socialaccount_socialaccount_id_seq'::regclass),
    provider character varying(30) COLLATE pg_catalog."default" NOT NULL,
    uid character varying(191) COLLATE pg_catalog."default" NOT NULL,
    last_login timestamp with time zone NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    extra_data text COLLATE pg_catalog."default" NOT NULL,
    user_id bigint NOT NULL,
    CONSTRAINT socialaccount_socialaccount_pkey PRIMARY KEY (id),
    CONSTRAINT socialaccount_socialaccount_provider_uid_fc810c6e_uniq UNIQUE (provider, uid)
);

CREATE TABLE IF NOT EXISTS public.socialaccount_socialapp
(
    id integer NOT NULL DEFAULT nextval('socialaccount_socialapp_id_seq'::regclass),
    provider character varying(30) COLLATE pg_catalog."default" NOT NULL,
    name character varying(40) COLLATE pg_catalog."default" NOT NULL,
    client_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
    secret character varying(191) COLLATE pg_catalog."default" NOT NULL,
    key character varying(191) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT socialaccount_socialapp_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.socialaccount_socialtoken
(
    id integer NOT NULL DEFAULT nextval('socialaccount_socialtoken_id_seq'::regclass),
    token text COLLATE pg_catalog."default" NOT NULL,
    token_secret text COLLATE pg_catalog."default" NOT NULL,
    expires_at timestamp with time zone,
    account_id integer NOT NULL,
    app_id integer NOT NULL,
    CONSTRAINT socialaccount_socialtoken_pkey PRIMARY KEY (id),
    CONSTRAINT socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq UNIQUE (app_id, account_id)
);

CREATE TABLE IF NOT EXISTS public.token_blacklist_blacklistedtoken
(
    id bigint NOT NULL DEFAULT nextval('token_blacklist_blacklistedtoken_id_seq'::regclass),
    blacklisted_at timestamp with time zone NOT NULL,
    token_id bigint NOT NULL,
    CONSTRAINT token_blacklist_blacklistedtoken_pkey PRIMARY KEY (id),
    CONSTRAINT token_blacklist_blacklistedtoken_token_id_key UNIQUE (token_id)
);

CREATE TABLE IF NOT EXISTS public.token_blacklist_outstandingtoken
(
    id bigint NOT NULL DEFAULT nextval('token_blacklist_outstandingtoken_id_seq'::regclass),
    token text COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp with time zone,
    expires_at timestamp with time zone NOT NULL,
    user_id bigint,
    jti character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT token_blacklist_outstandingtoken_pkey PRIMARY KEY (id),
    CONSTRAINT token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_uniq UNIQUE (jti)
);

CREATE TABLE IF NOT EXISTS public.users_user
(
    id bigint NOT NULL DEFAULT nextval('users_user_id_seq'::regclass),
    email character varying(254) COLLATE pg_catalog."default",
    firstname character varying(255) COLLATE pg_catalog."default" NOT NULL,
    lastname character varying(255) COLLATE pg_catalog."default" NOT NULL,
    account_type character varying(255) COLLATE pg_catalog."default" NOT NULL,
    password character varying(255) COLLATE pg_catalog."default",
    date_joined timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    is_staff boolean NOT NULL,
    is_superuser boolean NOT NULL,
    last_login timestamp with time zone,
    updated_at timestamp with time zone NOT NULL,
    barangay character varying(255) COLLATE pg_catalog."default",
    birthdate date,
    middlename character varying(255) COLLATE pg_catalog."default",
    condition_status character varying(255) COLLATE pg_catalog."default",
    educational_attainment character varying(255) COLLATE pg_catalog."default",
    gender character varying(255) COLLATE pg_catalog."default",
    house_status character varying(255) COLLATE pg_catalog."default",
    occupation character varying(255) COLLATE pg_catalog."default",
    religion character varying(255) COLLATE pg_catalog."default",
    mobile_number character varying(255) COLLATE pg_catalog."default",
    purok character varying(255) COLLATE pg_catalog."default",
    street character varying(255) COLLATE pg_catalog."default",
    blood_type character varying(255) COLLATE pg_catalog."default",
    username character varying(255) COLLATE pg_catalog."default",
    official_role character varying(255) COLLATE pg_catalog."default",
    official_type character varying(255) COLLATE pg_catalog."default",
    suffix character varying(255) COLLATE pg_catalog."default",
    end_term date,
    start_term date,
    image character varying(100) COLLATE pg_catalog."default" NOT NULL,
    birthplace character varying(255) COLLATE pg_catalog."default",
    civil_status character varying(255) COLLATE pg_catalog."default",
    height integer,
    prio_group_id bigint,
    province character varying(255) COLLATE pg_catalog."default",
    weight integer,
    zipcode integer,
    age integer NOT NULL,
    is_voter boolean NOT NULL,
    is_head boolean NOT NULL,
    is_employed boolean NOT NULL,
    verification_id character varying(100) COLLATE pg_catalog."default" NOT NULL,
    groups integer,
    configure character varying(255) COLLATE pg_catalog."default",
    head_id integer NOT NULL,
    current_address integer,
    permanent_address integer,
    CONSTRAINT users_user_pkey PRIMARY KEY (id),
    CONSTRAINT users_user_email_243f6e77_uniq UNIQUE (email)
);

CREATE TABLE IF NOT EXISTS public.users_user_user_permissions
(
    id bigint NOT NULL DEFAULT nextval('users_user_user_permissions_id_seq'::regclass),
    user_id bigint NOT NULL,
    permission_id integer NOT NULL,
    CONSTRAINT users_user_user_permissions_pkey PRIMARY KEY (id),
    CONSTRAINT users_user_user_permissions_user_id_permission_id_43338c45_uniq UNIQUE (user_id, permission_id)
);

CREATE TABLE IF NOT EXISTS public.vaccination_appointments_vaccinationappointment
(
    id bigint NOT NULL DEFAULT nextval('vaccination_appointments_vaccinationappointment_id_seq'::regclass),
    name character varying(255) COLLATE pg_catalog."default",
    "time" character varying(255) COLLATE pg_catalog."default",
    status character varying(255) COLLATE pg_catalog."default",
    date_created timestamp with time zone NOT NULL,
    date timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    category character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT vaccination_appointments_vaccinationappointment_pkey PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_user_id_2c513194_fk_users_user_id FOREIGN KEY (user_id)
    REFERENCES public.users_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS account_emailaddress_user_id_2c513194
    ON public.account_emailaddress(user_id);


ALTER TABLE IF EXISTS public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirm_email_address_id_5b7f8c58_fk_account_e FOREIGN KEY (email_address_id)
    REFERENCES public.account_emailaddress (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS account_emailconfirmation_email_address_id_5b7f8c58
    ON public.account_emailconfirmation(email_address_id);


ALTER TABLE IF EXISTS public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id)
    REFERENCES public.auth_permission (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS auth_group_permissions_permission_id_84c5c92e
    ON public.auth_group_permissions(permission_id);


ALTER TABLE IF EXISTS public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id)
    REFERENCES public.auth_group (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS auth_group_permissions_group_id_b120cbf9
    ON public.auth_group_permissions(group_id);


ALTER TABLE IF EXISTS public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id)
    REFERENCES public.django_content_type (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS auth_permission_content_type_id_2f476e4b
    ON public.auth_permission(content_type_id);


ALTER TABLE IF EXISTS public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_users_user_id FOREIGN KEY (user_id)
    REFERENCES public.users_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS authtoken_token_user_id_key
    ON public.authtoken_token(user_id);


ALTER TABLE IF EXISTS public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id)
    REFERENCES public.django_content_type (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS django_admin_log_content_type_id_c4bce8eb
    ON public.django_admin_log(content_type_id);


ALTER TABLE IF EXISTS public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_users_user_id FOREIGN KEY (user_id)
    REFERENCES public.users_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS django_admin_log_user_id_c564eba6
    ON public.django_admin_log(user_id);


ALTER TABLE IF EXISTS public.ih_appointment
    ADD CONSTRAINT ih_appointment_clinic_sched_id_fkey FOREIGN KEY (clinic_sched_id)
    REFERENCES public.ih_clinic_sched (clinic_sched_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.ih_appointment
    ADD CONSTRAINT ih_appointment_clinic_services_id_fkey FOREIGN KEY (clinic_services_id)
    REFERENCES public.ih_clinic_services (clinic_services_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.ih_appointment
    ADD CONSTRAINT ih_appointment_id_fkey FOREIGN KEY (id)
    REFERENCES public.users_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.ih_appointment
    ADD CONSTRAINT ih_appointment_resident_diagnosis_id_fkey FOREIGN KEY (resident_diagnosis_id)
    REFERENCES public.ih_resident_diagnosis (resident_diagnosis_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.ih_appointment
    ADD CONSTRAINT ih_appointment_vax_id_fkey FOREIGN KEY (vax_id)
    REFERENCES public.ih_vaccine (vax_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.ih_medicine_appointment
    ADD CONSTRAINT ih_medicine_appointment_clinic_sched_id_fkey FOREIGN KEY (clinic_sched_id)
    REFERENCES public.ih_clinic_sched (clinic_sched_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.ih_medicine_appointment
    ADD CONSTRAINT ih_medicine_appointment_id_fkey FOREIGN KEY (id)
    REFERENCES public.users_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.ih_medicine_appointment
    ADD CONSTRAINT ih_medicine_appointment_medicine_id_fkey FOREIGN KEY (medicine_id)
    REFERENCES public.ih_medicine (medicine_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.ih_priority_group
    ADD CONSTRAINT ih_priority_group_comorbidity_id_id_f604f620_fk_ih_comorb FOREIGN KEY (comorbidity_id_id)
    REFERENCES public.ih_comorbidity (comorbidity_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS ih_priority_group_comorbidity_id_id_f604f620
    ON public.ih_priority_group(comorbidity_id_id);


ALTER TABLE IF EXISTS public.socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_socialaccount_user_id_8146e70c_fk_users_user_id FOREIGN KEY (user_id)
    REFERENCES public.users_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS socialaccount_socialaccount_user_id_8146e70c
    ON public.socialaccount_socialaccount(user_id);


ALTER TABLE IF EXISTS public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_social_account_id_951f210e_fk_socialacc FOREIGN KEY (account_id)
    REFERENCES public.socialaccount_socialaccount (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS socialaccount_socialtoken_account_id_951f210e
    ON public.socialaccount_socialtoken(account_id);


ALTER TABLE IF EXISTS public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_social_app_id_636a42d7_fk_socialacc FOREIGN KEY (app_id)
    REFERENCES public.socialaccount_socialapp (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS socialaccount_socialtoken_app_id_636a42d7
    ON public.socialaccount_socialtoken(app_id);


ALTER TABLE IF EXISTS public.token_blacklist_blacklistedtoken
    ADD CONSTRAINT token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk FOREIGN KEY (token_id)
    REFERENCES public.token_blacklist_outstandingtoken (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS token_blacklist_blacklistedtoken_token_id_key
    ON public.token_blacklist_blacklistedtoken(token_id);


ALTER TABLE IF EXISTS public.token_blacklist_outstandingtoken
    ADD CONSTRAINT token_blacklist_outs_user_id_83bc629a_fk_users_use FOREIGN KEY (user_id)
    REFERENCES public.users_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS token_blacklist_outstandingtoken_user_id_83bc629a
    ON public.token_blacklist_outstandingtoken(user_id);


ALTER TABLE IF EXISTS public.users_user
    ADD CONSTRAINT users_user_prio_group_id_ef2864d6_fk_ih_priori FOREIGN KEY (prio_group_id)
    REFERENCES public.ih_priority_group (prio_group_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS users_user_prio_group_id_ef2864d6
    ON public.users_user(prio_group_id);


ALTER TABLE IF EXISTS public.users_user_user_permissions
    ADD CONSTRAINT users_user_user_perm_permission_id_0b93982e_fk_auth_perm FOREIGN KEY (permission_id)
    REFERENCES public.auth_permission (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS users_user_user_permissions_permission_id_0b93982e
    ON public.users_user_user_permissions(permission_id);


ALTER TABLE IF EXISTS public.users_user_user_permissions
    ADD CONSTRAINT users_user_user_permissions_user_id_20aca447_fk_users_user_id FOREIGN KEY (user_id)
    REFERENCES public.users_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS users_user_user_permissions_user_id_20aca447
    ON public.users_user_user_permissions(user_id);

END;