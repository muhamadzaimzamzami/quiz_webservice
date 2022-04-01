from flask import Flask, jsonify, request
app = Flask(__name__)

#curl -i -X POST http://127.0.0.1:5000/api/v1/square_with_parameters_with_body_json -H 'Content-Type: application/json' -d '{"tinggi":165, "berat": 80}'
@app.route("/api/v1/quiz_bmi_calculator", methods=["POST"])
def bmi_calculator():
    t = request.json['tinggi']
    b = request.json['berat']
    bmi = float(b) / (float(t)/100)**2
    message = "BMI anda " + str(bmi)
    if bmi <= 18.5 :
        kategori = " Kurus "
    elif bmi <= 25 :
        kategori = " Normal"
    elif bmi <= 40 :
        kategori = "Berlebih"
    else :
        kategori = "Bahaya"
    data = {'message': message, 'Kategori':kategori}
    return jsonify(data), 200
  

if __name__ == '__main__':
    app.run(debug = True, port= 5000)