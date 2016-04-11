# `avionvilleray`

Collecting statistics about planes on top of Villeray.

Using [dump1090](https://github.com/antirez/dump1090) to get data from the air.

Available online at [avionvilleray.ca](http://avionvilleray.ca)

## Technical details

Pyramid based, on top of Python 3.5, using [APScheduler](https://pypi.python.org/pypi/APScheduler/) and [Beanstalkd](https://github.com/kr/beanstalkd).

## Test

``` bash
$ python setup.py test
```

## Install

``` bash
$ pip install setup.py
```

[![Build Status](https://travis-ci.org/mlhamel/avionvilleray.svg?branch=master)](https://travis-ci.org/mlhamel/avionvilleray)
