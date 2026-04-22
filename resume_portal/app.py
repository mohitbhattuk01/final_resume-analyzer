# # from flask import Flask, render_template, request, jsonify, session, redirect, url_for, make_response, send_from_directory
# # import os
# # import json
# # from datetime import datetime
# # import PyPDF2
# # import re
# # import csv
# # from io import StringIO
# # import socket
# # import smtplib
# # from email.mime.text import MIMEText
# # from email.mime.multipart import MIMEMultipart

# # app = Flask(__name__)
# # app.static_folder = 'static'
# # app.secret_key = 'resume_screening_2026_super_secret_key_12345'

# # # ========== FOLDERS SETUP ==========
# # UPLOAD_FOLDER = 'static/uploads'
# # os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # # ========== JSON DATABASES ==========
# # APPLICANTS_FILE = 'applicants.json'
# # COMPANIES_FILE = 'companies.json'
# # ADMIN_FILE = 'admin.json'

# # # Create admin credentials
# # if not os.path.exists(ADMIN_FILE):
# #     with open(ADMIN_FILE, 'w') as f:
# #         json.dump({
# #             "username": "admin",
# #             "password": "admin123",
# #             "email": "admin@resumeai.com"
# #         }, f)
# #     print("✅ Created admin.json")

# # if not os.path.exists(COMPANIES_FILE):
# #     with open(COMPANIES_FILE, 'w') as f:
# #         json.dump([], f)

# # if not os.path.exists(APPLICANTS_FILE):
# #     with open(APPLICANTS_FILE, 'w') as f:
# #         json.dump([], f)
# #     print("✅ Created applicants.json")

# # # ========== COMPANY DATABASE ==========
# # COMPANY_DATA = [
# #     {"id": 1, "name": "Google", "skills": ["Python", "C++", "Java", "TensorFlow", "PyTorch", "Kubernetes", "System Design", "DSA"], "salary": "₹30-80 LPA"},
# #     {"id": 2, "name": "Microsoft", "skills": ["C#", "Python", "Azure", "SQL", "Power BI", ".NET Core", "System Design", "DSA"], "salary": "₹30-80 LPA"},
# #     {"id": 3, "name": "Amazon", "skills": ["Java", "C++", "Python", "AWS", "Distributed Systems", "DSA", "System Design"], "salary": "₹30-70 LPA"},
# #     {"id": 4, "name": "TCS", "skills": ["Java", "Python", "SQL", "Spring Boot", "AWS", "DSA", "DBMS"], "salary": "₹4-9 LPA"},
# #     {"id": 5, "name": "Infosys", "skills": ["Python", "Java", "Spring", "AWS", "Azure", "SQL", "DSA"], "salary": "₹6.25-21 LPA"},
# #     {"id": 6, "name": "Thoughtworks", "skills": ["C#", "Java", "Python", "TDD", "CI/CD", "Docker", "Microservices"], "salary": "₹12-25 LPA"},
# #     {"id": 7, "name": "Meta", "skills": ["Python", "C++", "React", "PyTorch", "System Design", "DSA"], "salary": "₹35-85 LPA"},
# #     {"id": 8, "name": "Apple", "skills": ["Swift", "C++", "Python", "iOS", "macOS", "System Design", "DSA"], "salary": "₹35-75 LPA"},
# #     {"id": 9, "name": "Salesforce", "skills": ["Apex", "Java", "JavaScript", "SQL", "Cloud Computing", "Lightning", "DSA"], "salary": "₹20-45 LPA"},
# #     {"id": 10, "name": "Adobe", "skills": ["JavaScript", "C++", "Python", "React", "Node.js", "Cloud", "DSA"], "salary": "₹25-50 LPA"}
# # ]

# # # ========== EMAIL FUNCTION ==========
# # SENDER_EMAIL = "mohitnjatt1122@gmail.com"
# # SENDER_PASSWORD = "nvkn lbrt hxqx umqx"

# # def send_status_email(applicant, status):
# #     try:
# #         if status == "Shortlisted":
# #             subject = f"🎉 Congratulations! Shortlisted for {applicant['company']} 2026"
# #             body = f"""
# # Dear {applicant['name']},

# # CONGRATULATIONS! You have been SHORTLISTED for {applicant['company']}.

# # 📊 YOUR SCORE BREAKDOWN:
# # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# # 🏢 Company: {applicant['company']}
# # 🎯 Final Score: {applicant['score']}%
# # 📈 Skill Score: {applicant.get('skill_score', 0)}%
# # 💼 Experience: {applicant.get('exp_years', 0)} years ({applicant.get('exp_score', 0)}%)
# # 📁 Projects: {applicant.get('projects_count', 0)} ({applicant.get('projects_score', 0)}%)
# # 🎓 Certifications: {applicant.get('cert_count', 0)} ({applicant.get('cert_score', 0)}%)

# # ✅ Skills Matched: {', '.join(applicant['matched_skills'][:5])}

# # 📌 NEXT STEPS:
# # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# # • Interview details will be sent within 48 hours

# # Best regards,
# # {applicant['company']} Recruitment Team
# # """
# #         elif status == "Rejected":
# #             subject = f"Update regarding {applicant['company']} Application"
# #             body = f"""
# # Dear {applicant['name']},

# # Thank you for applying to {applicant['company']}.

# # 📊 YOUR SCORE: {applicant['score']}%
# # ❌ Status: Not Selected this time

# # We encourage you to apply again in future.

# # Best regards,
# # {applicant['company']} Recruitment Team
# # """
# #         else:
# #             return False
        
# #         msg = MIMEMultipart()
# #         msg['From'] = SENDER_EMAIL
# #         msg['To'] = applicant['email']
# #         msg['Subject'] = subject
# #         msg.attach(MIMEText(body, 'plain'))
        
# #         server = smtplib.SMTP('smtp.gmail.com', 587)
# #         server.starttls()
# #         server.login(SENDER_EMAIL, SENDER_PASSWORD)
# #         server.send_message(msg)
# #         server.quit()
# #         print(f"✅ Email sent to {applicant['email']}")
# #         return True
# #     except Exception as e:
# #         print(f"❌ Email Error: {e}")
# #         return False

# # # ========== VIEW RESUME ==========
# # @app.route('/view_resume/<filename>')
# # def view_resume(filename):
# #     return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

# # # ========== RESUME EXTRACTORS ==========
# # def extract_text_from_pdf(pdf_path):
# #     text = ""
# #     try:
# #         with open(pdf_path, 'rb') as file:
# #             reader = PyPDF2.PdfReader(file)
# #             for page in reader.pages:
# #                 text += page.extract_text() + " "
# #         return text.lower()
# #     except:
# #         return ""

# # def extract_skills_from_text(text):
# #     skills_list = ['python', 'java', 'c++', 'sql', 'aws', 'docker', 'kubernetes', 'tensorflow', 'pytorch', 'react', 'node', 'django', 'flask', 'spring', 'javascript', 'html', 'css', 'git', 'linux', 'mongodb', 'postgresql', 'azure', 'gcp', 'devops', 'cicd', 'jenkins']
# #     found = []
# #     for skill in skills_list:
# #         if skill in text:
# #             found.append(skill)
# #     return list(set(found))

# # def extract_experience_years(text):
# #     patterns = [
# #         r'(\d+)\+?\s*years?',
# #         r'(\d+)\+?\s*yrs?',
# #         r'experience\s*of\s*(\d+)\s*years?',
# #         r'(\d+)\+?\s*years?\s*of\s*experience'
# #     ]
# #     for pattern in patterns:
# #         match = re.search(pattern, text, re.IGNORECASE)
# #         if match:
# #             return int(match.group(1))
# #     return 0

# # def extract_projects_count(text):
# #     project_keywords = ['project', 'projects', 'project:', '• project', '- project', 'developed', 'built', 'created']
# #     count = 0
# #     text_lower = text.lower()
# #     for keyword in project_keywords:
# #         count += text_lower.count(keyword)
# #     return min(count, 5)

# # def extract_certifications_count(text):
# #     cert_keywords = ['certification', 'certified', 'certificate', 'coursera', 'udemy', 'aws certified', 'google certified', 'microsoft certified', 'scrum', 'agile']
# #     count = 0
# #     text_lower = text.lower()
# #     for keyword in cert_keywords:
# #         count += text_lower.count(keyword)
# #     return min(count, 5)

# # # ========== SCORE CALCULATOR ==========
# # def calculate_match_score(resume_skills, company_name, resume_text):
# #     company = next((c for c in COMPANY_DATA if c['name'].lower() == company_name.lower()), None)
# #     if not company:
# #         return 0, [], [], {}
    
# #     required_skills = [s.lower() for s in company['skills']]
# #     resume_skills_lower = [s.lower() for s in resume_skills]
    
# #     # 1. SKILL SCORE (50%)
# #     matched_skills = []
# #     for skill in required_skills:
# #         if any(skill in rs or rs in skill for rs in resume_skills_lower):
# #             matched_skills.append(skill)
# #     skill_score = (len(matched_skills) / len(required_skills)) * 100 if required_skills else 0
    
# #     # 2. EXPERIENCE SCORE (25%)
# #     exp_years = extract_experience_years(resume_text)
# #     required_exp = 2
# #     exp_score = min((exp_years / required_exp) * 100, 100) if exp_years > 0 else 0
    
# #     # 3. PROJECTS SCORE (15%)
# #     projects_count = extract_projects_count(resume_text)
# #     projects_score = min((projects_count / 3) * 100, 100)
    
# #     # 4. CERTIFICATIONS SCORE (10%)
# #     cert_count = extract_certifications_count(resume_text)
# #     cert_score = min((cert_count / 3) * 100, 100)
    
# #     # FINAL SCORE
# #     final_score = (skill_score * 0.5) + (exp_score * 0.25) + (projects_score * 0.15) + (cert_score * 0.10)
    
# #     missing_skills = [s for s in required_skills if s not in matched_skills][:5]
    
# #     scores_detail = {
# #         'skill_score': round(skill_score, 2),
# #         'exp_score': round(exp_score, 2),
# #         'projects_score': round(projects_score, 2),
# #         'cert_score': round(cert_score, 2),
# #         'exp_years': exp_years,
# #         'projects_count': projects_count,
# #         'cert_count': cert_count
# #     }
    
# #     return round(final_score, 2), matched_skills[:8], missing_skills, scores_detail

# # # ========== ROUTES ==========
# # @app.route('/')
# # def home():
# #     return render_template('index.html')

# # @app.route('/apply')
# # def apply():
# #     company = request.args.get('company', '')
# #     return render_template('apply.html', company=company)

# # @app.route('/admin')
# # def admin():
# #     if session.get('admin_logged_in'):
# #         return redirect(url_for('admin_dashboard'))
# #     return render_template('admin_login.html')

# # @app.route('/admin/login', methods=['POST'])
# # def admin_login():
# #     data = request.json
# #     with open(ADMIN_FILE, 'r') as f:
# #         admin = json.load(f)
# #     if data.get('username') == admin['username'] and data.get('password') == admin['password']:
# #         session['admin_logged_in'] = True
# #         return jsonify({'success': True})
# #     return jsonify({'success': False})

# # @app.route('/admin/logout')
# # def admin_logout():
# #     session.pop('admin_logged_in', None)
# #     return redirect(url_for('admin'))

# # @app.route('/admin/dashboard')
# # def admin_dashboard():
# #     if not session.get('admin_logged_in'):
# #         return redirect(url_for('admin'))
# #     return render_template('admin_dashboard.html', companies=COMPANY_DATA)

# # # ========== API ENDPOINTS ==========
# # @app.route('/api/admin/applicants')
# # def api_admin_applicants():
# #     with open(APPLICANTS_FILE, 'r') as f:
# #         applicants = json.load(f)
# #     return jsonify(applicants)

# # @app.route('/api/admin/stats')
# # def api_admin_stats():
# #     with open(APPLICANTS_FILE, 'r') as f:
# #         applicants = json.load(f)
    
# #     # Company wise stats calculation
# #     company_wise = {}
# #     for company in COMPANY_DATA:
# #         company_name = company['name']
# #         company_apps = [a for a in applicants if a['company'] == company_name]
# #         if company_apps:
# #             avg_score = sum(a['score'] for a in company_apps) / len(company_apps)
# #             top_score = max(a['score'] for a in company_apps)
# #         else:
# #             avg_score = 0
# #             top_score = 0
            
# #         company_wise[company_name] = {
# #             'total': len(company_apps),
# #             'avg_score': round(avg_score, 2),
# #             'top_score': top_score
# #         }
    
# #     stats = {
# #         'total_applications': len(applicants),
# #         'total_companies': len(COMPANY_DATA),
# #         'pending_review': len([a for a in applicants if a.get('status') == 'Pending']),
# #         'avg_score': round(sum([a['score'] for a in applicants]) / len(applicants), 2) if applicants else 0,
# #         'company_wise': company_wise
# #     }
# #     return jsonify(stats)

# # @app.route('/api/admin/update_status', methods=['POST'])
# # def api_update_status():
# #     data = request.json
# #     with open(APPLICANTS_FILE, 'r') as f:
# #         applicants = json.load(f)
# #     for app in applicants:
# #         if app['id'] == data.get('id'):
# #             app['status'] = data.get('status')
# #             send_status_email(app, data.get('status'))
# #             break
# #     with open(APPLICANTS_FILE, 'w') as f:
# #         json.dump(applicants, f, indent=2)
# #     return jsonify({'success': True})

# # @app.route('/api/admin/delete_applicant', methods=['POST'])
# # def delete_applicant():
# #     data = request.json
# #     with open(APPLICANTS_FILE, 'r') as f:
# #         applicants = json.load(f)
# #     new_applicants = [app for app in applicants if app['id'] != data.get('id')]
# #     with open(APPLICANTS_FILE, 'w') as f:
# #         json.dump(new_applicants, f, indent=2)
# #     return jsonify({'success': True})

# # @app.route('/api/admin/top10/<company>')
# # def api_top10(company):
# #     with open(APPLICANTS_FILE, 'r') as f:
# #         applicants = json.load(f)
# #     company_apps = [a for a in applicants if a['company'] == company]
# #     company_apps.sort(key=lambda x: x['score'], reverse=True)
# #     return jsonify(company_apps[:10])

# # @app.route('/api/admin/export_csv/<company>')
# # def export_csv(company):
# #     with open(APPLICANTS_FILE, 'r') as f:
# #         applicants = json.load(f)
# #     company_apps = [a for a in applicants if a['company'] == company]
# #     company_apps.sort(key=lambda x: x['score'], reverse=True)
    
# #     si = StringIO()
# #     cw = csv.writer(si)
# #     cw.writerow(['Rank', 'Name', 'Email', 'Qualification', 'Score', 'Skill%', 'Exp%', 'Projects%', 'Cert%', 'Matched Skills', 'Status', 'Applied Date'])
    
# #     for idx, app in enumerate(company_apps[:10], 1):
# #         cw.writerow([
# #             idx, app['name'], app['email'], app.get('qualification', 'N/A'),
# #             f"{app['score']}%",
# #             f"{app.get('skill_score', 0)}%",
# #             f"{app.get('exp_score', 0)}%",
# #             f"{app.get('projects_score', 0)}%",
# #             f"{app.get('cert_score', 0)}%",
# #             ', '.join(app.get('matched_skills', [])[:5]),
# #             app.get('status', 'Pending'),
# #             app.get('applied_date', 'N/A')
# #         ])
    
# #     output = make_response(si.getvalue())
# #     output.headers["Content-Disposition"] = f"attachment; filename={company}_Top10_{datetime.now().strftime('%Y%m%d')}.csv"
# #     output.headers["Content-type"] = "text/csv"
# #     return output

# # @app.route('/api/companies')
# # def api_companies():
# #     return jsonify(COMPANY_DATA)

# # # ========== SUBMIT APPLICATION ==========
# # @app.route('/submit_application', methods=['POST'])
# # def submit_application():
# #     try:
# #         name = request.form.get('name')
# #         email = request.form.get('email')
# #         qualification = request.form.get('qualification')
# #         company = request.form.get('company')
# #         resume_file = request.files.get('resume')
        
# #         print("\n" + "="*60)
# #         print("📥 NEW APPLICATION RECEIVED")
# #         print("="*60)
# #         print(f"👤 Name: {name}")
# #         print(f"📧 Email: {email}")
# #         print(f"🎓 Qualification: {qualification}")
# #         print(f"🏢 Company: {company}")
# #         print(f"📄 Resume: {resume_file.filename}")
        
# #         timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
# #         filename = f"{timestamp}_{resume_file.filename}"
# #         filepath = os.path.join(UPLOAD_FOLDER, filename)
# #         resume_file.save(filepath)
# #         print(f"✅ Resume saved: {filename}")
        
# #         resume_text = extract_text_from_pdf(filepath)
# #         resume_skills = extract_skills_from_text(resume_text)
# #         print(f"🔍 Skills found: {len(resume_skills)}")
        
# #         score, matched_skills, missing_skills, scores_detail = calculate_match_score(resume_skills, company, resume_text)
        
# #         print(f"📊 Skill Score: {scores_detail['skill_score']}%")
# #         print(f"📊 Experience Score: {scores_detail['exp_score']}% ({scores_detail['exp_years']} years)")
# #         print(f"📊 Projects Score: {scores_detail['projects_score']}% ({scores_detail['projects_count']} projects)")
# #         print(f"📊 Certifications Score: {scores_detail['cert_score']}% ({scores_detail['cert_count']} certs)")
# #         print(f"🎯 FINAL SCORE: {score}%")
        
# #         applicant = {
# #             'id': timestamp,
# #             'name': name,
# #             'email': email,
# #             'qualification': qualification,
# #             'company': company,
# #             'resume': filename,
# #             'skills_found': resume_skills[:15],
# #             'matched_skills': matched_skills,
# #             'missing_skills': missing_skills,
# #             'score': score,
# #             'skill_score': scores_detail['skill_score'],
# #             'exp_score': scores_detail['exp_score'],
# #             'projects_score': scores_detail['projects_score'],
# #             'cert_score': scores_detail['cert_score'],
# #             'exp_years': scores_detail['exp_years'],
# #             'projects_count': scores_detail['projects_count'],
# #             'cert_count': scores_detail['cert_count'],
# #             'status': 'Pending',
# #             'applied_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# #         }
        
# #         with open(APPLICANTS_FILE, 'r') as f:
# #             applicants = json.load(f)
        
# #         applicants.append(applicant)
        
# #         with open(APPLICANTS_FILE, 'w') as f:
# #             json.dump(applicants, f, indent=2)
        
# #         print(f"💾 Data saved")
# #         print("="*60 + "\n")
        
# #         return jsonify({
# #             'success': True,
# #             'message': f'✅ Application submitted successfully for {company}!',
# #             'score': score,
# #             'skill_score': scores_detail['skill_score'],
# #             'exp_score': scores_detail['exp_score'],
# #             'projects_score': scores_detail['projects_score'],
# #             'cert_score': scores_detail['cert_score'],
# #             'matched_skills': matched_skills,
# #             'missing_skills': missing_skills
# #         })
        
# #     except Exception as e:
# #         print(f"❌ ERROR: {str(e)}")
# #         return jsonify({
# #             'success': False,
# #             'message': f'Error: {str(e)}'
# #         }), 500

# # if __name__ == '__main__':
# #     print("\n" + "="*80)
# #     print("🚀 AI RESUME SCREENING SYSTEM 2026 - READY!")
# #     print("="*80)
# #     print("🏢 Companies: 10 Top Tech Companies Loaded")
# #     print("📍 Home Page: http://localhost:5000")
# #     print("📍 Apply Page: http://localhost:5000/apply")
# #     print("📍 Admin Login: http://localhost:5000/admin")
# #     print("\n🔐 Admin Credentials:")
# #     print("   Username: admin")
# #     print("   Password: admin123")
# #     print("\n✅ FEATURES:")
# #     print("   • Skills Matching (50%)")
# #     print("   • Experience Years (25%)")
# #     print("   • Projects Count (15%)")
# #     print("   • Certifications (10%)")
# #     print("   • Email Notification")
# #     print("   • CSV Export")
# #     print("   • View Resume PDF")
# #     print("="*80)
# #     print("📁 JSON Database Files:")
# #     print(f"   • {APPLICANTS_FILE}")
# #     print(f"   • {COMPANIES_FILE}")
# #     print(f"   • {ADMIN_FILE}")
# #     print("="*80 + "\n")
    
# #     hostname = socket.gethostname()
# #     ip_address = socket.gethostbyname(hostname)
    
# #     print("\n" + "="*60)
# #     print("📱 SHARE THIS LINK WITH FRIENDS:")
# #     print(f"🔗 http://{ip_address}:5000")
# #     print("="*60)
    
# #     app.run(debug=True, host='0.0.0.0', port=5000)












































from flask import Flask, render_template, request, jsonify, session, redirect, url_for, make_response, send_from_directory
import os
import json
from datetime import datetime
import PyPDF2
import re
import csv
from io import StringIO
import socket
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = 'resume_screening_2026_super_secret_key_12345'

# ========== FOLDERS SETUP ==========
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ========== JSON DATABASES ==========
# All data files stored relative to app.py (works on both local & Render)
APPLICANTS_FILE = os.path.join(BASE_DIR, 'applicants.json')
COMPANIES_FILE = os.path.join(BASE_DIR, 'companies.json')
ADMIN_FILE = os.path.join(BASE_DIR, 'admin.json')

# Create admin credentials
if not os.path.exists(ADMIN_FILE):
    with open(ADMIN_FILE, 'w') as f:
        json.dump({
            "username": "admin",
            "password": "admin123",
            "email": "admin@resumeai.com"
        }, f)
    print("✅ Created admin.json")

if not os.path.exists(COMPANIES_FILE):
    with open(COMPANIES_FILE, 'w') as f:
        json.dump([], f)

if not os.path.exists(APPLICANTS_FILE):
    with open(APPLICANTS_FILE, 'w') as f:
        json.dump([], f)
    print("✅ Created applicants.json")

# ========== COMPANY DATABASE ==========
COMPANY_DATA = [
    {"id": 1, "name": "Google", "skills": ["Python", "C++", "Java", "TensorFlow", "PyTorch", "Kubernetes", "System Design", "DSA"], "salary": "₹30-80 LPA"},
    {"id": 2, "name": "Microsoft", "skills": ["C#", "Python", "Azure", "SQL", "Power BI", ".NET Core", "System Design", "DSA"], "salary": "₹30-80 LPA"},
    {"id": 3, "name": "Amazon", "skills": ["Java", "C++", "Python", "AWS", "Distributed Systems", "DSA", "System Design"], "salary": "₹30-70 LPA"},
    {"id": 4, "name": "TCS", "skills": ["Java", "Python", "SQL", "Spring Boot", "AWS", "DSA", "DBMS"], "salary": "₹4-9 LPA"},
    {"id": 5, "name": "Infosys", "skills": ["Python", "Java", "Spring", "AWS", "Azure", "SQL", "DSA"], "salary": "₹6.25-21 LPA"},
    {"id": 6, "name": "Thoughtworks", "skills": ["C#", "Java", "Python", "TDD", "CI/CD", "Docker", "Microservices"], "salary": "₹12-25 LPA"},
    {"id": 7, "name": "Meta", "skills": ["Python", "C++", "React", "PyTorch", "System Design", "DSA"], "salary": "₹35-85 LPA"},
    {"id": 8, "name": "Apple", "skills": ["Swift", "C++", "Python", "iOS", "macOS", "System Design", "DSA"], "salary": "₹35-75 LPA"},
    {"id": 9, "name": "Salesforce", "skills": ["Apex", "Java", "JavaScript", "SQL", "Cloud Computing", "Lightning", "DSA"], "salary": "₹20-45 LPA"},
    {"id": 10, "name": "Adobe", "skills": ["JavaScript", "C++", "Python", "React", "Node.js", "Cloud", "DSA"], "salary": "₹25-50 LPA"}
]

# ========== EMAIL FUNCTION ==========
SENDER_EMAIL = "mohitnjatt1122@gmail.com"
SENDER_PASSWORD = "nvkn lbrt hxqx umqx"

def send_status_email(applicant, status):
    try:
        if status == "Shortlisted":
            subject = f" Congratulations! Shortlisted for {applicant['company']} 2026"
            body = f"""
Dear {applicant['name']},

CONGRATULATIONS! You have been SHORTLISTED for {applicant['company']}.

📊 YOUR SCORE BREAKDOWN:
 
🏢 Company: {applicant['company']}
🎯 Final Score: {applicant['score']}%
📈 Skill Score: {applicant.get('skill_score', 0)}%     
💼 Experience: {applicant.get('exp_years', 0)} years ({applicant.get('exp_score', 0)}%)
📁 Projects: {applicant.get('projects_count', 0)} ({applicant.get('projects_score', 0)}%)
🎓 Certifications: {applicant.get('cert_count', 0)} ({applicant.get('cert_score', 0)}%)

✅ Skills Matched: {', '.join(applicant['matched_skills'][:5])}

📌 NEXT STEPS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Interview details will be sent within 48 hours

Best regards,
{applicant['company']} Recruitment Team
"""
        elif status == "Rejected":
            subject = f"Update regarding {applicant['company']} Application"
            body = f"""
Dear {applicant['name']},

Thank you for applying to {applicant['company']}.

📊 YOUR SCORE: {applicant['score']}%
❌ Status: Not Selected this time

We encourage you to apply again in future.

Best regards,
{applicant['company']} Recruitment Team
"""
        else:
            return False
        
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = applicant['email']
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"✅ Email sent to {applicant['email']}")
        return True
    except Exception as e:
        print(f" Email Error: {e}")
        return False

 




# ========== VIEW RESUME ==========
@app.route('/view_resume/<path:filename>')
def view_resume(filename):
    import urllib.parse
    
    # Decode filename (for spaces and special chars)
    filename = urllib.parse.unquote(filename)
    
    print(f"🔍 Looking for: {filename}")
    
    # Try multiple upload folder locations
    search_paths = [
        UPLOAD_FOLDER,
        os.path.join(PROJECT_ROOT, 'static', 'uploads'),
        os.path.join(BASE_DIR, 'static', 'uploads'),
    ]
    
    for folder in search_paths:
        full_path = os.path.join(folder, filename)
        print(f"📁 Checking: {full_path}")
        if os.path.exists(full_path):
            print(f"✅ File found at: {full_path}")
            return send_from_directory(folder, filename, as_attachment=False)
    
    # If not found, list what's in the upload folders for debugging
    for folder in search_paths:
        if os.path.exists(folder):
            print(f"📂 Files in {folder}: {os.listdir(folder)[:5]}")
    
    print(f"❌ File not found: {filename}")
    return f"File not found: {filename}", 404

 

# ========== RESUME EXTRACTORS ==========
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + " "
        return text.lower()
    except:
        return ""

def extract_skills_from_text(text):
    skills_list = ['python', 'java', 'c++', 'sql', 'aws', 'docker', 'kubernetes', 'tensorflow', 'pytorch', 'react', 'node', 'django', 'flask', 'spring', 'javascript', 'html', 'css', 'git', 'linux', 'mongodb', 'postgresql', 'azure', 'gcp', 'devops', 'cicd', 'jenkins']
    found = []
    for skill in skills_list:
        if skill in text:
            found.append(skill)
    return list(set(found))

def extract_experience_years(text):
    patterns = [
        r'(\d+)\+?\s*years?',
        r'(\d+)\+?\s*yrs?',
        r'experience\s*of\s*(\d+)\s*years?',
        r'(\d+)\+?\s*years?\s*of\s*experience'
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return int(match.group(1))
    return 0

def extract_projects_count(text):
    project_keywords = ['project', 'projects', 'project:', '• project', '- project', 'developed', 'built', 'created']
    count = 0
    text_lower = text.lower()
    for keyword in project_keywords:
        count += text_lower.count(keyword)
    return min(count, 5)

def extract_certifications_count(text):
    cert_keywords = ['certification', 'certified', 'certificate', 'coursera', 'udemy', 'aws certified', 'google certified', 'microsoft certified', 'scrum', 'agile']
    count = 0
    text_lower = text.lower()
    for keyword in cert_keywords:
        count += text_lower.count(keyword)
    return min(count, 5)

# ========== SCORE CALCULATOR ==========
def calculate_match_score(resume_skills, company_name, resume_text):
    company = next((c for c in COMPANY_DATA if c['name'].lower() == company_name.lower()), None)
    if not company:
        return 0, [], [], {}
    
    required_skills = [s.lower() for s in company['skills']]
    resume_skills_lower = [s.lower() for s in resume_skills]
    
    # 1. SKILL SCORE (50%)
    matched_skills = []
    for skill in required_skills:
        if any(skill in rs or rs in skill for rs in resume_skills_lower):
            matched_skills.append(skill)
    skill_score = (len(matched_skills) / len(required_skills)) * 100 if required_skills else 0
    
    # 2. EXPERIENCE SCORE (25%)
    exp_years = extract_experience_years(resume_text)
    required_exp = 2
    exp_score = min((exp_years / required_exp) * 100, 100) if exp_years > 0 else 0
    
    # 3. PROJECTS SCORE (15a%)
    projects_count = extract_projects_count(resume_text)
    projects_score = min((projects_count / 3) * 100, 100)
    
    # 4. CERTIFICATIONS SCORE (10%)
    cert_count = extract_certifications_count(resume_text)
    cert_score = min((cert_count / 3) * 100, 100)
    
    # FINAL SCORE
    final_score = (skill_score * 0.5) + (exp_score * 0.25) + (projects_score * 0.15) + (cert_score * 0.10)
    
    missing_skills = [s for s in required_skills if s not in matched_skills][:5]
    
    scores_detail = {
        'skill_score': round(skill_score, 2),
        'exp_score': round(exp_score, 2),
        'projects_score': round(projects_score, 2),
        'cert_score': round(cert_score, 2),
        'exp_years': exp_years,
        'projects_count': projects_count,
        'cert_count': cert_count
    }
    
    return round(final_score, 2), matched_skills[:8], missing_skills, scores_detail

# ========== ROUTES ==========
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/apply')
def apply():
    company = request.args.get('company', '')
    return render_template('apply.html', company=company)

@app.route('/admin')
def admin():
    if session.get('admin_logged_in'):
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html')

@app.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.json
    with open(ADMIN_FILE, 'r') as f:
        admin = json.load(f)
    if data.get('username') == admin['username'] and data.get('password') == admin['password']:
        session['admin_logged_in'] = True
        return jsonify({'success': True, 'message': 'Login successful! Welcome Admin.'})
    return jsonify({'success': False, 'message': 'Invalid username or password. Please try again.'})

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin'))

@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin'))
    return render_template('admin_dashboard.html', companies=COMPANY_DATA)

# ========== API ENDPOINTS ==========
@app.route('/api/admin/applicants')
def api_admin_applicants():
    with open(APPLICANTS_FILE, 'r') as f:
        applicants = json.load(f)
    
    # Apply filters from query params
    company = request.args.get('company', '')
    status = request.args.get('status', '')
    min_score = request.args.get('min_score', 0, type=float)
    
    if company:
        applicants = [a for a in applicants if a.get('company') == company]
    if status:
        applicants = [a for a in applicants if a.get('status') == status]
    if min_score > 0:
        applicants = [a for a in applicants if a.get('score', 0) >= min_score]
    
    # Sort by score descending
    applicants.sort(key=lambda x: x.get('score', 0), reverse=True)
    
    return jsonify(applicants)

@app.route('/api/admin/stats')
def api_admin_stats():
    with open(APPLICANTS_FILE, 'r') as f:
        applicants = json.load(f)
    
    # Company wise stats calculation
    company_wise = {}
    for company in COMPANY_DATA:
        company_name = company['name']
        company_apps = [a for a in applicants if a['company'] == company_name]
        if company_apps:
            avg_score = sum(a['score'] for a in company_apps) / len(company_apps)
            top_score = max(a['score'] for a in company_apps)
        else:
            avg_score = 0
            top_score = 0
            
        company_wise[company_name] = {
            'total': len(company_apps),
            'avg_score': round(avg_score, 2),
            'top_score': top_score
        }
    
    stats = {
        'total_applications': len(applicants),
        'total_companies': len(COMPANY_DATA),
        'pending_review': len([a for a in applicants if a.get('status') == 'Pending']),
        'avg_score': round(sum([a['score'] for a in applicants]) / len(applicants), 2) if applicants else 0,
        'company_wise': company_wise
    }
    return jsonify(stats)

@app.route('/api/admin/update_status', methods=['POST'])
def api_update_status():
    data = request.json
    with open(APPLICANTS_FILE, 'r') as f:
        applicants = json.load(f)
    for app in applicants:
        if app['id'] == data.get('id'):
            app['status'] = data.get('status')
            send_status_email(app, data.get('status'))
            break
    with open(APPLICANTS_FILE, 'w') as f:
        json.dump(applicants, f, indent=2)
    return jsonify({'success': True})

@app.route('/api/admin/delete_applicant', methods=['POST'])
def delete_applicant():
    data = request.json
    with open(APPLICANTS_FILE, 'r') as f:
        applicants = json.load(f)
    new_applicants = [app for app in applicants if app['id'] != data.get('id')]
    with open(APPLICANTS_FILE, 'w') as f:
        json.dump(new_applicants, f, indent=2)
    return jsonify({'success': True})

@app.route('/api/admin/top10/<company>')
def api_top10(company):
    with open(APPLICANTS_FILE, 'r') as f:
        applicants = json.load(f)
    company_apps = [a for a in applicants if a['company'] == company]
    company_apps.sort(key=lambda x: x['score'], reverse=True)
    return jsonify(company_apps[:10])

@app.route('/api/admin/export_csv/<company>')
def export_csv(company):
    with open(APPLICANTS_FILE, 'r') as f:
        applicants = json.load(f)
    company_apps = [a for a in applicants if a['company'] == company]
    company_apps.sort(key=lambda x: x['score'], reverse=True)
    
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['Rank', 'Name', 'Email', 'Qualification', 'Score', 'Skill%', 'Exp%', 'Projects%', 'Cert%', 'Matched Skills', 'Status', 'Applied Date'])
    
    for idx, app in enumerate(company_apps[:10], 1):
        cw.writerow([
            idx, app['name'], app['email'], app.get('qualification', 'N/A'),
            f"{app['score']}%",
            f"{app.get('skill_score', 0)}%",
            f"{app.get('exp_score', 0)}%",
            f"{app.get('projects_score', 0)}%",
            f"{app.get('cert_score', 0)}%",
            ', '.join(app.get('matched_skills', [])[:5]),
            app.get('status', 'Pending'),
            app.get('applied_date', 'N/A')
        ])
    
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = f"attachment; filename={company}_Top10_{datetime.now().strftime('%Y%m%d')}.csv"
    output.headers["Content-type"] = "text/csv"
    return output

@app.route('/api/companies')
def api_companies():
    return jsonify(COMPANY_DATA)

# ========== SUBMIT APPLICATION ==========
@app.route('/submit_application', methods=['POST'])
def submit_application():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        qualification = request.form.get('qualification')
        company = request.form.get('company')
        resume_file = request.files.get('resume')
        
        print("\n" + "="*60)
        print("📥 NEW APPLICATION RECEIVED")
        print("="*60)
        print(f"👤 Name: {name}")
        print(f"📧 Email: {email}")
        print(f"🎓 Qualification: {qualification}")
        print(f"🏢 Company: {company}")
        print(f"📄 Resume: {resume_file.filename}")
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{timestamp}_{resume_file.filename}"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        resume_file.save(filepath)
        print(f"✅ Resume saved: {filename}")
        
        resume_text = extract_text_from_pdf(filepath)
        resume_skills = extract_skills_from_text(resume_text)
        print(f"🔍 Skills found: {len(resume_skills)}")
        
        score, matched_skills, missing_skills, scores_detail = calculate_match_score(resume_skills, company, resume_text)
        
        print(f" Skill Score: {scores_detail['skill_score']}%")
        print(f" Experience Score: {scores_detail['exp_score']}% ({scores_detail['exp_years']} years)")
        print(f" Projects Score: {scores_detail['projects_score']}% ({scores_detail['projects_count']} projects)")
        print(f" Certifications Score: {scores_detail['cert_score']}% ({scores_detail['cert_count']} certs)")
        print(f"🎯 FINAL SCORE: {score}%")
        
        applicant = {
            'id': timestamp,
            'name': name,
            'email': email,
            'qualification': qualification,
            'company': company,
            'resume': filename,
            'skills_found': resume_skills[:15],
            'matched_skills': matched_skills,
            'missing_skills': missing_skills,
            'score': score,
            'skill_score': scores_detail['skill_score'],
            'exp_score': scores_detail['exp_score'],
            'projects_score': scores_detail['projects_score'],
            'cert_score': scores_detail['cert_score'],
            'exp_years': scores_detail['exp_years'],
            'projects_count': scores_detail['projects_count'],
            'cert_count': scores_detail['cert_count'],
            'status': 'Pending',
            'applied_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        with open(APPLICANTS_FILE, 'r') as f:
            applicants = json.load(f)
        
        applicants.append(applicant)
        
        with open(APPLICANTS_FILE, 'w') as f:
            json.dump(applicants, f, indent=2)
        
        print(f"💾 Data saved")
        print("="*60 + "\n")
        
        return jsonify({
            'success': True,
            'message': f'✅ Application submitted successfully for {company}!',
            'score': score,
            'skill_score': scores_detail['skill_score'],
            'exp_score': scores_detail['exp_score'],
            'projects_score': scores_detail['projects_score'],
            'cert_score': scores_detail['cert_score'],
            'matched_skills': matched_skills,
            'missing_skills': missing_skills
        })
        
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500

if __name__ == '__main__':
    print("\n" + "="*80)
    print("🚀 AI RESUME SCREENING SYSTEM 2026 - READY!")
    print("="*80)
    print("🏢 Companies: 10 Top Tech Companies Loaded")
    print("📍 Home Page: http://localhost:5000")
    print("📍 Apply Page: http://localhost:5000/apply")
    print("📍 Admin Login: http://localhost:5000/admin")
    print("\n Admin Credentials:")
    print("   Username: admin")
    print("   Password: admin123")
    print("\n✅ FEATURES:")
    print("   • Skills Matching (50%)")
    print("   • Experience Years (25%)")
    print("   • Projects Count (15%)")
    print("   • Certifications (10%)")
    print("   • Email Notification")
    print("   • CSV Export")
    print("   • View Resume PDF")
    print("="*80)
    print("📁 JSON Database Files:")
    print(f"   • {APPLICANTS_FILE}")
    print(f"   • {COMPANIES_FILE}")
    print(f"   • {ADMIN_FILE}")
    print("="*80 + "\n")
    
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    print("\n" + "="*60)
    print("📱 SHARE THIS LINK WITH FRIENDS:")
    print(f"🔗 http://{ip_address}:5000")
    print("="*60)
    
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)





