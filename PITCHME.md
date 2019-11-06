# Heroku
---
## Instalējam nepieciešamos resursus
@ul
- visual studio code
- git
- python
- pip
- heroku
+++
### Instalējam visual studio code
+++
### Instalējam git
+++
### Instalējam heroku
@ul
- https://devcenter.heroku.com/articles/heroku-cli
- https://cli-assets.heroku.com/heroku-x64.exe
- https://cli-assets.heroku.com/heroku-x86.exe
- heroku login
+++
### Instalējam python
	python -V
	https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe
	https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe
	Disable MAX_PATH
	This PC > Advanced System Settings > Advanced Tab > Environment Variables > Path > Edit > 
	Add to global variables
		C:\Users\Janis\AppData\Local\Programs\Python\Python38
		C:\Users\Janis\AppData\Local\Programs\Python\Python38\System
+++
### Instalējam pip
```powershell
    pip -V
    open power shell amd execute commands
    Invoke-WebRequest -OutFile get-pip.py https://bootstrap.pypa.io/get-pip.py
    python get-pip.py
    rm get-pip.py
    pip -V
```
+++
### Instalējam nepieciešamās bibleotēkas
```powershell
    pip install flask gunicorn
```
+++
### Izveidojam jaunu git repozitoriju
```powershell
    cd JŪSU_JAUNĀ_MAPE_HEROKU_PROJEKTAM
    git init
```
+++
### Izveidojam nepieciešamās datnes
@ul
- Procfile
- Procfile.windows
- requirements.txt
- runtime.txt
- server.py
- .gitignore
+++
### Saglabājam progresu
```powershell
    git commit
```
---
## Rediģējam datnes
@ul
- requirements.txt
- runtime.txt
- server.py
+++
### requirements.txt
#### Datnes nozīme un vajadzība
Te būs teksts
#### Kā pārbaudīt doto pakešu aprakstu
    ```powershell
        pip freeze
    ```
### Datnes saturs
+++?code=requirements.txt
+++

### runtime.txt
#### Datnes nozīme un vajadzība
#### Kā pārbaudīt doto python versiju
```powershell
    python -V
```
### Datnes saturs
+++?code=runtime.txt
+++

### server.py
#### Datnes nozīme un vajadzība
#### Datnes saturs
+++?code=server.pyp
+++
### Pārbaudām ka viss strādā :)
```powershell
    python ./server.py
```
+++
### Saglabājam progresu
```powershell
    git commit
```
---
## Pievienojam attālinātā servera konfigurāciju
@ul
- Procfile
- Procfile.windows
- server.py
+++
### Procfile
#### Datnes nozīme un vajadzība
#### Datnes saturs
+++?code=Procfile
+++
### Procfile.windows
#### Datnes nozīme un vajadzība
#### Datnes saturs
+++?code=Procfile.windows
### Pārbaudām ka viss strādā :)
```
    heroku local -f ./Procfile.windows
```
+++
### Saglabājam progresu
```powershell
    git commit
```
+++
### Aizsūtam uz serveru
	