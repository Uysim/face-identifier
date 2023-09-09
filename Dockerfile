FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y git python-opencv 

# install build tools
RUN python -m pip install --upgrade build
RUN pip install wheel twine


RUN mkdir /face_identifier

WORKDIR /face_identifier

COPY setup.py /face_identifier
RUN --mount=type=cache,target=/root/.cache/pip pip install .
RUN pip install git+https://github.com/rcmalli/keras-vggface.git@bee35376e76e35d00aeec503f2f242611a97b38a

COPY . /face_identifier

