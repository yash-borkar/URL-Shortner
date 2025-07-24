# 🔗 URL Shortener Service

A simple, lightweight URL shortening service built with Flask. Transform long URLs into short, shareable links with built-in analytics tracking.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## ✨ Features

- **🔧 URL Shortening**: Convert long URLs into 6-character alphanumeric codes
- **🔁 Smart Redirects**: Seamless redirection from short codes to original URLs
- **📊 Analytics Dashboard**: Track clicks, creation time, and usage statistics
- **✅ Input Validation**: Robust URL validation and comprehensive error handling
- **🧵 Thread-Safe**: Concurrent request handling with in-memory storage
- **🧪 Well-Tested**: Complete test suite using Pytest

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Language** | Python 3.8+ |
| **Web Framework** | Flask |
| **Testing** | Pytest |
| **Storage** | In-memory (Dictionary) |
| **HTTP Client** | Requests |

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/url-shortener.git
   cd url-shortener
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the application**
   ```bash
   python -m flask --app app.main run
   ```

4. **Access the service**
   
   The application will be available at `http://localhost:5000`

## 📚 API Documentation

### 🔗 Shorten URL

Create a short URL from a long URL.

**Endpoint:** `POST /api/shorten`

**Request Body:**
```json
{
  "url": "https://www.example.com/very/long/url/with/many/parameters"
}
```

**Example Request:**
```bash
curl -X POST http://localhost:5000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.google.com"}'
```

**Response:**
```json
{
  "short_code": "abc123",
  "short_url": "http://localhost:5000/abc123"
}
```

### 🔄 Redirect to Original URL

Redirect from short code to the original URL.

**Endpoint:** `GET /<short_code>`

**Example:**
```bash
curl -L http://localhost:5000/abc123
# Redirects to: https://www.google.com
```

### 📈 Get URL Analytics

Retrieve usage statistics for a shortened URL.

**Endpoint:** `GET /api/stats/<short_code>`

**Example Request:**
```bash
curl http://localhost:5000/api/stats/abc123
```

**Response:**
```json
{
  "url": "https://www.google.com",
  "clicks": 15,
  "created_at": "2025-07-24T10:30:45+00:00"
}
```

## 🧪 Testing

Run the complete test suite:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=app

# Run specific test file
pytest tests/test_main.py
```

### Test Coverage

The test suite covers:
- ✅ URL shortening functionality
- ✅ Redirection logic
- ✅ Analytics tracking
- ✅ Error handling scenarios
- ✅ Input validation
- ✅ Edge cases

## 📁 Project Structure

```
url-shortener/
├── app/
│   ├── __init__.py          # Flask app initialization
│   └── main.py              # Main application logic
├── tests/
│   └── test_main.py         # Test suite
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitignore               # Git ignore rules
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_APP` | Flask application entry point | `app.main` |
| `FLASK_ENV` | Environment mode | `development` |
| `FLASK_DEBUG` | Debug mode | `True` |

### Customization

You can modify the following parameters in `app/main.py`:

- **Short code length**: Change `SHORT_CODE_LENGTH` constant
- **Base URL**: Modify the base URL for generated short links
- **Storage backend**: Replace in-memory storage with database

## ⚠️ Important Notes

- **Data Persistence**: This service uses in-memory storage. All data is lost when the application restarts.
- **Production Ready**: This is a demonstration/learning project. For production use, consider:
  - Database integration (PostgreSQL, MongoDB)
  - Redis caching layer
  - Rate limiting
  - Authentication/authorization
  - Custom domain support
  - SSL/HTTPS configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/) web framework
- Inspired by services like [Bitly](https://bitly.com/) and [TinyURL](https://tinyurl.com/)
- Testing powered by [Pytest](https://pytest.org/)
