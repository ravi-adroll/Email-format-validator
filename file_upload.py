from flask import *  
from temp1 import *

app = Flask(__name__)  
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        if f.filename=='':
            return 'Select a File'
        if f.filename.split(".")[1]=='csv':
        	# print(f.filename)
            f.save(f.filename)
           	# dup_email.clear()
            # error_mails.clear()
            # exec_csv('CRM_test.csv')
            exec_csv(f.filename)
            # print(TOTAL_LINE)
            return render_template('success.html',name=f.filename,dup_email=dup_email,error_emails=error_mails,TOTAL_LINE=TOTAL_LINE)	# return render_template("success.html", name = f.filename)  
        else:
        	return ("Please upload a file in csv formmat")
print(TOTAL_LINE)

if __name__ == '__main__':  
    app.run(debug = True)  
