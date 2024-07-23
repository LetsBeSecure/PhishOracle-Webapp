from flask import Flask, render_template, redirect, request, Response, send_file

from generate_features import generate_features, generate_final_html
import tempfile

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("input_form.html")


# Define a route to receive user input
@app.route('/input', methods=['GET', 'POST'])
def receive_input():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        print(user_input)
        print(type(user_input))
        # Perform logic to generate the list of features
        features = generate_features(user_input)
        # Render the checkbox form
        checkbox_form = render_template('checkbox_form.html', features=features)
        return checkbox_form
    return render_template('input_form.html')


# Define a route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    selected_features = request.form.getlist('selected_features')
    final_html = generate_final_html(selected_features)  # Replace with your logic
    # Perform logic to generate the final HTML content
    # features_list = generate_final_html(selected_features)
    return render_template('added_features.html', features=selected_features, final_html=final_html)


@app.route('/download', methods=['POST'])
def download_file():
    # Get the filename from the hidden input field in the form
    filename = request.form.get('filename')

    # Define the local path to the HTML file
    phishing_folder_path = "E:\\PhishOracle_Experiment_Complete\\PhishOracle_Web_App\\Phishing_Webpage\\" + filename

    # Send the file as a downloadable response
    return send_file(phishing_folder_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
