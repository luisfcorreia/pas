import web
import config

stuff = []

def	readfile():
	
	data = ""
	f = open('list.txt', 'r')
	# read stuff from file
	while True:
		d1 = f.readline().strip()
		d2 = f.readline().strip()
		d3 = f.readline().strip()
		
		# idiotic EOF test
		if not d3:
			break
			
		stuff.append((d1, d2, d3))
		

t_globals = dict(
  datestr=web.datestr,
)
render = web.template.render('templates/', cache=config.cache, globals=t_globals)
render._keywords['globals']['render'] = render
readfile()


		
def listing():

	return render.listing(stuff)
