from flask import Flask, render_template, request
import os
import shutil
from add_visual_features_main_modified import extract_all_features, apply_features

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/select_features', methods=['POST'])
def select_features():
    webpage_dir = request.form['webpage_dir']
    features = extract_all_features(webpage_dir)
    return render_template('feature_select.html', features=features, webpage_dir=webpage_dir)


@app.route('/generate', methods=['POST'])
def generate():
    selected_features = request.form.getlist('selected_features')
    webpage_dir = request.form['webpage_dir']

    output_html_path = apply_features(webpage_dir, selected_features)

    return render_template('result.html', message="Phishing webpages generated in folder: " + output_html_path)


if __name__ == '__main__':
    app.run(debug=True)
