
import socket
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = 'resume_screening_2026_super_secret_key_12345'

# ========== FOLDERS SETUP ==========
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ========== JSON DATABASES ==========
APPLICANTS_FILE = 'applicants.json'
COMPANIES_FILE = 'companies.json'
ADMIN_FILE = 'admin.json'

# Create admin credentials
if not os.path.exists(ADMIN_FILE):