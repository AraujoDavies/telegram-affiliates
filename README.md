# robo-telegram-affiliates


### Enviroment (You need to set):

- ABSOLUTE_SESSION_PATH = **"/home/myuser/robo-telegram-affiliates/code/sessions/"**

    async scripts have difficult in find paths, then set absolute path.

- DATABASE_URI = mysql+pymysql://{YOUR_USER}:{YOUR_PASSWORD}@{YOUR_HOST}/

    connection with your DB. 
    
    ***ALERT***: if you are using **'./code/db/init_db.py'** to create your db **DON'T SET SCHEMA** after last '/'