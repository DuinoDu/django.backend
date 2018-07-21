#!/bin/bash
# File              : updatemodel.sh
# Author            : duino <472365351duino@gmail.com>
# Date              : 21.07.2018
# Last Modified Date: 21.07.2018
# Last Modified By  : duino <472365351duino@gmail.com>

python manage.py makemigrations simple_app
python manage.py migrate simple_app
