# 🌿 VedaCare - AI-Powered Ayurvedic Wellness Platform

![VedaCare Banner](vedacare_backend/static/images/hero-bg.jpg) *(Optional: Placeholder for banner)*

VedaCare is a comprehensive **Ayurvedic Health & Herbal Identification Platform** designed to bridge the gap between ancient Ayurvedic wisdom and modern technology. Using machine learning and intelligent keyword matching, VedaCare helps users identify medicinal plants, predict potential health conditions based on symptoms, and shop for herbal remedies.

---

## ✨ Key Features

### 🔍 1. AI Plant Identification
- **Real-time Scanner**: Identify herbal plants using your camera or by uploading a photo.
- **Powered by Plant.id**: Integrates with the Plant.id API for high-accuracy botanical identification.
- **Deep Database Matching**: Automatically maps identified plants to local Ayurvedic properties, medicinal uses, and preparation methods.

### 🩺 2. Symptom Checker & Disease Prediction
- **Intelligent Analysis**: Enter your symptoms (e.g., "dry skin, anxious, cold") to receive an Ayurvedic diagnosis (e.g., Vata Imbalance).
- **Remedy Recommendations**: Get personalized preparation methods and recommended herbal plants for your specific condition.
- **Health Reports**: All analyses are saved to your history for future reference.

### 📚 3. Herbal Library
- **Comprehensive Database**: Explore a rich library of Ayurvedic plants like Tulsi, Ashwagandha, and Giloy.
- **Detailed Profiles**: Learn about medicinal uses, properties (Rasa, Guna, Virya), habitats, and precautions.
- **Searchable**: Real-time filtering to find the right herb for any ailment.

### 🛒 4. E-Kart (Herbal Shop)
- **Seamless Shopping**: Buy premium herbal products directly from the platform.
- **Cart Management**: LocalStorage-persisted shopping cart for a smooth checkout experience.
- **Order Tracking**: Monitor your order status from "Placed" to "Delivered."

### 📊 5. Admin Analytics & Management
- **Sales Reports**: Generate detailed PDF sales reports with charts and summaries.
- **Health Insights**: Track common ailments trending among users.
- **Content Management**: Full control over the plant database, conditions, and user base.

### 🔔 6. Smart Notifications
- **Status Updates**: Get alerted when your health analysis is ready or an order is confirmed.
- **Broadcasts**: Admin-led notifications for health tips or platform updates.

---

## 🛠️ Technology Stack

- **Backend**: [Django 4.2](https://www.djangoproject.com/) (Python 3.x)
- **Database**: SQLite3 (Development)
- **AI/ML**: [Plant.id API](https://plant.id/) for botanical vision, Custom Keyword Engine for Ayurvedic logic.
- **Frontend**: 
    - **UI/UX**: Vanilla CSS3 with **Modern Glassmorphism** & Premium Design System.
    - **Logic**: Vanilla JavaScript (ES6+).
    - **Icons**: Font Awesome 6.
- **Reporting**: ReportLab (PDF Generation).

---

## 🚀 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/VEDACARE_ML.git
   cd VEDACARE_ML
   ```

2. **Setup Virtual Environment**
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   *(Ensure you have a requirements.txt, or install manually)*
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Migrations**
   ```bash
   cd vedacare_backend
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser (For Admin Access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**
   ```bash
   python manage.py run_server
   ```
   Visit `http://127.0.0.1:8000` in your browser.

---

## 📂 Project Structure

```text
VEDACARE_ML/
├── vedacare_backend/       # Main Django Project
│   ├── core/               # Main Application Logic (Models, Views, AI Engine)
│   ├── static/             # CSS (Design System), JS, Images
│   ├── templates/          # Modern Glassmorphism HTML templates
│   ├── media/              # User-uploaded plant images
│   └── manage.py           # Django CLI
├── venv/                   # Virtual Environment
└── README.md               # You are here!
```

---

## 🎨 Design Philosophy

VedaCare features a **Premium Nature-Inspired UI**:
- **Color Palette**: Deep Forest Greens (#14532d), Emerald Accents, and Soft Healing Gradients.
- **Glassmorphism**: Backdrop blurs and translucent cards for a modern, airy feel.
- **Micro-interactions**: Subtle hover scales, pulsing animations, and staggered list entries.

---

## 📝 License
This project is for educational purposes. All herbal information should be verified by a certified Ayurvedic practitioner.

---
**Developed with ❤️ for Ayurvedic Wellness.**
