from flask import send_from_directory
from modules.report_generator import generate_pdf
from flask import send_from_directory
from flask import Flask, request, render_template
import hashlib, os
from PIL import Image
from PIL.ExifTags import TAGS
import magic
from datetime import datetime
from modules.timeline_generator import extract_events, generate_timeline 

app = Flask(__name__)
app.secret_key = 'forensics123'
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_hashes(filepath):
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()
    with open(filepath,'rb') as f:
        while chunk := f.read(8192):
            md5.update(chunk)
            sha256.update(chunk)
    return md5.hexdigest(), sha256.hexdigest()

def get_exif(filepath):
    try:
        img = Image.open(filepath)
        exif = {}
        if hasattr(img, '_getexif'):
            exifdata = img._getexif()
            if exifdata:
                for tag_id, value in exifdata.items():
                    tag = TAGS.get(tag_id, tag_id)
                    exif[tag] = str(value)
        return exif if exif else {"Info": "No EXIF data found"}
    except:
        return {"Info": "Not an image or no EXIF"}
@app.route('/', methods=['GET','POST'])
def index():
    result = None
    pdf_file = None 

    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename != '':
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            events = extract_events(filepath) 
            timeline = generate_timeline(events) 

            md5, sha256 = get_hashes(filepath)
            file_type = magic.Magic(mime=True).from_file(filepath)
            size = f"{os.path.getsize(filepath)/1024:.2f} KB"

            result = {
                "Filename": file.filename,
                "File Type": file_type,
                "File Size": size,
                "MD5 Hash": md5,
                "SHA256 Hash": sha256,
                "Upload Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Timeline": timeline
            }

            pdf_file = generate_pdf(result)

            if 'image' in file_type:
                result.update({"--- EXIF Data ---": ""})
                result.update(get_exif(filepath))

    return render_template("index.html", result=result, pdf_file=pdf_file)
@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory("reports", filename, as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True)