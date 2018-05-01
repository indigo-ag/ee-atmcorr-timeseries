#!/usr/bin/env bash

source venv/bin/activate
pip install -r requirements.txt -U

s3pypi --bucket pypi.internal.telluslabs.com
