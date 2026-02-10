# JineArt IVF Website

Professional Django-based website for JineArt IVF Clinic - fertility and reproductive health services.

## 🌟 Features

- **Multilingual Support**: Turkish, English, and German (using django-parler)
- **Modern Admin Panel**: Django Jet admin interface
- **Rich Content Editor**: CKEditor integration for content management
- **Dynamic Preferences**: Easy site configuration management
- **Responsive Design**: Mobile-friendly interface
- **SEO Optimized**: Sitemaps and meta tag support
- **Contact Forms**: reCAPTCHA protected contact functionality

## 🛠️ Tech Stack

- **Framework**: Django 3.2
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **Web Server**: Gunicorn
- **Static Files**: WhiteNoise
- **Admin**: Django Jet

## 📦 Installation

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/jineart-ivf-website.git
cd jineart-ivf-website
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file (copy from `.env-example`):
```bash
cp .env-example .env
```

5. Generate a SECRET_KEY and add to `.env`:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

6. Run migrations:
```bash
python manage.py migrate
```

7. Create superuser:
```bash
python manage.py createsuperuser
```

8. Collect static files:
```bash
python manage.py collectstatic
```

9. Run development server:
```bash
python manage.py runserver
```

Visit http://localhost:8000

## 🚀 Deployment

### Railway Deployment

This project is configured for easy deployment on Railway.

1. Push to GitHub
2. Connect Railway to your GitHub repository
3. Add environment variables in Railway dashboard
4. Deploy automatically

### Required Environment Variables

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,.railway.app
DB_URL=postgresql://user:password@host:port/dbname
DJANGO_SETTINGS_MODULE=config.settings.pro

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_PORT=587
CONTACT_FORM_RECEIVER=contact@yourdomain.com

# Optional
ADMIN_URL=admin/
LANGUAGE_CODE=tr
TIME_ZONE=Europe/Istanbul
SECURE_SSL_REDIRECT=True
APPLY_EXTRA_SECURITY_SETTINGS=True
```

## 📁 Project Structure

```
jineart_ivf/
├── config/              # Project configuration
│   ├── settings/        # Split settings (base, dev, pro)
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── page/                # Main application
│   ├── models/          # Database models
│   ├── admin/           # Admin configurations
│   ├── views.py         # View functions
│   └── urls.py          # App URL patterns
├── templates/           # HTML templates
├── static/              # Static files (CSS, JS, images)
├── locale/              # Translation files
└── manage.py            # Django management script
```

## 🌐 Languages

- Turkish (default)
- English
- German

## 📝 License

Proprietary - All rights reserved

## 👨‍⚕️ About

JineArt IVF Clinic provides comprehensive fertility and reproductive health services.

---

**Version**: 1.0.0  
**Django Version**: 3.2  
**Python Version**: 3.9+
