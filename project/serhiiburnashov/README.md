<h2 align="center">Lv-568.2.PythonCore</h1>
<h3 align="center">Фінальний проєкт :boom:</h2>

#### Веб-сторінка проєкту: [*перейти*](http://51.13.76.21/) :rocket:

Налаштовуємо хост та порт:
>```python 
>if __name__ == "__main__":
>    app.run(host="0.0.0.0", port=80, debug=False)
>```

Встановлюємо та налаштовуємо зовнішній доступ:
>```bash 
>sudo apt install authbind
> 
>sudo touch /etc/authbind/byport/80
>sudo chmod 777 /etc/authbind/byport/80
>
>authbind --deep python3 main.py
>```
