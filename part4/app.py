from flask import Flask, render_template, request
from markupsafe import escape
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("SENDER_EMAIL"))
print(os.getenv("SENDER_PASSWORD"))

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/contactme')
def contactme():
    return render_template('contactme.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/submit', methods=['POST'])
def submit_contact_form():
    name = request.form.get('name')
    email = request.form.get('email')
    questions = request.form.get('questions')

    # Email configuration
    sender_email = os.getenv("SENDER_EMAIL")
    receiver_email = 'edwartro000+apcsfinal@frogrock.org'
    subject = 'Contact Form Submission'
    message = f"Name: {name}\nEmail: {email}\nQuestions: {questions}"

    try:
        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, os.getenv("SENDER_PASSWORD"))
            smtp.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{message}")

        # Redirect to a success page
        return render_template('success.html')
    except Exception as e:
        # Display an error message
        return render_template('error.html', error=str(e))
