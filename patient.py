from flask import Flask, jsonify, request

app = Flask(__name__)

# data for doctors
doctors = [
    {
        "id": 1,
        "name": "Dr. Smith",
        "specialty": "Cardiologist",
        "available_days": ["Monday", "Wednesday", "Friday"],
        "max_patients": 5
    },
    {
        "id": 2,
        "name": "Dr. Johnson",
        "specialty": "Dermatologist",
        "available_days": ["Tuesday", "Thursday", "Saturday"],
        "max_patients": 5
    }
]

# Endpoint for all doctors
@app.route('/doctors', methods=['GET'])
def get_doctors():
    return jsonify(doctors)

# Endpoint for doctor detail
@app.route('/doctor/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = next((doc for doc in doctors if doc["id"] == doctor_id), None)
    if doctor:
        return jsonify(doctor)
    else:
        return jsonify({"error": "Doctor not found"}), 404

# Endpoint for checking doctor's availability
@app.route('/doctor/<int:doctor_id>/availability', methods=['GET'])
def get_doctor_availability(doctor_id):
    # Dummy implementation, assuming all evenings are available
    return jsonify({"available_slots": ["5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM"]})

# Endpoint for booking appointment
@app.route('/book-appointment', methods=['POST'])
def book_appointment():
    data = request.json
    doctor_id = data.get('doctor_id')
    slot = data.get('slot')
    # Dummy implementation, assuming booking is successful
    return jsonify({"message": f"Appointment booked with Doctor {doctor_id} at {slot}"}), 200

if __name__ == '__main__':
    app.run(debug=True)
