from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, DecimalField, TextField
from wtforms.validators import DataRequired

class MainForm(FlaskForm):
	
	#def __init__(self):
	choice= SelectField('MatrixType',choices=[("2","2x2"),("3","3x3")])
	submit = SubmitField('Apply matrix dimensions')

class M2(FlaskForm):
	
	a11=DecimalField('a11',places=2,render_kw={"placeholder": "a11"})
	a12=DecimalField('a12',places=2,render_kw={"placeholder": "a12"})

	a21=DecimalField('a21',places=2,render_kw={"placeholder": "a21"})
	a22=DecimalField('a22',places=2,render_kw={"placeholder": "a22"})
	submit = SubmitField('Describe Matrix')

	def __repr__(self): 
		return str({'a11':self.a11.raw_data, 'a12':self.a12.raw_data,'a21':self.a21.raw_data, 'a22':self.a22.raw_data})

	def getMatrixRepresentation(self):
		return "[[{},{}],[{},{}]]".format(self.a11.raw_data[0], self.a12.raw_data[0], self.a21.raw_data[0], self.a22.raw_data[0]).replace("[","{").replace("]","}")

class M3(M2):
	
	a13=DecimalField('a13',places=2,render_kw={"placeholder": "a13"})
	a23=DecimalField('a23',places=2,render_kw={"placeholder": "a23"})

	a31=DecimalField('a31',places=2,render_kw={"placeholder": "a31"})
	a32=DecimalField('a32',places=2,render_kw={"placeholder": "a32"})
	a33=DecimalField('a33',places=2,render_kw={"placeholder": "a33"})
	
	def __repr__(self): 
		return str({'a11':self.a11.raw_data, 'a12':self.a12.raw_data,'a13':self.a13.raw_data,'a21':self.a21.raw_data, 'a22':self.a22.raw_data,'a23':self.a23.raw_data,'a31':self.a31.raw_data,'a32':self.a32.raw_data,'a33':self.a33.raw_data})

	def getMatrixRepresentation(self):
		return "[[{},{},{}],[{},{},{}],[{},{},{}]]".format(self.a11.raw_data[0], self.a12.raw_data[0], self.a13.raw_data[0], self.a21.raw_data[0], self.a22.raw_data[0], self.a23.raw_data[0],self.a31.raw_data[0],self.a32.raw_data[0],self.a33.raw_data[0]).replace("[","{").replace("]","}")

class CacheReplacementAlgo(FlaskForm):
	algos = SelectField('REPLACEMENT ALGO', choices = ['LRU','LFU','FIFO'])
	cache_size=DecimalField('cache size',places=1, render_kw={'placeholder':'cache size'})
	access_pattern = TextField(render_kw={'placeholder':'page reference pattern'})
	showResult=False
	text=''
	cache=''
	hit_count=''
	hit_ratio=''
	submit = SubmitField('Simulate')
