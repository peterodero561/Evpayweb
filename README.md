# Evpay

## Introduction

Welcome to **EvPay** – the **Electric Vehicle Payment System**.

EvPay is designed to streamline operations and foster seamless interactions between electric vehicle users, drivers, and garage managers. It serves as a comprehensive platform where:
- **Users** can create profiles, make payments for bus fares, and enjoy a convenient and cashless travel experience.
- **Drivers** can register their buses, manage payment transactions, and make service payments to garages effortlessly.
- **Garage** Managers can create profiles to register their garages, list services offered, and receive payments from drivers efficiently.

By integrating user-friendly profiles, a robust payment system, and tailored features for each role, EvPay simplifies the complexities of fare management and service payments. The platform ensures a smoother experience for electric vehicle transportation while promoting accountability and transparency among stakeholders.

Whether you're a commuter, a driver managing your fleet, or a garage manager offering essential services, EvPay is here to meet your needs with reliability and efficiency.

## Features

#### I) User Profiles
- Users (drivers and garage managers) can create personalized profiles.
- Profile management includes the ability to update personal information, contact details, and preferences.

#### II) Driver Vehicle Management
- Drivers can register their electric vehicles (buses) on the platform.
- Drivers can manage vehicle details, including bus type, and capacity

#### III) Garage Registration
- Garage managers can create profiles to register their garages and list the services offered.
- The system allows garage managers to track services

#### IV) Fare Payment System
- Users can pay bus fares directly through the platform, using integrated payment gateways.


## Getting Started
#### a) Prerequissites

Before you begin, ensure you have the following installed on your local machine:
- Python 3.8+: The project is built using Python.
- pip3: Python's package installer.
- Git: Version control for managing the project's code.

#### b) Clone repository
```
git clone https://github.com/peterodero561/evpay
cd evpay
```

#### c) Setup virtual environment
```
python3 -m venv evpay
source evpay/bin/activate
```

#### d) Install dependancies
```
pip3 install -r requirements.txt
```

#### e) Initialize database
```
flask db init
flask db migrate
flask db upgrade
```

#### f) Run server and access application
```
python3 manage_app.py
```

The application should now be accessible at http://127.0.0.1:5000/auth in your web browser.
