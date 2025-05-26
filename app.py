from flask import Flask, render_template, request
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message=None)

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'cookiesfrombrowser': ('chrome',),  # ← مهم برای استفاده از کوکی مرورگر
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
        return render_template('index.html', message=f"✅ ویدیو دانلود شد: {info['title']}")
    except Exception as e:
        return render_template('index.html', message=f"❌ خطا در دانلود: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
