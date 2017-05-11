# steelkiwi test

1. Download repo
> wget https://github.com/dimdiden/steelkiwi/archive/master.zip

2. Uzip it and delete
> unzip master.zip && rm -f master.zip

3. Create virtualenv
> virtualenv venv

4. Activate it
> . venv/bin/activate

5. Change folder and install requirements
> cd steelkiwi-master/ && pip install -r requirements.txt

6. Create mysql database
> CREATE DATABASE steelkiwi CHARACTER SET utf8;

> CREATE USER '<your user>'@'localhost' IDENTIFIED BY '<your password>';

> GRANT ALL ON steelkiwi.* TO '<your user>'@'localhost';

> flush privileges;

7. Change user in settings file
> sed -i s/ded/<your user>/g steelkiwi/settings/local.py

8. Perform migrations
> ./manage.py migrate

9. Load prepared data into database
> ./manage.py loaddata product_fixtures.json

10. Run
> ./manage.py runserver
