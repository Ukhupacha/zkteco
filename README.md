# Zkteco webapp



`Zkteco webapp` is a webapp for the zkteco attendance machine family.

It creates an image report on the days that the selected employee has worked.

It is build on top of pyzk's fork from https://github.com/agn-7/pyzk and https://github.com/e-hulten/july beautiful plot images.

It is intended to work on an Alpine's Linux os, but it can work anywhere with the respective dependencies.




# Installation 
## Requirements
python 3.8
## Alpine linux
There is a script for Alpine on scripts/alpine.sh that will set up the dependencies and create a service.
``` bash
sh scripts/alpine.sh
```
Start the service with 
``` bash
rc-service attendance start
```
## Freebsd 
There is a script for Freebsd on scripts/freebsd.sh that will set up the dependencies and create a service.

``` bash
sh scripts/freebsd.sh
```
Start the service with 
``` bash
service supervisord start
```
## Test without service
Clone the repo and install the dependencies on requirements.txt
``` bash
pip3 install -r requirements.txx
```

You can run it on your pc and try it
```commandline
python app.py -a 127.0.0.1 -p 8000
```
You would need to change the ip address of your device in app.py 'zkteco.intranet' by default

# Docker
## Install
There is a script for docker
``` bash
./build.sh
```
This script will build zkteco:latest after that run docker-compose up -d

## Webapp shows in 127.0.0.1:8000
![alt text](./images/ui.png)

## Calendar Report of attendance
![alt text](./images/july-image.png)

## PDF Report with time punches
![alt text](./images/pdf-report.png)

# Compatible devices

```
Firmware Version : Ver 6.21 Nov 19 2008
Platform : ZEM500
DeviceName : U580

Firmware Version : Ver 6.60 Apr 9 2010
Platform : ZEM510_TFT
DeviceName : T4-C

Firmware Version : Ver 6.60 Dec 1 2010
Platform : ZEM510_TFT
DeviceName : T4-C

Firmware Version : Ver 6.60 Mar 18 2011
Platform : ZEM600_TFT
DeviceName : iClock260

Platform         : ZEM560_TFT
Firmware Version : Ver 6.60 Feb  4 2012
DeviceName       :

Firmware Version : Ver 6.60 Oct 29 2012
Platform : ZEM800_TFT
DeviceName : iFace402/ID

Firmware Version : Ver 6.60 Mar 18 2013
Platform : ZEM560
DeviceName : MA300

Firmware Version : Ver 6.60 Dec 27 2014
Platform : ZEM600_TFT
DeviceName : iFace800/ID

Firmware Version : Ver 6.60 Nov 6 2017 (remote tested with correct results)
Platform : ZMM220_TFT
DeviceName : (unknown device) (broken info but at least the important data was read)

Firmware Version : Ver 6.60 Jun 9 2017
Platform : JZ4725_TFT
DeviceName : K20 (latest checked correctly!)

Firmware Version : Ver 6.60 Aug 23 2014 
Platform : ZEM600_TFT
DeviceName : VF680 (face device only, but we read the user and attendance list!)

Firmware Version : Ver 6.70 Feb 16 2017
Platform : ZLM30_TFT
DeviceName : RSP10k1 (latest checked correctly!)

Firmware Version : Ver 6.60 Jun 16 2015
Platform : JZ4725_TFT
DeviceName : K14 (tested & verified working as expected.)

Firmware Version : Ver 6.60 Jan 13 2016
Platform         : ZMM220_TFT
DeviceName       : iFace702 (without voice function, test with encoding='gbk')
```



### Latest tested (not really confirmed)

```
Firmware Version : Ver 6.60 Jun 16 2015
Platform : JZ4725_TFT
DeviceName : iClock260

Firmware Version : Ver 6.60 Jun 5 2015
Platform : ZMM200_TFT
DeviceName : iClock3000/ID (Active testing! latest fix)

Firmware Version : Ver 6.70 Jul 12 2013
Platform : ZEM600_TFT
DeviceName : iClock880-H/ID (Active testing! latest fix)
```

### Not Working (needs more tests, more information)

```
Firmware Version : Ver 6.4.1 (build 99) (display version 2012-08-31)
Platform : 
DeviceName : iClock260 (no capture data - probably similar problem as the latest TESTED)
```

If you have another version tested and it worked, please inform me to update this list!

# Todo

* Create better documentation

