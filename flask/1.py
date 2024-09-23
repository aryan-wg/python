import flask

app = flask.Flask(__name__)
posts = {
    0:{
        "title":"first post",
        "content":"content of the first post"
    }
}

@app.route("/")
def home():
    return "this is the home route"

@app.route("/getData/<postId>")
def data(postId):
    # print(type(postId))
    return posts[int(postId)]

@app.route("/postReq",methods=["POST"])
def testingMethods():
   params = flask.request.get_json()
   # https: // stackoverflow.com / questions / 10434599 / get - the - data - received - in -a - flask - request
   print(params)
   return "got a post request"
if __name__ == "__main__":
    app.run()

