import falcon
from sklearn.externals import joblib
clf = joblib.load('titanic-model/titanic.pkl') 
import msgpack


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
		doc = {
			'images': [
				{
					'href': '/titanic-model/titanic.pdf'
				}
			]
		}
		resp.data = msgpack.packb(doc, use_bin_type=True)
		resp.content_type = falcon.MEDIA_MSGPACK
		resp.status = falcon.HTTP_200
			

			
			
app.add_route('/', StaticResource())
app.add_route('/predict', Titanic())
 


