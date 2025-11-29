# Setup Checklist

Use this checklist to ensure everything is properly configured.

## ✅ Prerequisites

- [ ] Python 3.8+ installed (`python --version`)
- [ ] Node.js 14+ installed (`node --version`)
- [ ] PostgreSQL installed and running
- [ ] Redis installed (optional, for messaging)
- [ ] Git installed

## ✅ Backend Setup

### Environment Setup
- [ ] Created virtual environment (`python -m venv venv`)
- [ ] Activated virtual environment
- [ ] Installed dependencies (`pip install -r requirements.txt`)
- [ ] Copied `.env.example` to `.env`
- [ ] Updated `.env` with correct database credentials
- [ ] Updated `.env` with SECRET_KEY

### Database Setup
- [ ] Created PostgreSQL database (`createdb airbnb_db`)
- [ ] Database connection successful
- [ ] Ran migrations (`python manage.py migrate`)
- [ ] Created superuser (`python manage.py createsuperuser`)
- [ ] (Optional) Loaded sample data

### Testing Backend
- [ ] Started Django server (`python manage.py runserver`)
- [ ] Backend accessible at http://localhost:8000
- [ ] Admin panel accessible at http://localhost:8000/admin/
- [ ] API docs accessible at http://localhost:8000/swagger/
- [ ] Can login to admin panel

## ✅ Frontend Setup

### Environment Setup
- [ ] Installed Node dependencies (`npm install`)
- [ ] Created `.env` file with API URL
- [ ] No installation errors

### Testing Frontend
- [ ] Started React server (`npm start`)
- [ ] Frontend accessible at http://localhost:3000
- [ ] No console errors
- [ ] Page loads correctly

## ✅ Integration Testing

### Authentication
- [ ] Can register new user
- [ ] Can login with credentials
- [ ] Can access profile page
- [ ] Can update profile
- [ ] Can logout

### Properties (Guest View)
- [ ] Can view property list on home page
- [ ] Can search properties
- [ ] Can filter properties
- [ ] Can view property details
- [ ] Can see property images (if uploaded)
- [ ] Can see property reviews

### Bookings
- [ ] Can create a booking
- [ ] Booking validation works (dates, availability)
- [ ] Can view booking list
- [ ] Can process payment
- [ ] Can cancel booking
- [ ] Booking status updates correctly

### Reviews
- [ ] Can submit a review
- [ ] Review appears on property page
- [ ] Rating displays correctly
- [ ] Cannot submit duplicate review

### Host Features
- [ ] Can access host dashboard (if host role)
- [ ] Can create new property
- [ ] Can upload property images
- [ ] Can view host bookings
- [ ] Can confirm/cancel bookings
- [ ] Dashboard stats display correctly

### Messages
- [ ] Can send message
- [ ] Can view conversation
- [ ] Messages display correctly
- [ ] (If Redis running) Real-time updates work

## ✅ Admin Panel

- [ ] Can access admin panel
- [ ] Can view all users
- [ ] Can view all properties
- [ ] Can view all bookings
- [ ] Can view all payments
- [ ] Can view all reviews
- [ ] Can view all messages

## ✅ API Testing

Using http://localhost:8000/swagger/ or Postman:

- [ ] POST /api/users/register/ - Creates user
- [ ] POST /api/users/login/ - Returns JWT tokens
- [ ] GET /api/properties/ - Returns property list
- [ ] POST /api/properties/create/ - Creates property (with auth)
- [ ] POST /api/bookings/create/ - Creates booking (with auth)
- [ ] POST /api/reviews/create/ - Creates review (with auth)

## ✅ Error Handling

- [ ] Invalid login shows error message
- [ ] Invalid booking dates show error
- [ ] Unauthorized access redirects to login
- [ ] 404 pages display correctly
- [ ] Form validation works

## ✅ Responsive Design

- [ ] Desktop view works correctly
- [ ] Tablet view is responsive
- [ ] Mobile view is responsive
- [ ] Navigation works on all screen sizes

## ✅ Optional Features

### Redis/WebSockets
- [ ] Redis server running
- [ ] WebSocket connection successful
- [ ] Real-time messaging works

### Production Preparation
- [ ] All sensitive data in `.env`
- [ ] `.gitignore` configured correctly
- [ ] No passwords in code
- [ ] DEBUG=False works (for production)

## 🐛 Common Issues & Solutions

### Backend won't start
```bash
# Check if port is in use
lsof -i :8000
# Use different port
python manage.py runserver 8001
```

### Frontend won't start
```bash
# Clear cache
rm -rf node_modules package-lock.json
npm install
npm start
```

### Database connection error
```bash
# Check PostgreSQL is running
pg_isready
# Verify credentials in .env
# Check database exists
psql -l
```

### Migration errors
```bash
# Reset migrations (development only!)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
python manage.py makemigrations
python manage.py migrate
```

### CORS errors
- Verify frontend URL in backend `settings.py` CORS_ALLOWED_ORIGINS
- Check backend URL in frontend `.env`

## 📋 Deployment Checklist (When Ready)

- [ ] Set DEBUG=False in production
- [ ] Configure allowed hosts
- [ ] Set up production database
- [ ] Configure static files
- [ ] Set up media file storage
- [ ] Configure email backend
- [ ] Set secure SECRET_KEY
- [ ] Enable HTTPS
- [ ] Set up monitoring
- [ ] Configure backups

## 🎉 Success Criteria

Your setup is complete when:

✅ Backend API is accessible and responding
✅ Frontend loads without errors
✅ Can register and login users
✅ Can create and view properties
✅ Can make bookings
✅ Can submit reviews
✅ Admin panel is accessible
✅ All features work as expected

---

**Need Help?**
- Check README.md for detailed instructions
- Review QUICKSTART.md for basic setup
- Check API documentation at /swagger/
- Review error logs in terminal

**Ready to go?** Start building amazing features! 🚀
