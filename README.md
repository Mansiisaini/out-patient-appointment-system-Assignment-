# out-patient-appointment-system-Assignment-

Explainations of code

1.Imports:
from flask import Flask, jsonify, request

Flask: This imports the Flask class, which we use to create our web application.
jsonify: This function converts Python dictionaries into JSON format, which is useful for returning responses from our API.
request: This object allows us to access data sent with the request, such as form data or JSON payloads.

2.Create Flask App:

app = Flask(__name__)

This line initializes a Flask application. __name__ is a special variable in Python that represents the name of the current module.

 3.Data for Doctors:

doctors = [
    {
        "id": 1,
        "name": "Dr. sita",
        "specialty": "Cardiologist",
        "available_days": ["Monday", "Wednesday", "Friday"],
        "max_patients": 5
    },
    {
        "id": 2,
        "name": "Dr. verma",
        "specialty": "Dermatologist",
        "available_days": ["Tuesday", "Thursday", "Saturday"],
        "max_patients": 5
    }
]
This is a list of dictionaries, each representing a doctor. Each dictionary contains information such as the doctor's ID, name, specialty, available days, and maximum number of patients.

4.Define Endpoints:
Doctors Listing (/doctors):

@app.route('/doctors', methods=['GET'])
def get_doctors():
    return jsonify(doctors)
This endpoint returns the list of all doctors when a GET request is made to /doctors.
Doctor Detail Page (/doctor/<int:doctor_id>):

@app.route('/doctor/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = next((doc for doc in doctors if doc["id"] == doctor_id), None)
    if doctor:
        return jsonify(doctor)
    else:
        return jsonify({"error": "Doctor not found"}), 404
This endpoint returns detailed information about a specific doctor when a GET request is made to /doctor/<doctor_id>, where <doctor_id> is the ID of the doctor.
Availability (/doctor/<int:doctor_id>/availability):

@app.route('/doctor/<int:doctor_id>/availability', methods=['GET'])
def get_doctor_availability(doctor_id):
    # Dummy implementation, assuming all evenings are available
    return jsonify({"available_slots": ["5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM"]})
This endpoint returns available time slots for a specific doctor when a GET request is made to /doctor/<doctor_id>/availability.
Appointment Booking (/book-appointment):

@app.route('/book-appointment', methods=['POST'])
def book_appointment():
    data = request.json
    doctor_id = data.get('doctor_id')
    slot = data.get('slot')
    # Dummy implementation, assuming booking is successful
    return jsonify({"message": f"Appointment booked with Doctor {doctor_id} at {slot}"}), 200
This endpoint allows booking an appointment with a doctor when a POST request is made to /book-appointment. The doctor's ID and desired time slot are extracted from the request JSON payload, and a success message is returned.

5.Run the Application:
if __name__ == '__main__':
    app.run(debug=True)
This block ensures that the Flask application runs when the script is executed directly (__name__ == '__main__'). It runs the Flask development server with debugging enabled.
