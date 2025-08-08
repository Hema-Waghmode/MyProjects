from flask import Flask,render_template,request,redirect
import pymysql

app=Flask('__name__') # s1=student()

@app.route('/')
def index():
    try:
          db=pymysql.connect(host="localhost",user="root",
                     password="root",database="todo912")

          cu=db.cursor()
          q="select * from task where is_deleted='N'"
          cu.execute(q)
          data=cu.fetchall()
          return render_template('dashboard.html',d=data)
        
    except Exception as e:
        print("Error:",e)
    

@app.route('/contact')
def contact():

    return "Hello From Contact.."

@app.route('/create')
def create():

    return render_template('form.html')


@app.route('/store',methods=['POST'])
def store():

    title=request.form['t']
    detail=request.form['det']
    date=request.form['dt']
    
    try:
        db=pymysql.connect(host="localhost",user="root",
                         password="root",database="todo912")
        
        cu=db.cursor()
        q="insert into task(title,detail,date,is_deleted) values('{}','{}','{}','N')".format(title,detail,date)
        cu.execute(q)
        db.commit()
        return redirect('/')
        
    except Exception as e:
        print("Error:",e)
        return "An error occurred: {}".format(e), 500

@app.route('/delete/<rid>')

def delete(rid):
    try:
        db=pymysql.connect(host="localhost",user="root",
                             password="root",database="todo912")
        
        cu=db.cursor()

        #HardDelete
        #q="delete from task where id='{}'".format(rid)
        #Soft Delete
        q="update task set is_deleted='y' where id='{}'".format(rid)
        cu.execute(q)
        db.commit()
        return redirect('/')

    except Exception as e:
        print("Error:",e)

@app.route('/edit/<rid>')

def edit(rid):
        try:
            db=pymysql.connect(host="localhost",user="root",
                             password="root",database="todo912")
            
            cu=db.cursor()
            q="select * from task where id='{}'".format(rid)
            cu.execute(q)
            data=cu.fetchone()
            return render_template('editform.html',d=data)
           
        except Exception as e:
            print("Error, failed to connect:",e)

@app.route('/update/<rid>',methods=['POST'])

def update(rid):

        ut=request.form['t']
        ud=request.form['det']
        udt=request.form['dt']
        try:
            db=pymysql.connect(host="localhost",user="root",
                             password="root",database="todo912")
            
            cu=db.cursor()
        
            q="update task SET title='{}',detail='{}',date='{}' where id='{}'".format(ut,ud,udt,rid)
            cu.execute(q)
            db.commit()
            return redirect('/')

        except Exception as e:
            print("Error:",e)

                        
    
#run server
app.run(debug=True) #app=> object and run()=>method of flask class
