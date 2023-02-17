        function updateOptions() {
            var appt_type = document.getElementById("appt_type");
            var clinic_services_id = document.getElementById("clinic_services_id");
        
            clinic_services_id.innerHTML = "";
        
            if (appt_type.value === "clinic_service_id") {
            var option1 = document.createElement("option");
            option1.value = "1";
            option1.text = "check-up";
            clinic_services_id.add(option1);
        
            var option2 = document.createElement("option");
            option2.value = "2";
            option2.text = "x-ray";
            clinic_services_id.add(option2);
        
            var option3 = document.createElement("option");
            option3.value = "3";
            option3.text = "ultrasound";
            clinic_services_id.add(option3);
        
            var option4 = document.createElement("option");
            option4.value = "4";
            option4.text = "Hermatology";
            clinic_services_id.add(option4);
            } else if (appt_type.value === "dental_service_id") {
            var option1 = document.createElement("option");
            option1.value = "5";
            option1.text = "teeth cleaning";
            clinic_services_id.add(option1);
        
            var option2 = document.createElement("option");
            option2.value = "6";
            option2.text = "tooth extraction";
            clinic_services_id.add(option2);
        
            var option3 = document.createElement("option");
            option3.value = "7";
            option3.text = "root canal";
            clinic_services_id.add(option3);
            } else if (appt_type.value === "vax_id") {
            var option1 = document.createElement("option");
            option1.value = "8";
            option1.text = "COVID-19";
            clinic_services_id.add(option1);
        
            var option2 = document.createElement("option");
            option2.value = "9";
            option2.text = "flu";
            clinic_services_id.add(option2);
        
            var option3 = document.createElement("option");
            option3.value = "10";
            option3.text = "pneumonia";
            clinic_services_id.add(option3);
            }
    }
