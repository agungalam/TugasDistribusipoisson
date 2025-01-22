from flask import Flask, render_template, request
import math

app = Flask(__name__)

def poisson_probability(lmbda, k):
    """
    Menghitung peluang distribusi Poisson.
    
    Args:
        lmbda (float): Rata-rata kedatangan (λ).
        k (int): Jumlah kedatangan (k).
    
    Returns:
        tuple: (probabilitas, komponen perhitungan) berupa peluang dan detail rumus.
    """
    # Komponen perhitungan
    numerator = math.pow(lmbda, k) * math.exp(-lmbda)
    denominator = math.factorial(k)
    probability = numerator / denominator

    # Detail perhitungan
    details = f"P(k; λ) = (λ^k * e^(-λ)) / k!\n" \
              f"P({k}; {lmbda}) = ({lmbda}^{k} * e^(-{lmbda})) / {k}!\n" \
              f"P({k}; {lmbda}) = ({numerator:.4f}) / {denominator}\n" \
              f"P({k}; {lmbda}) = {probability:.4f}"
    
    return probability, details

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    formula = None
    if request.method == 'POST':
        try:
            lmbda = float(request.form['lambda'])
            k = int(request.form['kValue'])

            if lmbda <= 0 or k < 0:
                result = "λ harus lebih besar dari 0 dan k tidak boleh negatif!"
            else:
                probability, details = poisson_probability(lmbda, k)
                result = f"Peluang {k} kedatangan saat λ={lmbda} adalah {probability:.4f}"
                formula = details
        except ValueError:
            result = "Harap masukkan nilai angka yang valid!"

    return render_template('index.html', result=result, formula=formula)

if __name__ == '__main__':
    app.run(debug=True)
