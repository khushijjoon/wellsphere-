from flask import Flask,render_template,request,jsonify # type: ignore

from chat import get_response

app=Flask(__name__)

@app.get("/")
def index_get():
    return render_template("index.html")

@app.post("/predict")
def predict():
    text=request.get_json().get("message")

    response=get_response(text)
    message={"asnwer":response}
    return jsonify(message)

if __name__=="__main__":
    app.run(debug=True)


