from flask import Flask, render_template, flash, redirect, request
from forms import MainForm, M2, M3, CacheReplacementAlgo
from descMatrix import describeMatrix
from simulation import lru, fifo, lfu
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

@app.route('/coss/cache_replacement_algo',methods=['GET','POST'])
def cache_replacement_algo():
	c=CacheReplacementAlgo()
	if request.method == 'GET':
		return render_template('cache_replacement_algo.html', form=c)
	else:
		c.showResult=True
		choice=c.algos.raw_data[0]
		if choice == 'LRU':
			stepsStr,cache,hits,hit_ratio=lru(c.access_pattern.raw_data[0].split(','),max_cache_size=int(c.cache_size.raw_data[0]))
		elif choice == 'FIFO':
			stepsStr,cache,hits,hit_ratio=fifo(c.access_pattern.raw_data[0].split(','),max_cache_size=int(c.cache_size.raw_data[0]))
		else: 
			stepsStr,cache,hits,hit_ratio=lfu(c.access_pattern.raw_data[0].split(','),max_cache_size=int(c.cache_size.raw_data[0]))
		c.text=stepsStr.split('\n')[:-1]
		c.cache=cache
		c.hit_count=hits
		c.hit_ratio=hit_ratio
		return render_template('cache_replacement_algo.html', form=c)
		# pass

if __name__ == '__main__':
	app.run()
