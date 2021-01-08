from flask import Flask, render_template, flash, redirect, request
from forms import MainForm, M2, M3
from descMatrix import describeMatrix
app=Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess1'

@app.route('/',methods=['GET','POST'])
def mainPage():
	form=MainForm()
	if request.method == 'POST':
		order = form.choice.raw_data[0]
		print('{}'.format(form.choice.raw_data[0]))
		if str(order) == '2':
			form = M2()
		elif str(order)=='3':
			form=M3()
		print('Returning {}'.format(type(form)))
		return render_template('matrix.html',form=form, choice = order)
	return render_template('choice.html',title='Choice', form = form)

@app.route('/matrix/<order>',methods=['GET','POST']) 
def matrix(order):
	#order=2
	#form=M2()
	#return render_template('matrix.html',form=form, choice = order)
	form = None
	if str(order) == '2':
		form = M2()
	elif str(order)=='3':
		form=M3()
	if request.method == 'POST':
		print('Form is {}'.format(form)) 
		print('Returning p{}'.format(type(form)))
		mydict=describeMatrix(form.getMatrixRepresentation())
		return render_template('result.html',dict=mydict)
	return render_template('matrix.html',form=form, choice = order)

if __name__ == '__main__':
	app.run()
