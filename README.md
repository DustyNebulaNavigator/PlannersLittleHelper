# Helper program for production

This program currently displays cycle time for machines.

This project currently consists of 3 programs.
- getting_data
- backend
- frontend

## Prerequisites

- Python: 3.11.4
- Node: 18.17.1

### Clone Git reposiroty
```
mkdir ~/Documents/src
git clone git@github.com:DustyNebulaNavigator/PlannersLittleHelper.git ~/Documents/src
```

### Install python dependencies
```
source ~/Documents/src/.venv/bin/activate
pip install -r ~/Documents/src/.requirements.txt
```

### Install node dependencies
```
cd ~/Documents/src/frontend
npm install 
```

### Run Getting data app
```
source ~/Documents/src/.venv/bin/activate
python ~/Documents/src/getting_data/app.py
```

### Run Backend
```
source ~/Documents/src/.venv/bin/activate
python ~/Documents/src/backend/manage.py runserver 192.168.90.139:8001
```

### Run Frontend
```
cd ~/Documents/src/frontend
npm install 
npm run dev 
```