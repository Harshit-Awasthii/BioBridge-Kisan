BioBridge Kisan

A Smart Agriculture Assistance Platform

🚀 Overview

BioBridge Kisan is a full-stack web application designed to assist farmers in making data-driven agricultural decisions. It bridges the gap between farmers and scientific insights by integrating AI-based crop recommendations, real-time weather data, and digital farm record management.

🎯 Key Features
🌱 AI Crop Recommendation
Uses a Decision Tree model to suggest suitable crops based on soil and environmental conditions.
🌦️ Weather Integration
Displays real-time weather data to help farmers plan agricultural activities.
👨‍🌾 Multi-User Roles
Farmer: Input soil data, get crop suggestions
Scientist: Analyze and manage data
Admin: Monitor and control the system
🔐 Authentication & Protected Routes
Secure login and role-based dashboard access.
☁️ Cloud Database (Firebase Firestore)
Stores user data, farm records, and recommendations efficiently.
📊 Dashboard UI
Interactive dashboard for viewing results, weather, and saved farm data.
🛠️ Tech Stack

Frontend:

React.js (Vite)
CSS / Bootstrap

Backend:

Python Flask

Database:

Firebase Firestore

Machine Learning:

Decision Tree Algorithm (Scikit-learn)

APIs:

Weather API
⚙️ How It Works
User registers and logs in
Farmer enters soil and environmental data
Data is sent to Flask backend
ML model processes input and predicts suitable crops
Results are displayed on dashboard
Data is stored in Firestore for future reference
