@"
# Docker + Ansible + CI/CD ile Otomatik Web Uygulaması Dağıtımı

Bu projede basit bir Flask web uygulaması Docker container haline getirilir.
GitHub Actions ile Docker image build edilir ve Docker Hub'a push edilir.
Ardından Ansible kullanılarak sunucuya otomatik deploy edilir.

## Kullanılan Teknolojiler

- Python Flask
- Docker
- Docker Hub
- Ansible
- GitHub Actions
- Linux Server

## Mimari

Developer -> GitHub -> GitHub Actions -> Docker Hub -> Ansible -> Server -> Container

## Çalıştırma

Lokal test için:

```bash
docker build -t myapp .
docker run -d -p 5000:5000 --name myapp myapp

Test Endpoints:

http://localhost:5000
http://localhost:5000/health
http://localhost:5000/version
http://localhost:5000/api/info