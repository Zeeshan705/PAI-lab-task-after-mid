from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

responses = {
    "appointment": [
        "To book an appointment, please call us at 0300-1234567 or visit our reception desk between 8 AM and 6 PM.",
        "You can schedule an appointment online through our patient portal or by calling our helpline.",
        "Our appointment slots are available Monday to Saturday. Walk-ins are also welcome before 12 PM."
    ],
    "doctor": [
        "Our medical staff includes Dr. Ahmed (Cardiologist), Dr. Sara (Neurologist), Dr. Bilal (Orthopedic), and Dr. Nadia (General Physician).",
        "All our doctors are PMDC registered with 10+ years of experience. Would you like to know about a specific specialist?",
        "You can request a specific doctor when booking your appointment. Availability depends on their schedule."
    ],
    "department": [
        "We have the following departments: Cardiology, Neurology, Orthopedics, Pediatrics, Gynecology, and Emergency.",
        "Our hospital has 12 specialized departments including Oncology, Radiology, and Physiotherapy.",
        "Each department is equipped with modern diagnostic tools. Which department are you looking for?"
    ],
    "emergency": [
        "Our emergency department is open 24/7. Please call 1122 or visit us directly for urgent cases.",
        "Emergency services are available round the clock. Our trauma team is always on standby.",
        "For life-threatening emergencies, call 1122 immediately. Our ER is located at the main entrance."
    ],
    "timing": [
        "OPD timings are Monday to Saturday, 8 AM to 8 PM. Emergency is open 24/7.",
        "Our lab and pharmacy are open from 7 AM to 10 PM daily including Sundays.",
        "Doctor consultation hours vary by department. General OPD opens at 9 AM every weekday."
    ],
    "fee": [
        "General consultation fee is Rs. 500. Specialist consultation starts from Rs. 1000 to Rs. 2500.",
        "Our fee structure varies by department. Lab tests and diagnostic services have separate charges.",
        "We accept cash, card, and insurance. Zakat patients may be eligible for free treatment."
    ],
    "location": [
        "We are located at Main Boulevard, Gulberg III, Lahore. Easily accessible from all major routes.",
        "Our hospital is near Liberty Chowk, Lahore. Parking is available on the premises.",
        "You can find us on Google Maps by searching 'MediCare Hospital Lahore'. Free shuttle service available."
    ],
    "insurance": [
        "We are affiliated with Jubilee Insurance, EFU, and State Life. Please bring your card when visiting.",
        "Our hospital accepts most major insurance providers. Contact our billing department for details.",
        "Sehat Sahulat Program and government health cards are also accepted at our facility."
    ],
    "lab": [
        "Our diagnostic lab offers blood tests, urine analysis, X-ray, ultrasound, MRI, and CT scan.",
        "Lab results are typically available within 24 hours. Urgent reports can be provided in 4 to 6 hours.",
        "You can collect your lab reports from the reception or receive them via WhatsApp upon request."
    ],
    "pharmacy": [
        "Our in-house pharmacy stocks a wide range of medicines and is open from 7 AM to 11 PM.",
        "Medicines prescribed by our doctors are available at discounted rates in our pharmacy.",
        "For home delivery of medicines, call 0311-9876543. Delivery available within 10 km radius."
    ]
}

greetings = ["hello", "hi", "hey", "salam", "assalam", "good morning", "good evening", "howdy"]
farewells = ["bye", "goodbye", "thanks", "thank you", "shukriya", "ok bye", "that's all"]

def get_response(message):
    msg = message.lower().strip()
    
    for word in greetings:
        if word in msg:
            return "Hello! Welcome to MediCare Hospital. How can I assist you today? You can ask about appointments, doctors, departments, fees, timings, lab tests, pharmacy, or emergency services."
    
    for word in farewells:
        if word in msg:
            return "Thank you for contacting MediCare Hospital. We wish you good health. Take care!"
    
    if any(w in msg for w in ["appointment", "book", "schedule", "visit"]):
        return random.choice(responses["appointment"])
    
    if any(w in msg for w in ["doctor", "specialist", "physician", "surgeon", "consultant"]):
        return random.choice(responses["doctor"])
    
    if any(w in msg for w in ["department", "ward", "unit", "section"]):
        return random.choice(responses["department"])
    
    if any(w in msg for w in ["emergency", "urgent", "accident", "critical", "ambulance"]):
        return random.choice(responses["emergency"])
    
    if any(w in msg for w in ["timing", "time", "hours", "open", "close", "schedule"]):
        return random.choice(responses["timing"])
    
    if any(w in msg for w in ["fee", "cost", "charges", "price", "payment", "rate"]):
        return random.choice(responses["fee"])
    
    if any(w in msg for w in ["location", "address", "where", "direction", "map", "place"]):
        return random.choice(responses["location"])
    
    if any(w in msg for w in ["insurance", "sehat", "card", "coverage"]):
        return random.choice(responses["insurance"])
    
    if any(w in msg for w in ["lab", "test", "xray", "x-ray", "mri", "scan", "blood", "report", "result"]):
        return random.choice(responses["lab"])
    
    if any(w in msg for w in ["pharmacy", "medicine", "drug", "tablet", "prescription"]):
        return random.choice(responses["pharmacy"])
    
    return "I am sorry, I did not quite understand that. You can ask me about appointments, doctors, departments, fees, timings, emergency, lab tests, pharmacy, insurance, or our location."


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    reply = get_response(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
