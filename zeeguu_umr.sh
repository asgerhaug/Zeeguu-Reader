#!/usr/bin/env bash
# Run this script to host on your machine.

VIRTUALENV_ROOT=${VIRTUALENV_ROOT:-"${HOME}/.virtualenvs/zeeguu_umr"}
# Expects that you already setup your environment, so we check.
if [ ! -d ${VIRTUALENV_ROOT} ]; then
   echo "Could not find virtual environment, plese run dev_setup.sh first." 1>&2
   exit 1
fi

source ${VIRTUALENV_ROOT}/bin/activate
export FLASK_APP=zeeguu_umr.py
# in debug mode there's no need to restart if one changes files
export FLASK_DEBUG=1
flask run --host=0.0.0.0 --port=8800
