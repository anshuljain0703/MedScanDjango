# MedScanAI - Project Walkthrough

## 1. Project Overview
**MedScanAI** is an advanced web application designed to assist medical diagnosis using Artificial Intelligence. It allows patients to upload Chest X-Ray images, which are then analyzed by a Deep Learning model to detect diseases like **Pneumonia**, **COVID-19**, and **Tuberculosis**.

The system features a **Dual-Role Workflow**:
- **Patients** upload scans and receive instant AI grading.
- **Doctors** review these AI-generated reports, add their expert analysis, and verify the diagnosis.

---

## 2. Technology Stack
This project is built using industry-standard technologies:
- **Backend Framework:** Django (Python) - Handles the server logic, security, and database.
- **AI/ML Engine:** TensorFlow & Keras - Runs the Convolutional Neural Network (CNN) for image analysis.
- **Database:** SQLite - Stores user profiles, reports, and verification status.
- **Frontend:** HTML5, CSS3 (Modern Glassmorphism Design) - Provides a responsive user interface.
- **PDF Engine:** ReportLab - Generates professional medical PDF reports on the fly.

---

## 3. How It Works (The Core Logic)

### A. The "Brain" (AI Model)
- **Location:** `scanner/ml_model/predictor.py` + `model_25_epoch.h5`
- **Process:**
    1. An image is uploaded by the user.
    2. The system resizes it to **256x256 pixels** (the size the "brain" understands).
    3. It "normalizes" the image (converts colors to numbers between 0 and 1).
    4. The model calculates the probability for 5 diseases:
       - Bacterial Pneumonia
       - COVID-19
       - Normal
       - Tuberculosis
       - Viral Pneumonia
    5. It returns the highest probability as the **Prediction**.

### B. The Workflow
1. **Authentication (`views.py`)**: 
   - Users sign up as either a **Patient** or a **Doctor**.
   - Django's built-in Auth system secures passwords and sessions.

2. **Patient Action**:
   - Patient uploads an X-Ray on the `home` page.
   - Django saves the image to the `media/` folder.
   - The **Predictor** analyzes the image.
   - The **Report Generator** (`utils/report_generator.py`) creates a detailed PDF.
   - The result is saved to the **Database** (`models.py`) with status `Pending`.

3. **Doctor Action**:
   - Doctor logs in and sees the **Dashboard**.
   - They see a list of all "Pending" reports.
   - They click **Verify**, review the X-Ray and AI prediction.
   - They add their **Professional Comments** and sign off.
   - The report status updates to **Verified**.

4. **Completion**:
   - The Patient sees the doctor's comments and the "Verified" badge in their history.

---

## 4. Key Files & Structure

| File/Folder | Purpose |
|-------------|---------|
| `manage.py` | The command-center script to run the server. |
| `db.sqlite3` | The database file containing all users and reports. |
| **`scanner/`** | **The Main Application Folder** |
| `├── models.py` | Defines the data structure (Tables: `Profile`, `MedicalReport`). |
| `├── views.py` | The logic controller (Handles clicks, uploads, and page rendering). |
| `├── urls.py` | The URL router (Connects web addresses like `/signup` to views). |
| `├── ml_model/` | Contains the AI Brain (`predictor.py` and the `.h5` model file). |
| `├── templates/` | HTML files for the website appearance. |
| `├── static/` | CSS files for styling and colors. |
| `└── utils/` | Helper scripts (e.g., `report_generator.py` for PDFs). |

---

## 5. Security & Professionalism
- **Login Required:** Pages cannot be accessed without logging in.
- **Role Protection:** Patients cannot access the Doctor Dashboard.
- **Data Integrity:** Verification stamps are time-locked and linked to the specific Doctor account.
- **Standardization:** Input images are standardized before analysis to ensure accuracy.

---

## 6. How to Run
1. Open Terminal in the project folder.
2. Run `python manage.py runserver`.
3. Open browser at `http://127.0.0.1:8000`.
