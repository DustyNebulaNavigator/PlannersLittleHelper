# Install postgresql
sudo apt-get update
sudo apt-get install postgresql libpq-dev
sudo service postgresql start
sudo -u postgres createdb ´´´mydb´´´
sudo -u postgres createuser -P myuser
sudo -u postgres psql
grant all privileges on database mydb to myuser;
\q

# Phase 1 - Cycle time monitoring
- .env sisaldab süsteemi seadistusi (ip, kasutajanimed, paroolid)
- machines.py sisaldab masinate nimesid, mac aadresse ning ADAM andurite pinnide seadistust.
- 

###
- Programmi käivitamisel luuakse ühendus andmebaasida.
- Iga macines.py failis oleva masina kohta luuakse andmebaasi oma tabel (kui seda veel ei olnud).
- Andmebaasist küsitakse iga masina viimane caunteri väärtus. Juhul kui ühtegi kannet tabelis ei ole, siis arvestatakse antud masina counteri väärtuseks null.


