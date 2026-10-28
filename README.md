# 🛡️ ZK Network

### A Secure Web Application with Hybrid Asymmetric Cryptography and Key Escrow

**ZK Network** is a secure messaging and social networking platform developed as a laboratory project for **CSE447: Cryptography and Cryptanalysis**. Built with Django and Django REST Framework, the application implements custom cryptographic engines to protect posts and direct messages through encryption, key management, and integrity verification.

🌐 **Live Demo:** [https://zero-knowledge-zk.vercel.app/](https://zero-knowledge-zk.vercel.app/)

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Cryptographic Architecture](#-cryptographic-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation and Setup](#️-installation-and-setup)
- [Running the Application](#-running-the-application)
- [Testing](#-testing)
- [Master Key Rotation](#-master-key-rotation)
- [Security Considerations](#️-security-considerations)
- [Academic Disclaimer](#-academic-disclaimer)

---

## 🔍 Overview

ZK Network explores the practical application of cryptographic concepts in a web-based messaging platform.

The application combines asymmetric encryption, elliptic curve cryptography (ECC), message authentication, and server-managed key escrow to protect stored communications.

Its primary objectives are to:

- Protect stored posts and direct messages through encryption.
- Implement cryptographic operations using custom-built mathematical engines.
- Maintain message integrity through HMAC-SHA256 authentication.
- Secure user authentication through time-limited email one-time passwords (OTPs).
- Manage cryptographic keys through a centralized server-side vault.
- Demonstrate authentication, authorization, and cryptographic integrity in a Django application.

## 🚀 Key Features

### 🔑 Server-Managed Key Escrow
- Generates and manages user RSA keypairs through a centralized server-side key vault.
- Uses a master key mechanism to protect user cryptographic keys.
- Performs key management and cryptographic operations on the server.

### 🔐 Hybrid Cryptographic Architecture
- **Encrypted Posts:** Uses a custom ECC implementation with an RSA-based key ring for post encryption and access control.
- **Secure Direct Messages:** Uses RSA-based encryption and server-mediated decryption for direct messaging.
- **Encrypted Storage:** Stores encrypted communication data rather than plaintext messages in the database.

### 🛡️ Message Integrity Protection
- Protects direct messages with HMAC-SHA256 authentication tags.
- Detects unauthorized modifications to message ciphertexts.
- Displays `[MESSAGE CORRUPTED]` when message integrity verification fails.

### 📧 Two-Factor Authentication
- Requires a time-limited email OTP as a secondary authentication step.
- Integrates OTP verification into the authentication and key-unwrapping workflow.

### 🎟️ JWT Authentication
- Implements custom JSON Web Token (JWT) authentication.
- Integrates token-based authentication with the application's login lifecycle.

### 👥 Role-Based Access Control
- Provides a dedicated Django administration interface.
- Supports administrative auditing and moderation.
- Separates administrative functions from ordinary user operations.

---

## 🔬 Cryptographic Architecture

ZK Network uses multiple cryptographic components to demonstrate how encryption, key management, and integrity verification can work together.

| Component | Purpose |
|---|---|
| RSA | Asymmetric encryption and cryptographic key management |
| ECC | Elliptic curve cryptography for the post encryption workflow |
| RSA Key Ring | Manages encrypted post access according to the application's key-management design |
| HMAC-SHA256 | Verifies the integrity and authenticity of direct messages |
| Master Key Vault | Protects and manages user cryptographic keys |
| JWT | Supports stateless, token-based authentication |
| Email OTP | Provides a secondary authentication step |

### Post Encryption

The post encryption workflow uses custom ECC functionality alongside an RSA-based key ring. This architecture is intended to protect stored posts and control access according to the application's encryption design.

### Direct Message Encryption

Direct messages use RSA-based encryption and server-mediated decryption. HMAC-SHA256 tags provide an additional integrity check to detect unauthorized ciphertext modifications.

### Key Management

The server manages user keypairs through a master key vault. This approach demonstrates centralized key escrow, where the server retains capabilities needed to manage or unwrap protected user keys.

**Note:** Server-managed key escrow is not equivalent to end-to-end encryption in which the server cannot access plaintext. The security properties depend on the implementation and key-access controls.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Backend | Python, Django 6.0.4 |
| API Framework | Django REST Framework |
| Database | SQLite3 |
| Cryptography | Custom RSA, ECC, hashing, and MAC engines |
| Cryptographic Primitives | PyCryptodome |
| Authentication | Custom JWT authentication, email OTP |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript |
| Environment Configuration | Python dotenv |
| Deployment | Vercel |

### Custom Cryptographic Modules

The project includes custom cryptographic components organized around the following engines:

- `rsa_core` — RSA-related operations.
- `ecc_core` — Elliptic curve cryptography.
- `hash_core` — Hashing functionality.
- `mac_core` — Message authentication code operations.

PyCryptodome is used for underlying mathematical primitives, as specified in the project's implementation design.

---

## 📁 Project Structure

The following is a conceptual overview of the main components. Adjust the paths to match the actual repository structure.

```text
zk-network/
│
├── accounts/                 # User accounts and authentication
├── network/                   # Posts and messaging functionality
├── crypto_engine/             # Cryptographic implementations
│   ├── rsa_core               # RSA operations
│   ├── ecc_core               # ECC operations
│   ├── hash_core              # Hashing functionality
│   └── mac_core               # Message authentication
│
├── zk_core/                   # Django project configuration
│   ├── settings.py            # Application settings
│   ├── urls.py                # URL routing
│   ├── wsgi.py                # WSGI configuration
│   └──
│
├── templates/                 # HTML templates
├── static/                    # CSS, JavaScript, and static assets
├── manage.py                  # Django management utility
├── test_post_e2e.py           # Post encryption end-to-end tests
├── test_dm_e2e.py             # Direct message end-to-end tests
├── requirements.txt           # Python dependencies
├── .env                       # Local environment variables (not committed)
└── README.md
```

> **Note:** This structure is illustrative. Confirm the actual module paths and filenames in your repository before using it as an exact directory listing.

---

## ⚙️ Installation and Setup

Follow these steps to run ZK Network locally.

### Prerequisites

Install the following:

- Python 3.10 or later.
- Git.
- pip, Python's package installer.

### 1. Clone the Repository

Replace the placeholder repository URL with your actual GitHub repository URL.

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd zk-network
```

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

If your repository contains a `requirements.txt` file, install the project dependencies using:

```bash
pip install -r requirements.txt
```

Otherwise, install the core dependencies:

```bash
pip install django==6.0.4 djangorestframework pycryptodome python-dotenv
```

Additional dependencies may be required depending on your project's implementation.

### 4. Configure Environment Variables

Create a `.env` file in the project root, alongside `manage.py`.

The application uses environment variables for Django configuration and cryptographic key management.

Example configuration:

```dotenv
SECRET_KEY=your-local-django-secret-key
DEBUG=True
DM_MAC_SECRET=your-local-mac-secret
SERVER_RSA_PUBLIC_KEY=your-public-key-configuration
SERVER_RSA_PRIVATE_KEY=your-private-key-configuration
```

**Important:**

- Use valid values compatible with the application's expected key formats.
- The RSA key variables must match the formats expected by your custom cryptographic implementation.
- Do not commit `.env` to GitHub.
- Do not use production secrets in your local development environment.
- Configure separate, secure environment variables for deployment.

The application settings must explicitly read the appropriate environment variables. Variable names in `.env` alone do not configure Django automatically.

### 5. Initialize the Database

Run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an administrator account if required:

```bash
python manage.py createsuperuser
```

Follow the prompts to configure the administrator credentials.

---

## ▶️ Running the Application

Start the Django development server:

```bash
python manage.py runserver
```

Open the application in your browser:

**Local application:** http://127.0.0.1:8000/

The Django administration interface is generally available at:

http://127.0.0.1:8000/admin/

The exact routes depend on the project's URL configuration.

If your project includes a startup vault-verification utility, run or configure it according to the implementation's instructions before using the cryptographic features.

---

## 🧪 Testing

ZK Network includes end-to-end test scripts for post encryption and direct messaging.

Run the post encryption tests:

```bash
python test_post_e2e.py
```

Run the direct messaging tests:

```bash
python test_dm_e2e.py
```

These tests are intended to validate the cryptographic workflows and related application behavior implemented by the project.

For more comprehensive verification, tests should also cover:

- RSA key generation and encryption/decryption.
- ECC encryption and decryption workflows.
- Message authentication and ciphertext tampering.
- Authentication and OTP verification.
- JWT validation and authorization.
- Access control for posts and direct messages.
- Key storage and key-unwrapping operations.

The actual test coverage depends on the test cases implemented in the repository.

---

## 🔄 Master Key Rotation

ZK Network's design includes a management workflow for rotating master RSA keys.

If the project implements the `rotate_master_keys` Django management command, run:

```bash
python manage.py rotate_master_keys
```

Follow the command's prompts and instructions.

**Before rotating keys:**

1. Back up the database and current key material securely.
2. Confirm that the rotation command supports all encrypted records in your database.
3. Ensure that existing user keys and encrypted messages remain recoverable.
4. Securely update the relevant environment variables.
5. Test decryption and message integrity after rotation.

**Warning:** Incorrect key rotation can make encrypted data permanently inaccessible. Only perform this operation after reviewing the implementation and verifying your backups.

---

## ☁️ Live Deployment

ZK Network is deployed on Vercel.

🌐 **Visit the application:** [https://zero-knowledge-zk.vercel.app/](https://zero-knowledge-zk.vercel.app/)

The deployed application's available features depend on its current configuration and deployment environment.

---

## ⚠️ Security Considerations

This project demonstrates cryptographic concepts for academic learning. Its architecture should not be interpreted as proof of production-grade security.

Important considerations include:

- **Key escrow:** Server-managed keys introduce trust in the server and its key-management infrastructure.
- **Cryptographic implementation:** Custom cryptographic engines require independent review and rigorous testing.
- **Key storage:** Master keys and private keys must be protected against unauthorized access.
- **Authentication:** OTP delivery, JWT validation, session management, and account recovery require careful security controls.
- **Database persistence:** SQLite on a serverless deployment may not provide reliable persistent storage for application data.
- **Deployment configuration:** Production deployments must use secure secrets, disable Django debug mode, and configure allowed hosts and CSRF protections appropriately.
- **Email delivery:** A console-based email backend is suitable for development testing but does not provide actual email delivery to users.

The actual security guarantees depend on the implemented algorithms, key management, configuration, and testing.

---

## 🎓 Academic Disclaimer

ZK Network was developed as an educational project for **CSE447: Cryptography and Cryptanalysis**.

The project demonstrates the implementation and integration of cryptographic concepts, including RSA, ECC, hashing, message authentication, and key escrow, within a Django web application.

The custom cryptographic implementations have not necessarily undergone independent professional security audits. The project is intended for educational and demonstration purposes and **should not be used to protect real-world sensitive information without comprehensive security review and testing**.

---

## 👨‍💻 Project Information

**Project:** ZK Network  
**Course:** CSE447 — Cryptography and Cryptanalysis  
**Framework:** Django  
**Deployment:** Vercel  
**Live Demo:** [zero-knowledge-zk.vercel.app](https://zero-knowledge-zk.vercel.app/)

---
