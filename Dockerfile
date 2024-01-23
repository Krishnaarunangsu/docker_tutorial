# Derive the latest base python image
FROM python:latest

# Labels as key-value pair
LABEL key="Narayan.18"

# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
# COPY dictionary_comprehension.py ./
# COPY test.py ./
COPY  . ./

# Now the structure looks like this '/usr/app/src/test.py'

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.zz
CMD [ "python","./test.py" ]