import os
import random
import time
import requests
from bs4 import BeautifulSoup
import urllib.request
import webbrowser
import re
from urllib.parse import urlparse
from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
import xml.etree.ElementTree as ET
import cairosvg
import numpy as np

'''
=======================================    PHASE 3 (FUNCTION 1) BEGINS HERE  =======================================
In this function, we create an anchor tag with empty content
<a href="#">
<a href="#content">
<a href="#skip">
<a href="javascript::void(0)">
'''


def function_1(obtained_soup_here):
    print("Adding feature <a href=\"#\">")

    f1_soup = obtained_soup_here
    for el in f1_soup.find_all("a"):
        href_choice = ['#', '#content', '#skip', 'Javascript:void(0)']
        el["href"] = random.choice(href_choice)
        el["onclick"] = ""

    function_1_soup = f1_soup.prettify()

    return function_1_soup


'''
========================================    PHASE 3 (FUNCTION 1) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 2) BEGINS HERE  =======================================
In this feature, we disable the right click and CTRL options from viewing any source code content

Add attribute 'oncontextmenu="return false;"' in the body tag to disable the right click of the webpage
If wanted we can add an alert message if right clicked using javascript
javascript_code_to_append_for_alert = \'''
<script type="text/javascript"> 
function no_right_click() 
{ 
alert("Right click is not allowed for this page"); 
return false; 
} 
</script> 
\'''
and in the tag body the attribute should be 'oncontextmenu="return no_right_click();"'
'''


def function_2(obtained_soup_here):
    print("Adding feature 'Disabling Right Click, Fn key and CTRL key'")

    f2_soup = obtained_soup_here

    # Create a new script tag with the JavaScript content
    script_tag = f2_soup.new_tag("script", type="text/javascript")
    script_tag.string = """
        document.addEventListener('contextmenu', event => event.preventDefault());
        document.addEventListener('keydown', function(event) {
            if (event.ctrlKey) {
                event.preventDefault();
            }
        });
        """

    # Check if the head tag exists, if not create one and append it to the soup
    if f2_soup.head:
        f2_soup.head.append(script_tag)
    else:
        # If there's no head, check if body exists and append there
        if f2_soup.body:
            f2_soup.body.append(script_tag)
        else:
            # If there's neither head nor body, create a body and append the script
            body_tag = f2_soup.new_tag("body")
            body_tag.append(script_tag)
            f2_soup.append(body_tag)

    function_2_soup = f2_soup.prettify()

    return function_2_soup


'''
========================================    PHASE 3 (FUNCTION 2) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 3) BEGINS HERE  =======================================
In this feature we find and replace the domain name with look alike characters
'''


# Function to replace all characters in a domain to its look alike
def replace_all_characters(text, replacements):
    return ''.join(random.choice(replacements[char]) if char in replacements else char for char in text)


# Function to replace one character in a domain of href to its look alike
def replace_one_character(text, replacements):
    chars = list(text)
    indices = [i for i, char in enumerate(chars) if char in replacements]
    if indices:
        index = random.choice(indices)
        chars[index] = random.choice(replacements[chars[index]])
    return ''.join(chars)


# Function to replace domain name in href
def replace_domain_in_href(href, replacements):
    # Use regex to extract the domain name
    domain_pattern = re.compile(r'^(https?://)?([^/]+)')
    match = domain_pattern.match(href)
    if match:
        domain = match.group(2)
        modified_domain = replace_one_character(domain, replacements)
        return href.replace(domain, modified_domain)
    return href


def function_3(obtained_soup_here):
    print("Adding feature look alike domain name")

    f3_soup = obtained_soup_here

    # Define the look-alike characters
    char_replacements = {
        'a': ['ä', 'ẚ', 'á', 'ầ', 'ā', 'ä'],
        'b': ['b̀', 'b̂', 'b̃', 'ḇ̂', 'b̤', 'b̥'],
        'c': ['c̀', 'ć', 'c̃', 'c̈', 'ċ', 'c̓'],
        'd': ['d̊', 'd́', 'ď', 'ḑ', 'đ', 'd̥'],
        'e': ['è', 'ê', 'ē', 'ė', 'ë', 'e̊'],
        'i': ['í', 'ǐ', 'i̎', 'ḭ', 'ị'],
        'o': ['ó', 'ò', 'ṓ', 'ö', 'o̍']
    }

    for a_tag in f3_soup.find_all("a", href=True):
        original_href = a_tag['href']
        modified_href = replace_domain_in_href(original_href, char_replacements)
        a_tag['href'] = modified_href

    function_3_soup = f3_soup.prettify()

    return function_3_soup


'''
========================================    PHASE 3 (FUNCTION 3) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 4) BEGINS HERE  =======================================
In this feature we hide the links to appear on status bar on hovering links in a webpage when opened on a web browser
'''


def function_4(obtained_soup_here):
    print("Adding feature hiding links on status bar")

    f4_soup = obtained_soup_here

    for a_tag in f4_soup.find_all('a', href=True):
        original_href = a_tag['href']
        a_tag['onclick'] = f"window.open('{original_href}'); return false;"
        del a_tag['href']

    function_4_soup = f4_soup.prettify()

    return function_4_soup


'''
========================================    PHASE 3 (FUNCTION 4) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 5) BEGINS HERE  =======================================
In this feature we disable the anchor links from getting clicked by mouse when opened on a web browser
'''


def function_5(obtained_soup_here):
    print("Adding feature to disable anchor tags")

    f5_soup = obtained_soup_here

    for a_tag in f5_soup.find_all('a', href=True):
        if a_tag.has_attr('style'):
            present_style = a_tag['style']
            new_style = present_style + 'cursor:not-allowed; text-decoration:none;'
            a_tag['style'] = new_style
        else:
            a_tag['style'] = 'cursor:not-allowed; text-decoration:none;'

    function_5_soup = f5_soup.prettify()

    return function_5_soup


'''
========================================    PHASE 3 (FUNCTION 5) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 6) BEGINS HERE  =======================================
In this feature we replace the white spaces between texts with a number from 0 to 9 and make it transparent
'''


# Function to replace white spaces with a number inside span elements
def replace_whitespace_with_number(tag, f6_soup_cloned):
    new_contents = []
    for content in tag.contents:
        if isinstance(content, str):
            parts = content.split(' ')
            for i, part in enumerate(parts):
                new_contents.append(part)
                if i < len(parts) - 1:
                    # Create a new span with a random number
                    span = f6_soup_cloned.new_tag('span')
                    span.string = str(random.randint(0, 9))
                    span['style'] = 'color: transparent;'
                    new_contents.append(span)
        else:
            new_contents.append(content)

    tag.clear()
    for item in new_contents:
        tag.append(item)


def function_6(obtained_soup_here):
    print("Adding feature to replace blank space with a character")

    f6_soup = obtained_soup_here

    # Find and process specified tags
    for tag_name in ["p", "h1", "h2", "h3", "span", "a"]:
        tags = f6_soup.find_all(tag_name)
        for tag in tags:
            replace_whitespace_with_number(tag, f6_soup)

    function_6_soup = f6_soup.prettify()

    return function_6_soup


'''
========================================    PHASE 3 (FUNCTION 6) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 7) BEGINS HERE  =======================================
In this feature we modify the action field in the form tag to save the credentials to local file
'''


def function_7(obtained_soup_here):
    print("Adding feature to modify action field to save form credentials")

    f7_soup = obtained_soup_here

    for form_tag in f7_soup.find_all('form'):
        form_tag['action'] = ''

    # Add JavaScript code to handle form submission
    script_code = """
        <script>
            function handleSubmit(event) {
                event.preventDefault(); // Prevent form submission

                // Get form inputs
                var form = event.target;
                var formData = new FormData(form);

                // Convert FormData to object
                var formObject = {};
                formData.forEach(function(value, key){
                    formObject[key] = value;
                });

                // Convert object to JSON string
                var jsonData = JSON.stringify(formObject);

                // Save data to a file
                var fileContents = "Form Inputs:\\n" + jsonData;
                var fileBlob = new Blob([fileContents], {type: "text/plain"});
                var fileUrl = URL.createObjectURL(fileBlob);

                // Create a link to download the file
                var downloadLink = document.createElement("a");
                downloadLink.href = fileUrl;
                downloadLink.download = "form_inputs.txt";
                downloadLink.click();
            }

            // Add event listener to the form
            var formElement = document.querySelector('form');
            if (formElement) {
                formElement.addEventListener("submit", handleSubmit);
            } else {
                console.error("Form not found.");
            }
        </script>
        """

    # Append the JavaScript code to the end of the HTML body
    if f7_soup.body:
        f7_soup.body.append(BeautifulSoup(script_code, "html.parser"))
    elif f7_soup.html:
        f7_soup.html.append(BeautifulSoup(script_code, "html.parser"))
    else:
        print("[WARNING] No <body> or <html> tag found.")

    function_7_soup = f7_soup.prettify()

    return function_7_soup


'''
========================================    PHASE 3 (FUNCTION 7) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 8) BEGINS HERE  =======================================
In this feature we disable other login buttons, except the one with the submit button of form
'''


# Function to disable an element
def disable_element(element):
    element['onclick'] = 'return false;'
    element['style'] = 'pointer-events: none; cursor: default;'


def function_8(obtained_soup_here):
    print('Disabling other login buttons')

    f8_soup = obtained_soup_here

    # Define the list of keywords to check in the text content
    keywords = ['google', 'github', 'facebook', 'linkedin', 'twitter', 'instagram']

    # Iterate over each tag to check and disable
    for tag in f8_soup.find_all('a'):
        # Check if the text content contains any of the keywords
        if any(keyword in tag.get_text().strip().lower() for keyword in keywords):
            disable_element(tag)

    icon_classes = ['fa-google', 'fa-github', 'fa-facebook', 'fa-linkedin', 'fa-twitter', 'fa-instagram']
    icon_aria_labels = ['google', 'github', 'facebook', 'linkedin', 'Twitter', 'Instagram']

    # Check and disable <button> tags
    for tag in f8_soup.find_all('button'):
        if tag.get('type') == 'button':
            if any(icon_aria_label in tag.get('aria-label', '').lower() for icon_aria_label in icon_aria_labels):
                disable_element(tag)
        else:
            tag_text = tag.get_text().strip().lower()
            if any(keyword in tag_text for keyword in keywords):
                if any(icon_class in tag.get('class', []) for icon_class in icon_classes):
                    disable_element(tag)
                else:
                    # Check for icons within the tag
                    for icon_class in icon_classes:
                        if tag.find(class_=icon_class):
                            disable_element(tag)
                            break

    function_8_soup = f8_soup.prettify()

    return function_8_soup


'''
========================================    PHASE 3 (FUNCTION 8) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 9) BEGINS HERE  =======================================
In this feature we make use of the pop up login and save the credentials to local
'''


def function_9(obtained_soup_here):
    print("Adding feature pop-up login and save credentials")

    # Load HTML content from a file or obtained from previous steps
    f9_soup = obtained_soup_here

    # Ensure <html> and <body> tags exist
    if f9_soup.html is None:
        f9_soup.append(BeautifulSoup('<html></html>', 'html.parser'))
    if f9_soup.html.body is None:
        f9_soup.html.append(BeautifulSoup('<body></body>', 'html.parser'))

    # Find the form tag that contains input fields
    form_tag = f9_soup.find('form')

    if not form_tag:
        print("No form tag found.")
        return f9_soup.prettify()

    # Copy the entire form tag to a variable
    copied_form_html = str(form_tag.parent)

    # Remove input tags from the original form
    for input_tag in form_tag.find_all('input'):
        input_tag.decompose()

    # Add class, href, and onclick attributes to buttons
    for button_change in f9_soup.find_all('button'):
        button_change['class'] = "_button"
        button_change['href'] = "#"
        button_change['onclick'] = "showPopup()"
        button_change.string = "Login"

    # Create a div tag for the popup form
    pop_up_div_tag_add_string = f'<div class="popup" id="popup" style="display: none; position: fixed; top: 50%; ' \
                                f'left: 50%; transform: translate(-50%, -50%); background-color: white; padding: ' \
                                f'20px; border: 1px solid #ccc; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); z-index: ' \
                                f'9999;">{copied_form_html}</div> '
    pop_up_div_tag = BeautifulSoup(pop_up_div_tag_add_string, 'html.parser')

    # Append the div tag for the popup form to the body
    f9_soup.html.body.append(pop_up_div_tag)

    # Add JavaScript code to show and hide the popup
    script_tag_for_pop_up = f"""
        <script>
            function showPopup() {{
                document.getElementById('popup').style.display = 'block';
            }}

            function hidePopup() {{
                document.getElementById('popup').style.display = 'none';
            }}

            function handleSubmit(event) {{
                event.preventDefault(); // Prevent form submission

                // Get form inputs
                var form = event.target;
                var formData = new FormData(form);

                // Convert FormData to object
                var formObject = {{}};
                formData.forEach(function(value, key){{
                    formObject[key] = value;
                }});

                // Convert object to JSON string
                var jsonData = JSON.stringify(formObject);

                // Save data to a file
                var fileContents = "Form Inputs:\\n" + jsonData;
                var fileBlob = new Blob([fileContents], {{type: "text/plain"}});
                var fileUrl = URL.createObjectURL(fileBlob);

                // Create a link to download the file
                var downloadLink = document.createElement("a");
                downloadLink.href = fileUrl;
                downloadLink.download = "form_inputs.txt";
                downloadLink.click();
            }}

            document.addEventListener("DOMContentLoaded", function() {{
                var popupForm = document.querySelector("#popup form");
                if (popupForm) {{
                    popupForm.addEventListener("submit", handleSubmit);
                }} else {{
                    console.error("Popup form not found.");
                }}
            }});
        </script>
        """

    # Check if the head tag exists, if not create one and append it to the soup
    if f9_soup.head:
        f9_soup.head.append(script_tag_for_pop_up)
    else:
        # If there's no head, check if body exists and append there
        if f9_soup.body:
            f9_soup.body.append(script_tag_for_pop_up)
        else:
            # If there's neither head nor body, create a body and append the script
            body_tag = f9_soup.new_tag("body")
            body_tag.append(script_tag_for_pop_up)
            f9_soup.append(body_tag)

    # Save the modified HTML content to a file or use it further
    function_9_soup = f9_soup.prettify()

    return function_9_soup


'''
========================================    PHASE 3 (FUNCTION 9) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 10) BEGINS HERE  =======================================
In this feature we make various anchor tags that when clicked will open pop-up login form
'''


def function_10(obtained_soup_here):
    print("Adding feature to use pop-up login on various anchor tags")

    # Load HTML content from a file or obtained from previous steps
    f10_soup = obtained_soup_here

    # Find the form tag containing input fields and copy its content to a variable
    form_tag = f10_soup.find("form")
    copied_form_html = str(form_tag)

    # Find all anchor tags and add onclick attribute to open popup
    anchor_tags = f10_soup.find_all("a")
    for anchor_tag in anchor_tags:
        anchor_tag['href'] = "#"
        anchor_tag['onclick'] = "showPopup()"

    # Create a div tag for the popup form
    pop_up_div_tag_add_string = f'<div class="popup" id="popup" style="display: none; position: fixed; top: 50%; ' \
                                f'left: 50%; transform: translate(-50%, -50%); background-color: white; padding: ' \
                                f'20px; border: 1px solid #ccc; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); z-index: ' \
                                f'9999;">{copied_form_html}</div> '
    pop_up_div_tag = BeautifulSoup(pop_up_div_tag_add_string, 'html.parser')

    # Append the div tag for the popup form to the body
    f10_soup.html.body.append(pop_up_div_tag)

    # Implement JavaScript code to show the popup form
    popup_script = """
        <script>
        function showPopup() {
            document.getElementById("popup").style.display = "block";
        }
        function hidePopup() {
            document.getElementById("popup").style.display = "none";
        }
        </script>
        """
    f10_soup.body.append(BeautifulSoup(popup_script, "html.parser"))

    # Implement JavaScript code to handle form submission and save input values
    form_script = """
        <script>
        function handleSubmit(event) {
            event.preventDefault(); // Prevent form submission

            // Get form inputs
            var form = event.target;
            var formData = new FormData(form);

            // Convert FormData to object
            var formObject = {};
            formData.forEach(function(value, key){
                formObject[key] = value;
            });

            // Convert object to JSON string
            var jsonData = JSON.stringify(formObject);

            // Save data to a file
            var fileContents = "Form Inputs:\\n" + jsonData;
            var fileBlob = new Blob([fileContents], {type: "text/plain"});
            var fileUrl = URL.createObjectURL(fileBlob);

            // Create a link to download the file
            var downloadLink = document.createElement("a");
            downloadLink.href = fileUrl;
            downloadLink.download = "form_inputs.txt";
            downloadLink.click();
        }

        document.addEventListener("DOMContentLoaded", function() {
            var popupForm = document.querySelector("#popup form");
            if (popupForm) {
                popupForm.addEventListener("submit", handleSubmit);
            } else {
                console.error("Popup form not found.");
            }
        });
        </script>
        """
    f10_soup.body.append(BeautifulSoup(form_script, 'html.parser'))

    # Save the modified HTML content to a file or use it further
    function_10_soup = f10_soup.prettify()

    return function_10_soup


'''
========================================    PHASE 3 (FUNCTION 10) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 11) BEGINS HERE  =======================================
In this feature we make iframe containing login form and save the input values to local file
'''


def function_11(obtained_soup_here):
    print("Add feature iframe containing form and save credentials")

    # Load HTML content from a file or obtained from previous steps
    f11_soup = obtained_soup_here

    # Ensure <html> and <body> tags exist
    if f11_soup.html is None:
        f11_soup.append(BeautifulSoup('<html></html>', 'html.parser'))
    if f11_soup.html.body is None:
        f11_soup.html.append(BeautifulSoup('<body></body>', 'html.parser'))

    # Find the form tag containing input fields and copy its content to a variable
    form_tag = f11_soup.find("form")
    copied_form_html = str(form_tag)

    # Create an iframe tag
    iframe_tag_add_string = f"""
        <iframe id="formIframe" style="width: 100%; height: 500px; border: none;" title="Loin Form"></iframe>
        <script>
            document.addEventListener("DOMContentLoaded", function() {{
                var iframe = document.getElementById("formIframe");
                var doc = iframe.contentDocument || iframe.contentWindow.document;
                doc.open();
                doc.write(`<b>Login Here</b><br>{copied_form_html}`);
                doc.close();

                // Add JavaScript to handle form submission within the iframe
                var script = doc.createElement("script");
                script.type = "text/javascript";
                script.innerHTML = `
                    function handleSubmit(event) {{
                        event.preventDefault(); // Prevent form submission

                        // Get form inputs
                        var form = event.target;
                        var formData = new FormData(form);

                        // Convert FormData to object
                        var formObject = {{}};
                        formData.forEach(function(value, key) {{
                            formObject[key] = value;
                        }});

                        // Convert object to JSON string
                        var jsonData = JSON.stringify(formObject);

                        // Save data to a file
                        var fileContents = "Form Inputs:\\n" + jsonData;
                        var fileBlob = new Blob([fileContents], {{ type: "text/plain" }});
                        var fileUrl = URL.createObjectURL(fileBlob);

                        // Create a link to download the file
                        var downloadLink = document.createElement("a");
                        downloadLink.href = fileUrl;
                        downloadLink.download = "form_inputs.txt";
                        downloadLink.click();
                    }}

                    // Add event listener to the form
                    var iframeForm = doc.querySelector("form");
                    if (iframeForm) {{
                        iframeForm.addEventListener("submit", handleSubmit);
                    }} else {{
                        console.error("Form not found.");
                    }}
                `;
                doc.body.appendChild(script);
            }});
        </script>
        """
    iframe_tag = BeautifulSoup(iframe_tag_add_string, 'html.parser')

    # Check if the head tag exists, if not create one and append it to the soup
    if f11_soup.head:
        f11_soup.head.append(iframe_tag)
    else:
        # If there's no head, check if body exists and append there
        if f11_soup.body:
            f11_soup.body.append(iframe_tag)
        else:
            # If there's neither head nor body, create a body and append the script
            body_tag = f11_soup.new_tag("body")
            body_tag.append(iframe_tag)
            f11_soup.append(body_tag)

    # Save the modified HTML content to a file or use it further
    function_11_soup = f11_soup.prettify()

    return function_11_soup


'''
========================================    PHASE 3 (FUNCTION 11) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 12) BEGINS HERE  =======================================
In this feature we increase the DOM structure of the webpage by adding <link>, <script>, <img>, <a> and <div> tags
'''


# Function to randomly pick an image
def get_random_image(image_folder, image_list):
    return f"{image_folder}/{random.choice(image_list)}"


def function_12(obtained_soup_here):
    print("Adding feature to increase DOM structure")

    # Load HTML content from a file or obtained from previous steps
    f12_soup = obtained_soup_here

    # Ensure <html> and <body> tags exist
    if f12_soup.html is None:
        f12_soup.append(BeautifulSoup('<html></html>', 'html.parser'))
    if f12_soup.html.body is None:
        f12_soup.html.append(BeautifulSoup('<body></body>', 'html.parser'))

    # Define the list of local images
    image_folder = "../advertisement_images"
    image_list = ["amazon_advertisement.png", "myntra_advertisement.png", "flipkart_advertisement.png", "zoodio.png"]

    # Container for the new elements
    new_elements_container = f12_soup.new_tag("div", **{"class": "new-elements-container"})

    # Add <script> tag
    script_tag = f12_soup.new_tag("script", src="https://example.com/script.js")
    new_elements_container.append(script_tag)

    # Add <link> tag for stylesheet
    link_tag = f12_soup.new_tag("link", rel="stylesheet", href="https://example.com/styles.css")
    new_elements_container.append(link_tag)

    # Copy the form tag containing inputs
    form_tag = f12_soup.find("form")
    copied_form_html = str(form_tag)

    # Add a section for the new div tags with appealing content
    appealing_section = f12_soup.new_tag("div", **{"class": "appealing-section"})
    appealing_heading = f12_soup.new_tag("h2")
    appealing_heading.string = "Explore Our Features"
    appealing_section.append(appealing_heading)

    div_texts = [
        "Unlock new opportunities today!",
        "Stay ahead with the latest updates.",
        "Discover the power of innovation.",
        "Join our community and grow with us.",
        "Experience the future of technology."
    ]

    for i, text in enumerate(div_texts):
        anchor_tag = f12_soup.new_tag("a", **{"href": "#", "class": f"new-div-{i}", "onclick": "showPopup()",
                                              "style": "display: block; margin-bottom: 10px;"})
        anchor_tag.string = text
        appealing_section.append(anchor_tag)

    new_elements_container.append(appealing_section)

    # Create a div tag for the popup form
    pop_up_div_tag_add_string = f'<div class="popup" id="popup" style="display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: white; padding: 20px; border: 1px solid #ccc; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); z-index: 9999;">{copied_form_html}</div>'
    pop_up_div_tag = BeautifulSoup(pop_up_div_tag_add_string, 'html.parser')

    # Check if the head tag exists, if not create one and append it to the soup
    if f12_soup.head:
        f12_soup.head.append(pop_up_div_tag)
    else:
        # If there's no head, check if body exists and append there
        if f12_soup.body:
            f12_soup.body.append(pop_up_div_tag)
        else:
            # If there's neither head nor body, create a body and append the script
            body_tag = f12_soup.new_tag("body")
            body_tag.append(pop_up_div_tag)
            f12_soup.append(body_tag)

    # Implement JavaScript code to handle form submission and save input values
    form_script = """
        <script>
            function showPopup() {
                document.getElementById('popup').style.display = 'block';
            }

            function handleSubmit(event) {
                event.preventDefault(); // Prevent form submission

                // Get form inputs
                var form = event.target;
                var formData = new FormData(form);

                // Convert FormData to object
                var formObject = {};
                formData.forEach(function(value, key){
                    formObject[key] = value;
                });

                // Convert object to JSON string
                var jsonData = JSON.stringify(formObject);

                // Save data to a file
                var fileContents = "Form Inputs:\\n" + jsonData;
                var fileBlob = new Blob([fileContents], {type: "text/plain"});
                var fileUrl = URL.createObjectURL(fileBlob);

                // Create a link to download the file
                var downloadLink = document.createElement("a");
                downloadLink.href = fileUrl;
                downloadLink.download = "form_inputs.txt";
                downloadLink.click();
            }

            document.addEventListener("DOMContentLoaded", function() {
                var popupForm = document.querySelector("#popup form");
                if (popupForm) {
                    popupForm.addEventListener("submit", handleSubmit);
                } else {
                    console.error("Popup form not found.");
                }
            });
        </script>
        """

    # Check if the head tag exists, if not create one and append it to the soup
    if f12_soup.head:
        f12_soup.head.append(form_script)
    else:
        # If there's no head, check if body exists and append there
        if f12_soup.body:
            f12_soup.body.append(form_script)
        else:
            # If there's neither head nor body, create a body and append the script
            body_tag = f12_soup.new_tag("body")
            body_tag.append(form_script)
            f12_soup.append(body_tag)

    # Add a section for the image grid
    grid_section = f12_soup.new_tag("div", **{"class": "grid-section"})
    grid_heading = f12_soup.new_tag("h2")
    grid_heading.string = "Our Sponsors"
    grid_section.append(grid_heading)

    grid_container = f12_soup.new_tag("div", **{"class": "grid-container"})
    for i in range(len(image_list)):
        img_tag = f12_soup.new_tag("img", src=f"{image_folder}/{image_list[i]}", alt="Advertisement Image",
                                   **{"class": "grid-item"})
        grid_container.append(img_tag)

    grid_section.append(grid_container)
    new_elements_container.append(grid_section)

    # Add CSS for the grid layout and fixed image dimensions
    style_tag = f12_soup.new_tag("style")
    style_tag.string = """
        .new-elements-container {
            margin-top: 20px;
        }
        .appealing-section, .grid-section, .iframe-section, .nested-section {
            margin-bottom: 40px;
            padding: 20px;
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .appealing-section h2, .grid-section h2, .iframe-section h2, .nested-section h2 {
            margin-top: 0;
        }
        .grid-container {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            grid-gap: 10px;
            max-width: 600px;
            margin: auto;
        }
        .grid-item {
            width: 100%;  /* Ensures image fits within its grid cell */
            height: auto; /* Maintains aspect ratio */
            max-width: 100%;
            max-height: 100%;
            object-fit: cover; /* Ensures image covers the grid cell without distortion */
        }
        """
    # Check if the head tag exists, if not create one and append it to the soup
    if f12_soup.head:
        f12_soup.head.append(style_tag)
    else:
        # If there's no head, check if body exists and append there
        if f12_soup.body:
            f12_soup.body.append(style_tag)
        else:
            # If there's neither head nor body, create a body and append the script
            body_tag = f12_soup.new_tag("body")
            body_tag.append(style_tag)
            f12_soup.append(body_tag)

    # Check if the head tag exists, if not create one and append it to the soup
    if f12_soup.head:
        f12_soup.head.append(new_elements_container)
    else:
        # If there's no head, check if body exists and append there
        if f12_soup.body:
            f12_soup.body.append(new_elements_container)
        else:
            # If there's neither head nor body, create a body and append the script
            body_tag = f12_soup.new_tag("body")
            body_tag.append(new_elements_container)
            f12_soup.append(body_tag)

    # Save the modified HTML content to a file or use it further
    function_12_soup = f12_soup.prettify()

    return function_12_soup


'''
========================================    PHASE 3 (FUNCTION 12) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 13) BEGINS HERE  =======================================
In this feature we add body opacity to the webpage to make it quite transparent
'''


def function_13(obtained_soup_here):
    print("Adding feature we add body opacity")

    # Load HTML content from a file or obtained from previous steps
    f13_soup = obtained_soup_here

    body_tag = f13_soup.find('body')
    if body_tag:
        opacity_values = [0.37, 0.42, 0.6]
        if body_tag.has_attr('style'):
            original_style = body_tag['style']
            new_style = original_style + f'opacity: {random.choice(opacity_values)};'
            body_tag['style'] = new_style
        else:
            body_tag['style'] = f'opacity: {random.choice(opacity_values)};'

    # Save the modified HTML content to a file or use it further
    function_13_soup = f13_soup.prettify()

    return function_13_soup


'''
========================================    PHASE 3 (FUNCTION 13) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 14) BEGINS HERE  =======================================
In this feature we change the text font family
'''


def function_14(obtained_soup_here):
    print("Adding feature to change the font-family of text")

    # Load HTML content from a file or obtained from previous steps
    f14_soup = obtained_soup_here

    font_families = [
        "Times New Roman", "Georgia", "Palatino", "Book Antiqua", "Cambria",
        "Arial", "Helvetica", "Calibri", "Verdana", "Tahoma",
        "Courier New", "Lucida Console", "Monaco",
        "Comic Sans MS", "Brush Script MT", "Lucida Handwriting", "Snell Roundhand"
    ]

    tags_to_change = ["p", "h1", "h2", "h3", "span", "a"]

    for tag_name in tags_to_change:
        tags = f14_soup.find_all(tag_name)
        for tag in tags:
            if tag.has_attr('style'):
                original_style = tag['style']
                new_style = original_style + f"font-family: {random.choice(font_families)};"
                tag['style'] = new_style
            else:
                tag['style'] = f"font-family: {random.choice(font_families)};"

    # Save the modified HTML content to a file or use it further
    function_14_soup = f14_soup.prettify()

    return function_14_soup


'''
========================================    PHASE 3 (FUNCTION 14) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 15) BEGINS HERE  =======================================
In this feature we add opacity to the logo
'''


def function_15(obtained_soup_here):
    print("Adding feature of logo opacity")

    # Load HTML content from a file or obtained from previous steps
    f15_soup = obtained_soup_here

    # Find all img, svg, and a tags
    all_tags = f15_soup.find_all(['img', 'svg', 'a'])

    # List to store attributes to modify
    attributes_to_modify = []

    # Check if any tag attributes contain the term "logo" and add opacity style if found
    for tag in all_tags:
        for attr, value in tag.attrs.items():
            if "logo" in str(value).lower():
                attributes_to_modify.append(tag)
                break  # Break out of the inner loop once logo is found in current tag

    # Modify the attributes after the iteration
    for tag in attributes_to_modify:
        opacity_values = [0.15, 0.25, 0.35]
        if "style" in tag.attrs:
            original_style = tag['style']
            new_style = original_style + f'opacity: {random.choice(opacity_values)};'
            tag['style'] = new_style
        else:
            tag["style"] = f'opacity: {random.choice(opacity_values)};'

    # Save the modified HTML content to a file or use it further
    function_15_soup = f15_soup.prettify()

    return function_15_soup


'''
========================================    PHASE 3 (FUNCTION 15) ENDS HERE  ========================================
'''

'''
Read total features to add
'''


def get_total_features():
    with open("add_total_features.txt", 'r', encoding='utf-8') as f_input_features:
        features_to_add = int(f_input_features.read())

    return features_to_add


'''
Add all the features from this main file
'''


def add_features_now(modified_html_file):
    k = get_total_features()

    html_content = ''
    with open(modified_html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'lxml')

    # Check applicability of each function
    applicable_functions = []
    if soup.find("a"):
        function_to_add = random.choice([function_1, function_3, function_5, function_8])
        # function_to_add = random.choice([function_1])
        # function_to_add = random.choice([function_1])
        applicable_functions.append(function_to_add)
        applicable_functions.append(function_4)
    # if soup.find("p") or soup.find("h1") or soup.find("h2") or soup.find("h3") or soup.find("span"):
    #     applicable_functions.append(function_6)
    #     applicable_functions.append(function_14)
    form_tag = soup.find("form")
    if form_tag:
        # function_forms_to_add = random.choice([function_7, function_9, function_10, function_11, function_12])
        function_forms_to_add = random.choice([function_7])
        applicable_functions.append(function_forms_to_add)
    # if soup.find("body"):
    #     applicable_functions.append(function_13)
    applicable_functions.append(function_2)

    # Randomly select K functions
    selected_functions = random.sample(applicable_functions, min(k, len(applicable_functions)))

    # Apply each selected function
    for func in selected_functions:
        modified_soup = func(soup)
        # Save the modified HTML
        with open(modified_html_file, 'w', encoding='utf-8') as file:
            file.write(str(modified_soup))

FEATURE_FUNCTIONS_MAP = {
    "feature_1": function_1,
    "feature_2": function_2,
    "feature_3": function_3,
    "feature_4": function_4,
    "feature_5": function_5,
    "feature_6": function_6,
    "feature_7": function_7,
    "feature_8": function_8,
    "feature_9": function_9,
    "feature_10": function_10,
    "feature_11": function_11,
    "feature_12": function_12,
    "feature_13": function_13,
    "feature_14": function_14,
    "feature_15": function_15,
}

def apply_selected_content_features(modified_html_file, selected_feature_names):
    html_content = ''
    with open(modified_html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'lxml')

    for fname in selected_feature_names:
        func = FEATURE_FUNCTIONS_MAP.get(fname)
        if func:
            # soup = func(soup)
            result = func(soup)
            soup = result if isinstance(result, BeautifulSoup) else BeautifulSoup(result, 'lxml')
    with open(modified_html_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))
