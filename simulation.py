import time
from time import sleep
def lru(access_pattern,max_cache_size=1):
	stepsStr=""
	hits=0
	cache={}
	cache_size=0
	for page in access_pattern:
		if cache_size == max_cache_size and page not in cache:
			cache ={k:v for k,v in  sorted(cache.items(),key=lambda x: x[0],reverse=True) }
			page_to_remove=list(cache.keys())[0]
			stepsStr+='Removing page {} from cache '.format(page_to_remove)
			old_time =cache[page_to_remove]
			del cache[page_to_remove]
			stepsStr+='Adding page {} to cache\n'.format(page)
			cache[page]=int(round(time.time()*1000))
		else:
			if page not in cache:
				cache_size +=1	
				stepsStr+='Adding {} to cache\n'.format(page)
			else:
				hits+=1
				stepsStr+='Updating time for {}\n'.format(page)
			cache[page]=int(round(time.time() * 1000))
		sleep(0.1)
	return stepsStr,cache,hits,(hits/(len(access_pattern)*1.0))

def fifo(access_pattern, max_cache_size=1):
	stepsStr=""
	hits=0
	cache=[] #using queue
	cache_size=0
	for page in access_pattern:
		if cache_size == max_cache_size and page not in cache:
			stepsStr+='Removing page {} from cache '.format(cache.pop(0))
			cache.append(page)
			stepsStr+='Adding page {} to cache\n'.format(page)
		else:
			if page not in cache:
				stepsStr+='Adding page {} to cache\n'.format(page)
				cache.append(page)
				cache_size +=1
			else:
				stepsStr+='Page {} already in cache\n'.format(page)
				hits+=1
		sleep(0.1)
	return stepsStr,cache,hits,(hits/(len(access_pattern)*1.0))

def lfu(access_pattern, max_cache_size =1):
	stepsStr=""
	hits=0
	cache={}
	cache_size=0
	for page in access_pattern:
		if cache_size == max_cache_size and page not in cache:
			cache ={k:v for k,v in  sorted(cache.items(),key=lambda x: x[0],reverse=True) }
			page_to_remove=list(cache.keys())[0]
			stepsStr+='Removing page {} from cache Count = {}'.format(page_to_remove,cache[page_to_remove])
			old_time =cache[page_to_remove]
			del cache[page_to_remove]
			stepsStr+='Adding page {} to cache Count = {}\n'.format(page,1)
			cache[page]=1
			cache_size = cache_size+1
		else:
			if page not in cache:
				cache[page]=1
				stepsStr+='Adding page {} to cache Count = {}\n'.format(page,1)
				cache_size = cache_size+1
			else:
				hits+=1
				cache[page]=cache[page]+1
				stepsStr+='Updating count for {} Count = {}\n'.format(page,cache[page])
		sleep(0.1)
	return stepsStr,cache,hits,(hits/(len(access_pattern)*1.0))
			
