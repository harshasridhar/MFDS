import wolframalpha
import sys
# filename=sys.argv[1] 
app_id = 'A7LWEH-HX7J3U42QY'
client = wolframalpha.Client(app_id)
#res = client.query('solve y+z=-2, 4y+6z=-12, x+y+z=2')
#print(res['pod'][1]['subpod']['plaintext'])

#from parseInput import parseInputAsMatrix
def describeMatrix(matrix):
	links={}
	query=''+matrix
	print('Question is:'+query)
	res = client.query(query)
	#print(res)
	#print(res['pod'][1]['subpod']['plaintext'])
	pods=res['pod']
	for pod in pods:
		#print(pod['@title'],end=' '))
		if 'subpod' in pod:
		# print('{}',type(pod['subpod']))
			if type(pod['subpod']) is list:
				links[pod['@title']]=[]
				for subpod in pod['subpod']:
				# print('subpod is {}'.format(subpod))
				#print(subpod['plaintext'])
					links[pod['@title']].append(subpod['img']['@src'])
		else:
		#print('{}'.format(pod['subpod']['plaintext']))
			links[pod['@title']]=pod['img']['@src']
	return links

print(describeMatrix('{{1,0,0},{0,1,0},{0,0,1}}'))
