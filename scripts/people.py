# go to terminal and type install pipenv
# then, pipenv shell
# change directory to script
# type python [FILENAME]

import requests
r = requests.get("http://jesuitplantationproject.org/api/items?=&item_set_id=11")


with open('enslaved.txt','w') as fd:
    fd.write(r.text)

