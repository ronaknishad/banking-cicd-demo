from flask import Flask, jsonify

app = Flask(__name__)


def calculate_emi(principal, annual_rate, months):
    """Return the monthly EMI for a loan."""
    if principal <= 0 or months <= 0:
        raise ValueError("principal and months must be positive")
    r = annual_rate / 12 / 100
    if r == 0:
        return round(principal / months, 2)
    emi = principal * r * (1 + r) ** months / ((1 + r) ** months - 1)
    return round(emi, 2)


@app.route("/")
def home():
    return jsonify(message="Banking App API is running")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/emi/<int:principal>/<float:rate>/<int:months>")
def emi(principal, rate, months):
    return jsonify(emi=calculate_emi(principal, rate, months))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
