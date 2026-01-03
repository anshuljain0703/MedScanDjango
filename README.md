# MedScanAI: Intelligent Chest X-Ray Diagnosis System

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Django](https://img.shields.io/badge/Framework-Django%205.2-green.svg)
![TensorFlow](https://img.shields.io/badge/AI-TensorFlow%202.x-orange.svg)

**MedScanAI** is a robust medical imaging platform that leverages Deep Learning to assist in the early detection of respiratory diseases. By analyzing Chest X-Ray images, the system provides instant AI-driven predictions and facilitates a professional verification workflow between patients and doctors.

---

## 🚀 Key Features

### 1. Dual-Role Ecosystem
- **Patient Portal:** Upload scans, view AI predictions in real-time, and track medical history.
- **Doctor Dashboard:** Centralized hub for medical professionals to review, comment on, and verify AI-generated reports.

### 2. AI-Powered Diagnosis
- **Detection Capabilities:** Detects **COVID-19**, **Pneumonia (Bacterial & Viral)**, and **Tuberculosis** with high confidence.
- **Visual Feedback:** Shows prediction confidence percentages to help users understand the reliability of the result.

### 3. Professional Reporting
- **PDF Generation:** Automatically generates a detailed, professional medical report using the `ReportLab` engine.
- **Verification Workflow:** Reports transition from "Pending" to "Verified" once a doctor adds their expert analysis and digital sign-off.

### 4. Modern User Interface
- **Glassmorphism Design:** A sleek, responsive, and intuitive interface built with modern CSS techniques.
- **Interactive States:** Subtle micro-animations and hover effects for a premium user experience.

---

## 🛠️ Technology Stack

- **Backend:** [Django](https://www.djangoproject.com/) (Python)
- **Deep Learning:** [TensorFlow](https://www.tensorflow.org/) / Keras
- **PDF Engine:** ReportLab
- **Database:** SQLite (Development)
- **Frontend:** Semantic HTML5, Vanilla CSS3 (Custom Glassmorphism)

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.10+
- Pip (Python Package Manager)

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/anshuljain0703/MedScanDjango
   cd MedscanAntigravity/medscan_project
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the App**
   Open your browser and navigate to `http://127.0.0.1:8000`.

---

## 📖 Usage Guide

### For Patients
1. **Sign Up:** Create an account and select the **Patient** role.
2. **Upload Scan:** Go to the home page and upload a high-quality Chest X-Ray (JPEG/PNG).
3. **View Result:** Get instant AI grading and download your auto-generated PDF report.
4. **History:** Access previous scans and check if a doctor has verified them.

### For Doctors
1. **Sign Up/Login:** Use your credentials and select the **Doctor** role.
2. **Dashboard:** Browse through pending reports uploaded by patients.
3. **Verification:** Click on a report to review the image and AI prediction. Add your professional diagnosis and click **Verify**.

---

## 📁 Project Structure

```text
medscan_project/
├── scanner/                # Core application logic
│   ├── ml_model/           # AI model and predictor scripts
│   ├── utils/              # PDF generation and helper tools
│   ├── static/             # CSS, JS, and global assets
│   ├── templates/          # HTML views (Home, Dashboard, Login, etc.)
│   └── models.py           # Database schemas (Profile, MedicalReport)
├── media/                  # Stores uploaded X-rays and generated reports
├── medscan_project/        # Project configuration (settings, URLs)
└── manage.py               # Django management script
```

---

## 🛡️ License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📧 Contact

For any queries or professional collaboration, please reach out via the repository's issue tracker.
