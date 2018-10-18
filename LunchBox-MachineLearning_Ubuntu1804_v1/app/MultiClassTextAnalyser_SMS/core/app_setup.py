from ..main import app
from ..api import api


@app.route("/")
@app.route("/index")
def hello():
    # This could also be returning an index.html
    return '''You can validate any SMS. Try <a href="/SMS/?SMS=Thia is not a spam">/SMS/?SMS=Thia is not a spam</a>'''
     

    
