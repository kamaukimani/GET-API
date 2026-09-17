from app import create_app 

app=create_app()

@app.route('/')
def index():
    return "Index for Bakery/BakedGood API"

if __name__=="__main__":
    app.run(port=5555,debug=True)