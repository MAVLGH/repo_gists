#!/bin/bash

sudo apt-get install \
git \
gcc \
make \
openssl \
libssl-dev \
libbz2-dev \
libreadline-dev \
libsqlite3-dev \
zlib1g-dev \
libncursesw5-dev \
libgdbm-dev \
libc6-dev \
zlib1g-dev \
libsqlite3-dev \
tk-dev \
libssl-dev \
openssl \
libffi-dev \
liblzma-dev
curl https://pyenv.run | bash
echo 'export PATH="/home/$(whoami)/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc
