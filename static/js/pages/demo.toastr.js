! function (i) {
	"use strict";
	i("#toastr-one").on("click", function (t) {
		i.NotificationApp.send("Heads up!", "This alert needs your attention, but it is not super important.", "top-right", "rgba(0,0,0,0.2)", "info")
	}), i("#toastr-two").on("click", function (t) {
		i.NotificationApp.send("Heads up!", "Check below fields please.", "top-center", "rgba(0,0,0,0.2)", "warning")
	}), i("#toastr-three").on("click", function (t) {
		i.NotificationApp.send("Appointment request has been approved", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-four").on("click", function (t) {
		i.NotificationApp.send("Appointment request has been declined!", "", "top-right", "rgba(0,0,0,0.2)", "error")
	}), i("#toastr-five").on("click", function (t) {
		i.NotificationApp.send("Resident updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-five2").on("click", function (t) {
		i.NotificationApp.send("Brgy official updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-six").on("click", function (t) {
		i.NotificationApp.send("Blotter updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-forreview").on("click", function (t) {
		i.NotificationApp.send("Blotter marked as for review!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-household").on("click", function (t) {
		i.NotificationApp.send("Household updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-addhousehold").on("click", function (t) {
		i.NotificationApp.send("Household added successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-reqblotter").on("click", function (t) {
		i.NotificationApp.send("Blotter requested successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-deletecert").on("click", function (t) {
		i.NotificationApp.send("Certificate deleted!", "", "top-right", "rgba(0,0,0,0.2)", "error")
	}), i("#toastr-deletepay").on("click", function (t) {
		i.NotificationApp.send("Payment deleted!", "", "top-right", "rgba(0,0,0,0.2)", "error")
	}), i("#toastr-updatecert").on("click", function (t) {
		i.NotificationApp.send("Certificate updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-addcert").on("click", function (t) {
		i.NotificationApp.send("Certificate added successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-updateid").on("click", function (t) {
		i.NotificationApp.send("ID updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-generateid").on("click", function (t) {
		i.NotificationApp.send("ID is being generated...", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-updatedinvoice").on("click", function (t) {
		i.NotificationApp.send("Invoice updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-addpayment").on("click", function (t) {
		i.NotificationApp.send("Payment added successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-edittheme").on("click", function (t) {
		i.NotificationApp.send("Theme updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-editevent").on("click", function (t) {
		i.NotificationApp.send("Event updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-editproject").on("click", function (t) {
		i.NotificationApp.send("Project updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-editaccount").on("click", function (t) {
		i.NotificationApp.send("Account updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-createevent").on("click", function (t) {
		i.NotificationApp.send("Event / Project created successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-updateadmin").on("click", function (t) {
		i.NotificationApp.send("Admin updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-updatesenior").on("click", function (t) {
		i.NotificationApp.send("Senior Citizen updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-updatepatient").on("click", function (t) {
		i.NotificationApp.send("Patient updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-staffupdate").on("click", function (t) {
		i.NotificationApp.send("Staff updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-hworkerupdate").on("click", function (t) {
		i.NotificationApp.send("Health Worker updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-pleaderupdate").on("click", function (t) {
		i.NotificationApp.send("Purok Leader updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-summon").on("click", function (t) {
		i.NotificationApp.send("Blotter marked as summon!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-settled").on("click", function (t) {
		i.NotificationApp.send("Blotter marked as settled!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-editreq").on("click", function (t) {
		i.NotificationApp.send("Request edited successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-joinevent").on("click", function (t) {
		i.NotificationApp.send("You joined the event successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-reqcert").on("click", function (t) {
		i.NotificationApp.send("Certificate requested successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-editpatient").on("click", function (t) {
		i.NotificationApp.send("Patient updated successfully!", "", "top-right", "rgba(0,0,0,0.2)", "success")
	}), i("#toastr-dismiss").on("click", function (t) {
		i.NotificationApp.send("Blotter marked as dismissed!", "", "top-right", "rgba(0,0,0,0.2)", "error")
	}), i("#toastr-cancelblotter").on("click", function (t) {
		i.NotificationApp.send("Blotter cancelled!", "", "top-right", "rgba(0,0,0,0.2)", "error")
	}), i("#toastr-cancelreq").on("click", function (t) {
		i.NotificationApp.send("Request cancelled!", "", "top-right", "rgba(0,0,0,0.2)", "error")
	}), i("#toastr-deleteid").on("click", function (t) {
		i.NotificationApp.send("ID deleted!", "", "top-right", "rgba(0,0,0,0.2)", "error")
	}), i("#toastr-endterm").on("click", function (t) {
		i.NotificationApp.send("Barangay official was terminated!", "", "top-right", "rgba(0,0,0,0.2)", "error")
	}), i("#toastr-eight").on("click", function (t) {
		i.NotificationApp.send("", "Set the `showHideTransition` property to fade|plain|slide to achieve different transitions.", "top-right", "rgba(0,0,0,0.2)", "info", 3e3, 1, "fade")
	})
}(window.jQuery);