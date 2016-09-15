from config import ERROR_MSG_INVALID_FILE_EXTENSION
from divisibility import app
import division
from exception import InputError
import parser
import validator

from flask import Flask, Response, render_template, request, redirect, url_for

"""
Verifies if given file is allowed in the system based on file extension.
Arguments:
    filename - string (e.g. "input.txt")
Returns:
    boolean
"""
def allowed_file(filename):
    #splits extension and verifies if is contained on app allowed extensions
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

"""
Template stream used to ease larger output latency. A standard 10 items buffering is used.
Arguments:
    template_name - string (e.g. "output.html")
    context - return object to be streamed
Returns:
    template with streaming data
"""
def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    response = t.stream(context)
    response.enable_buffering(10)
    return response

"""
Route for index rendering
Arguments:
    None
Returns:
    index template
"""
@app.route('/')
def index():
    return render_template('index.html')

"""
Route for processing file upload.
Arguments:
    file - file passed implicit as request parameter
Returns:
    template with streaming data
"""
@app.route('/upload', methods=['POST'])
def upload():

    #gets file from request
    file_f = request.files['file']

    #check if the file is one of the allowed types/extensions, otherwise returns error
    if not file_f or not allowed_file(file_f.filename):
        return render_template('error.html', error_message = ERROR_MSG_INVALID_FILE_EXTENSION)

    #parse and validation of input, if any exception is raised, captures message and displays
    input_data = None
    try:
        #parse file
        input_data = parser.parse_file(file_f)
    except InputError as ie:
        return render_template('error.html', error_message = ie.msg)

    #process each entry in the input separately
    output = []
    for entry in input_data:
        n,x,y = entry
        output.append(division.get_divisible(n, x, y))

    #close input file
    file_f.close()

    #returns
    #return render_template('output.html', output=output)
    return Response(stream_template('output.html', output=output))
