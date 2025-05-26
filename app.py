<<<<<<< HEAD
from flask import Flask, render_template, request
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
        return f"✅ ویدیو دانلود شد: {info['title']}"
    except Exception as e:
        return f"❌ خطا: {str(e)}"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
=======
from flask import Flask, request, render_template
import yt_dlp

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    formats = []
    error = None
    if request.method == "POST":
        url = request.form["url"]
        try:
            ydl_opts = {"quiet": True, "skip_download": True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                formats = info.get("formats", [])
        except Exception as e:
            error = f"❌ خطا: {str(e)}"
    return render_template("index.html", formats=formats, error=error)
>>>>>>> f1df5fb9c81137dd808257a46c961906ff9a554c
