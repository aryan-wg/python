from flask import Flask,render_template

app = Flask(__name__)
post = {
    0:{
        "title":"first post",
        "content":"content of the first post"
    }
}

@app.route("/get/<postId>",methods = ["post","get"])
def render_html(postId):
    data = post.get(int(postId))
    print(data)
    if not data:
        return render_template('404.jinja2',post_id = postId )
    else:
        return render_template('test_template.jinja2',data = data)

if __name__ == "__main__":
    app.run()