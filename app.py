import os

from pathlib import Path

from flask import Flask, request, render_template, redirect, url_for, send_from_directory

from translator.video_translator import translate_video

app = Flask(__name__)

# ALLOWED_EXTENSIONS = set(['mp4',])
# MAX_FILE_SIZE = 2048 * 2048 + 1

root = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def upload_file():
    if request.method == 'POST':
        try:
            f = request.files['video_file']
            f.save(f.filename)
            t_video = translate_video(f.filename)
            # return redirect(url_for('play', video=get_file(t_video)))
            send_from_directory(root,t_video)
            return redirect(url_for('upload_file'))
        except Exception as e:
            return render_template('index.html', context=e)
    return render_template('index.html')

# @app.route('/video')
# def play():
#     return render_template('video.html')

if __name__ == "__main__":
    app.run(debug=True,port=3000)