## Setup

Assuming you've got virtualenv setup. (If not, [get it](https://virtualenv.pypa.io/en/stable/)).

- Install virtualenvwrapper (just makes life easier)
```sh
$ pip install virtualenvwrapper
```

- Create a virtualenv
```sh
$ mkvirtualenv euler
```

- Install requirements.txt:

```sh
$ pip install -r requirements.txt
```

- Run the server:
```sh
$ python server.py
```

- Visit the app (should be running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/))