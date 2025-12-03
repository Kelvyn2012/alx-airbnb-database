# Python Version Compatibility Guide

## Issue: psycopg2-binary Installation Error on Python 3.14

If you're seeing this error when running `pip install -r requirements.txt`:

```
error: subprocess-exited-with-error
× Building wheel for psycopg2-binary (pyproject.toml) did not run successfully.
error: call to undeclared function '_PyInterpreterState_Get'
```

This means you're trying to install psycopg2-binary on **Python 3.14**, which is **not yet supported**.

---

## Recommended Solution: Use Python 3.12

This project is tested and works perfectly with **Python 3.12**.

### Check Your Python Version

```bash
python --version
# or
python3 --version
```

If you see `Python 3.14.x`, you need to switch to Python 3.12.

---

## Installing Python 3.12

### macOS (using Homebrew)

```bash
# Install Python 3.12
brew install python@3.12

# Create virtual environment with Python 3.12
python3.12 -m venv venv

# Activate
source venv/bin/activate

# Verify version
python --version  # Should show Python 3.12.x

# Install dependencies
pip install -r requirements.txt
```

### macOS (using pyenv)

```bash
# Install pyenv if not already installed
brew install pyenv

# Install Python 3.12
pyenv install 3.12.7

# Set as local version for this project
cd /path/to/alx-airbnb-database/backend
pyenv local 3.12.7

# Create virtual environment
python -m venv venv

# Activate and install
source venv/bin/activate
pip install -r requirements.txt
```

### Ubuntu/Debian

```bash
# Add deadsnakes PPA for Python 3.12
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

# Install Python 3.12
sudo apt install python3.12 python3.12-venv python3.12-dev

# Create virtual environment
python3.12 -m venv venv

# Activate and install
source venv/bin/activate
pip install -r requirements.txt
```

### Windows

1. Download Python 3.12 from [python.org](https://www.python.org/downloads/)
2. Run the installer (check "Add Python to PATH")
3. Open Command Prompt:

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## Supported Python Versions

| Python Version | Status | Notes |
|----------------|--------|-------|
| 3.10.x | ✓ Supported | Tested and working |
| 3.11.x | ✓ Supported | Tested and working |
| **3.12.x** | **✓ Recommended** | **Best compatibility** |
| 3.13.x | ⚠️ Partial | Some dependencies may have issues |
| 3.14.x | ✗ Not Supported | psycopg2-binary doesn't compile |

---

## Alternative: Using psycopg3 (Advanced)

If you **must** use Python 3.14, you can try switching to psycopg3:

### 1. Update requirements.txt

Replace:
```
psycopg2-binary==2.9.9
```

With:
```
psycopg[binary]==3.2.1
```

### 2. Update Django Settings

In `settings.py`, ensure you're using the standard PostgreSQL backend:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # ... rest of config
    }
}
```

### 3. Test Thoroughly

Psycopg3 has some API differences from psycopg2. Test all database operations.

**Note:** This is an experimental approach. We recommend using Python 3.12.

---

## Current Project Setup

Your project is currently configured for **Python 3.12**:

```
✓ Virtual environment: /backend/venv (Python 3.12)
✓ Server running: Python 3.12
✓ All dependencies installed: Python 3.12
```

If you're getting the error, it's because you're trying to install packages with a different Python version than what your venv uses.

---

## Verifying Your Setup

After switching to Python 3.12:

```bash
# Check Python version in venv
source venv/bin/activate
python --version

# Should output: Python 3.12.x

# Install dependencies
pip install -r requirements.txt

# Verify psycopg2 installation
python -c "import psycopg2; print(psycopg2.__version__)"

# Should output: 2.9.9 (dt dec pq3 ext lo64)

# Run the server
python manage.py runserver
```

---

## Why Python 3.12?

1. **Stability**: Mature and stable release
2. **Compatibility**: All dependencies fully support it
3. **Performance**: Excellent performance improvements over 3.10/3.11
4. **Long-term support**: Will be supported until 2028
5. **Production-ready**: Used in production by many Django projects

---

## Troubleshooting

### Error: "No module named '_ctypes'"

Install required system libraries:

**macOS:**
```bash
brew install libffi
```

**Ubuntu/Debian:**
```bash
sudo apt install libffi-dev
```

### Error: "pg_config not found"

Install PostgreSQL development headers:

**macOS:**
```bash
brew install postgresql@14
```

**Ubuntu/Debian:**
```bash
sudo apt install libpq-dev
```

### Multiple Python Versions Conflict

Use virtual environments to isolate Python versions:

```bash
# Remove old venv
rm -rf venv

# Create new venv with specific Python
python3.12 -m venv venv

# Always activate before working
source venv/bin/activate
```

---

## Summary

**Quick Fix:**
1. Install Python 3.12
2. Create new venv: `python3.12 -m venv venv`
3. Activate: `source venv/bin/activate`
4. Install: `pip install -r requirements.txt`
5. Run server: `python manage.py runserver`

**Status:** This resolves the psycopg2-binary installation error completely.

---

## Additional Resources

- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [Python Version Support Timeline](https://devguide.python.org/versions/)
- [psycopg2 Documentation](https://www.psycopg.org/docs/)
- [psycopg3 Migration Guide](https://www.psycopg.org/psycopg3/docs/basic/from_pg2.html)

---

**Last Updated:** December 3, 2025
**Recommended Python:** 3.12.7
**Status:** ✓ Working Configuration
