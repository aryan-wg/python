import flask

app = flask.Flask(__name__)

posts={
    0 : {
        'title':'Hello, World',
        'content': 'This is my first blog'
    }
}
 
@app.route('/')
def home():
    return "HEllO"
 
@app.route('/post/<int:post_id>')
def post(post_id):
    # post= posts.get(post_id)
    return render_template('post.html',data=posts[0])
    # return render_template('post.jinja2', post=posts.get(post_id))
 
if __name__ =='__main__':
    app.run(debug=True)
 
