from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = "v2.0.0"


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>CI/CD Deploy Projesi</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: #f4f6f8;
                    padding: 40px;
                }
                .card {
                    background: white;
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                    max-width: 700px;
                    margin: auto;
                }
                h1 { color: #1f2937; }
                p { font-size: 18px; color: #374151; }
                code {
                    background: #e5e7eb;
                    padding: 4px 8px;
                    border-radius: 6px;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Docker + Ansible + CI/CD Deploy Başarılı</h1>
                <p>Bu uygulama Flask ile geliştirilmiştir.</p>
                <p>Docker container içinde çalışmaktadır.</p>
                <p>CI/CD pipeline ile otomatik build ve deploy sürecine uygundur.</p>
                <p>Versiyon: <code>v2.0.0</code></p>
            </div>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "flask-web-app",
        "version": APP_VERSION
    })


@app.route("/version")
def version():
    return jsonify({
        "version": APP_VERSION,
        "environment": "docker"
    })


@app.route("/api/info")
def info():
    return jsonify({
        "project": "Docker + Ansible + CI/CD ile Otomatik Web Uygulaması Dağıtımı",
        "technologies": [
            "Python",
            "Flask",
            "Docker",
            "Docker Compose",
            "Nginx",
            "GitHub Actions",
            "Ansible"
        ],
        "architecture": "Developer -> GitHub -> CI/CD -> Docker Image -> Ansible -> Server -> Container"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)