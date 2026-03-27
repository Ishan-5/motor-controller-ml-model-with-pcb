# ⚡ Smart Motor Monitoring & Control System (ML + PCB + IoT Simulation)

## 🚀 Overview
This project is a **full-stack motor monitoring and control system** combining **custom PCB design, embedded system concepts, machine learning, and a real-time web dashboard**.

It simulates an intelligent system capable of monitoring motor parameters and predicting load conditions, with future scope for real hardware integration.

---

## 🧠 Key Features

### 🔌 Hardware Design (PCB)
- Designed complete motor driver circuit using **EasyEDA**
- Includes:
  - Relay-based bidirectional motor control
  - MOSFET-based PWM speed control
  - Sensor interfacing (Current, Voltage, Temperature)
- Deliverables:
  - ✅ Schematic Design  
  - ✅ 2D PCB Layout  
  - ✅ 3D PCB Visualization  
  - ✅ Multi-layer PCB (4-layer ready)

---

### 📡 Sensor System
- Simulated real-world sensors:
  - Current sensor (ACS712 concept)
  - Voltage divider circuit
  - Temperature sensor (LM35 concept)
- Designed for future integration with ESP32 ADC

---

### 🤖 Machine Learning
- Built ML model using **Random Forest Classifier**
- Predicts motor load:
  - LOW  
  - MEDIUM  
  - HIGH  
- Trained on structured sensor dataset

---

### 🌐 Web Dashboard (Flask)
- Real-time monitoring interface
- Features:
  - Live sensor values
  - ML-based load prediction
  - Interactive charts (Chart.js)
  - Dark theme UI
- Backend built using Flask API

---

## 🧱 System Architecture
PCB Sensors → ESP32 (future) → Flask API → ML Model → Dashboard UI

(Current version uses simulated sensor data for development and testing)

---

## 🛠 Tech Stack

- **Hardware Design**: EasyEDA  
- **Backend**: Flask (Python)  
- **Machine Learning**: Scikit-learn  
- **Frontend**: HTML, CSS, Chart.js  
- **Data Handling**: Pandas  

---

## 📊 Dashboard Features

- Real-time data visualization
- Multi-parameter graphs:
  - Current
  - Voltage
  - Temperature
- Load classification display
- Clean dark-themed UI

---

## 📁 Project Structure
project/
├── app.py
├── model.pkl
├── motor_data.csv
├── templates/
│ └── index.html
├── pcb/
│ ├── schematic.png
│ ├── pcb_2d.png
│ ├── pcb_3d.png
└── README.md

---

## 🔮 Future Improvements

- 🔁 Real ESP32 integration (WiFi + ADC)
- ⚡ RPM measurement using Hall sensor
- 🚨 Smart alert system (overload protection)
- 📱 Mobile-friendly UI
- 📡 IoT cloud integration

---

## 💡 Learning Outcomes

- PCB design and hardware system integration  
- Sensor interfacing concepts  
- Machine Learning for real-world signals  
- Backend API development  
- Frontend dashboard design  

---

## 📌 Conclusion

This project demonstrates the integration of **hardware + software + AI**, forming a complete intelligent monitoring system — similar to industrial IoT solutions.

---

## 👨‍💻 Author
**Devansh Kumar Pandey**
