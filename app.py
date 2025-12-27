# app.py (به‌روزرسانی شده)
from flask import Flask, render_template
import os # کتابخانه os را وارد کنید

app = Flask(__name__)

# --- این خط را اضافه کنید ---
# Render به یک SECRET_KEY نیاز دارد
# در محیط واقعی، این کلید باید از طریق متغیر محیطی (Environment Variable) لود شود.
# اما برای شروع می‌توانید یک کلید موقت اینجا قرار دهید.
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_default_secret_key_for_dev')
# --- پایان خط اضافه شده ---


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # در محیط محلی (Local)، از این دستور استفاده می‌شود.
    # در Render، Gunicorn از دستور Procfile استفاده می‌کند.
    app.run(debug=True)