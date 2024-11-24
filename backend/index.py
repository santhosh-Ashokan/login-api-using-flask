from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
@app.route('/register')
def homepage():
    return render_template("register.html")

@app.route("/conform",methods=['POST','GET'])
def register():
    if request.method=='POST':
        n=request.form.get('name')
        nn=request.form.get('nickname')
        a=request.form.get('age')
        c=request.form.get('count')
        s=request.form.get('salary')
        l=request.form.get('last')
        print(l)

        return render_template('conform.html',name=n,nickname=nn,age=a,count=c,salary=s,last=l)
        
if __name__=="__main__":
    app.run(debug=True)