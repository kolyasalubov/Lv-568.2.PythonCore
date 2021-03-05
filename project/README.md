http://51.13.76.21/

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
    
sudo apt install authbind
 
sudo touch /etc/authbind/byport/80
sudo chmod 777 /etc/authbind/byport/80

authbind --deep python3 main.py
