#  FinancePro | Full-Stack Financial Intelligence Dashboard

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

##  Overview
**FinancePro** is a secure, personal finance management tool designed to bridge the gap between raw transaction data and actionable insights. Built with a robust Python backend, it allows users to manage their wealth, set savings milestones, and visualize spending habits through an automated analytics engine.

### Why this project?
Most trackers are either too simple (spreadsheets) or too invasive. FinancePro demonstrates a **privacy-first approach** to fintech, using local database encryption logic and server-side rendering to keep user data secure and fast.

---

##  Core Features
* **Secure Authentication:** Full user lifecycle management (Register/Login/Logout) using session-based security.
* **Dynamic Data Viz:** Real-time generation of spending distribution charts using **Matplotlib**.
* **Smart Budgeting:** A dedicated system for setting financial goals with visual progress tracking.
* **Currency Agnostic:** Built-in logic to handle multiple currency formats and transaction categories.
* **Zero-JS UI:** A high-performance, mobile-responsive interface built entirely with optimized CSS.

---

## 🛠️ Technical Architecture
* **Backend:** Python / Flask
* **Database:** SQLAlchemy ORM (Relational SQLite)
* **Security:** Flask-Login & Password Hashing
* **Frontend:** HTML5 / CSS3 (Flexbox & Grid)
* **Analysis:** Matplotlib for automated report generation

---

##  Technical Implementation Highlights
1.  **Relational Data Modeling:** Implemented complex database relationships where each `User` owns multiple `Expenses` and `Goals`, ensuring strict data isolation.
2.  **Server-Side Logic:** Developed backend routes to calculate real-time balances and budget remainders before rendering to the client.
3.  **Scalable CSS:** Used CSS variables and modular design patterns to ensure the dashboard looks professional on desktop, tablet, and mobile.

---

##  How to Run Locally
1. Clone the repo:
   `git clone https://github.com/YOUR_USERNAME/FinanceTracker-Pro.git`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the application:
   `python app.py`
4. Visit: `http://127.0.0.1:5000`

   ## View live Demo {https://financepro-uzut.onrender.com}

---
**Developed by Jose David Ndong Mba** *Looking to build secure, data-driven solutions.*
