<img src="./static/app/base/Logo.png" width="40%">

# Cardiocare
Spreading awareness about heart diseases

## Getting started

### Built With
* Django
* Bootstrap
* Jquery

### Installation
Its recommended to use `python3.8` or above and virtual environment `virtualenv>=20.0.29`.

Download or clone this repository

```bash
git clone https://github.com/AsadNizami/Cardiocare.git
cd Cardiocare
``` 
Create a virtual environment to install the required dependencies it it
```bash
virtualenv venv
venv\Scripts\activate
```
Note: `venv` should prompt in front the terminal, indicating that the session operates in a virtual environment.

Then install the dependencies
```bash
pip install -r requirements.txt
```

Start the django server
```bash
python manage.py runserver
```
Navigate to `http://127.0.0.1:8000` in your browser.

## General Info


## Get Involved!
We're happy to receive bug reports, fixes or any other enhancements.
Fork this repository and send a pull request. :smile:

## References
* https://docs.djangoproject.com/en/3.2/topics/http/views/
* https://docs.djangoproject.com/en/3.2/ref/contrib/admin/
* https://docs.djangoproject.com/en/3.2/topics/db/models/
* https://www.kaggle.com/tentotheminus9/what-causes-heart-disease-explaining-the-model
