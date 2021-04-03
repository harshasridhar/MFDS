from flask import Flask, render_template, flash, redirect, request
from forms import MainForm, M2, M3, CacheReplacementAlgo, BuildTree, PreIn, PostIn, Parenthesis
from descMatrix import describeMatrix
from simulation import lru, fifo, lfu
from Problem import Problem
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

@app.route('/dsad',methods=['GET'])
def dsad():
	return render_template('dsad.html')

@app.route('/dsad/tree',methods=['GET','POST'])
def tree():
	form=BuildTree()
	if request.method == 'POST':
		combo=form.combo.raw_data[0]
		if combo == "Pre&In":
			form=PreIn()
			return render_template('prein.html',form=form)
		else:
			form=PostIn()
			return render_template('postin.html',form=form)
	return render_template('tree.html',form=form)

@app.route('/prein',methods=['POST'])
def preIn():
	prein=PreIn()
	p=Problem()
	tree=p.buildTree(prein.preorder.raw_data[0].split(','),prein.inorder.raw_data[0].split(','))
	prein.showResult=True
	prein.traversal=tree.getTreeRepresentation(order='post')
	return render_template('prein.html',form=prein)

@app.route('/parenthesis',methods=['GET'])
def parenthesis():
	return render_template('parenthesis.html',arr="",output='')
from code import main
@app.route('/parenthesis_py',methods=['GET','POST'])
def parenthesis_post():
	parenthesis=Parenthesis()
	if request.method == 'POST':
		int_array = [int(i) for i in parenthesis.arr.raw_data[0].strip().split(',')]
		output=main(int_array)
		parenthesis.output = output
	return render_template('parenthesis_python.html',form=parenthesis)

@app.route('/postin',methods=['POST'])
def postIn():
	postin=PostIn()
	p=Problem()
	tree=p.buildTreeFromPostOrderAndInorder(postin.postorder.raw_data[0].split(','),postin.inorder.raw_data[0].split(','))
	postin.showResult=True
	postin.traversal=tree.getTreeRepresentation(order='pre')
	return render_template('postin.html',form=postin) 



if __name__ == '__main__':
	app.run()
