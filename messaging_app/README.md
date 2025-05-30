# Messaging App

A simple Django-based messaging application that allows users to send and receive messages in real time.

## Features

- User registration and authentication
- One-to-one and group conversations
- Real-time messaging
- Message read/unread status
- RESTful API using Django REST Framework

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- Virtualenv (recommended)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/messaging_app.git
   cd messaging_app
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```



## API Endpoints

- `/api/messages/` - List and create messages
- `/api/conversations/` - List and create conversations
- `/api/users/` - List users

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License.

## Contact

For questions or suggestions, open an issue or contact the maintainer.
