from app import app,db
from app.models import User,passenger,ticket,train,train_status,cancellation,books,starts,stopsat,station


@app.shell_context_processor
def make_shell_context():
    return {'db':db,'User':User,'Passenger':passenger,'ticket':ticket,'train':train,'ticket':ticket,'train_status':train_status,'station':station,'books':books,'cancellation':cancellation,'starts':starts,'stops':stopsat}



if __name__=="__main__":
    app.run(debug=True)