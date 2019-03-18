# Website van Home Vermeylen
0. Leer de basics: 
    * HTML: https://www.youtube.com/watch?v=kDyJN7qQETA
    * Bootstrap: https://getbootstrap.com/docs/4.1/getting-started/introduction/
    * Django: https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
1. clone deze repository naar je pc
2. maak virtual environment aan (virtualenvwrapper package)
    * voor windows:
        * https://pypi.org/project/virtualenvwrapper-win/
        * http://timmyreilly.azurewebsites.net/setup-a-virtualenv-for-python-3-on-windows/
    * voor apple/linux: zelf zoeken
3. install alle requirements via pip
4. py manage.py runserver

## Groepen gebruikers:
* muilgraaf
    * kan aan frontend muilgraaf via de site
    * geen staff status
* praesidium
    * muilgraaf rechten
    * staff status
    * kan alles behalve authenticatie en autorisatie zien in admin
    * kan geen activiteit toevoegen aan de google calendar
* praeses
    * praesidium rechten
    * kan activiteiten toevoegen aan google calendar
* superuser
    * superuser status aka kan alles
