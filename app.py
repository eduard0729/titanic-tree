import falcon
from sklearn.externals import joblib
clf = joblib.load('titanic-model/titanic.pkl') 
import msgpack
import json

app = falcon.API()

class StaticResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('index.html', 'r') as f:
            resp.body = f.read()
            
            
class Titanic(object):
	from sklearn.externals import joblib
	clf = joblib.load('titanic-model/titanic.pkl') 
	def on_get(self, req, resp):
		resp.status = falcon.HTTP_200
		resp.content_type = 'text/html'
		with open('predict.html', 'r') as f:
			resp.body = f.read()

			

			
			
app.add_route('/', StaticResource())
app.add_route('/predict', Titanic())
 


