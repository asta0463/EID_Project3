AWS with Graphical Client
==================================
Repository for the thid Project of ECEN 5053-002 : Embedded Interface Design   
This project involves communication between 2 Pis that run QT GUIs using applications of the Cloud Platform, Amazon Web Services  .


Authors: Rhea Cooper and Ashish Tak

Date: 11/12/2017

Installation Instructions:
--------------------------------
1.Install all the python libraries and dependencies :
``````````````````````````````````````````````````````````` 
sudo apt-get update
sudo apt-get install build-essential python-dev python-openssl
sudo python setup.py install
`````````````````````````````````````````````````````````````             
2.Install QT4 designer on the Server and Client Pi:
```````````````````````````````````````````````````````````
sudo apt-get install qt4-designer
```````````````````````````````````````````````````````````
3.Install PyQt4 on the Server and Client Pi: 
```````````````````````````````````````````````````````````
sudo apt-get install pyqt4
```````````````````````````````````````````````````````````
4.Install MySQL database on the Server Pi: 
```````````````````````````````````````````````````````````
sudo apt-get install python-pip python-dev libmysqlclient-dev
```````````````````````````````````````````````````````````
5.The username and password for the database access is root and root. The Database is DB1. Login using :
```````````````````````````````````````````````````````````
mysql -uroot -p
```````````````````````````````````````````````````````````
6.Connect the DHT22 to GPIO4 of the Server RaspberryPi with a 4.7k or 10k resistor.
7.Install the python SDK for AWS IOT on the Server and Client Pi by running the following commands: 
```````````````````````````````````````````````````````````
pip install AWSIoTPythonSDK
python setup.py install
```````````````````````````````````````````````````````````
8.Install boto3 on the Client Pi: 
```````````````````````````````````````````````````````````
pip install boto3
```````````````````````````````````````````````````````````
9.To use Boto 3, you must first import it and tell it what service you are going to use:
```````````````````````````````````````````````````````````
import boto3
sqs = boto3.resource('sqs')
```````````````````````````````````````````````````````````
10.In the "examples" folder of the "Server" folder of the Server Pi run :
```````````````````````````````````````````````````````````
python AdafruitDHT.py 22 4
```````````````````````````````````````````````````````````
11.Login to the AWS IOT console. In the "TEST" tab, type "P3" in the Subscription topic to see the incoming temperature and humidity values.

12.Login to the AWS Lambda console and click on "View Logs" in the Monitoring Tab to view the debugging information and statistics of incoming messages.

13.Login to the AWS SQS console to view the messages in the "P3_2" Queue.

14.Login to the AWS S3 console and download the files in the "p3.bucket".

15.Login to the AWS DynamoDB and check the items in the "TempHum" table.

16.In the "Client" folder of the Client Pi run to view the graphs:
```````````````````````````````````````````````````````````
python Client.py
```````````````````````````````````````````````````````````







Project Work
---------------------------------
The sensor RPi does the following:
Takes temperature/humidity readings every 5 seconds and displays in QT the last, average, highest, and lowest readings for both temp and humidity with time/date of each reading.
The sensor RPi3 also stores temperature and humidity readings (with timestamps) in a MySQL database.
It connects to AWS when started, and sends the temperature and humidity readings to an AWS IoT Thing via MQTT every 5 seconds.


In AWS, a Node.js Lambda function receives the incoming temperature and humidity message, and creates an 8 value message with the latest value, average, maximum, and minimum of the received temperature and humidity data and drops the 8 value message on an AWS SQS Queue.

The Client RPi3 has a QT UI with a data request button-when pressed, it retrieves a maximum of 30 messages from the SQS Queue.
The display contains two graphs of the four temperature and humidity values that it extracts from the SQS messages(values, averages, maximum, minimum). 


Project Additions
---------------------------------
The AWS IOT rule triggers :
1. A Lambda Node.js function to trigger an SNS notification.A text message containing the incoming temperature and humididty values.is sent to the phone number subscribed to the topic.
2. A Lambda Node.js function to populate a DynamoDB table with the incoming temperature and humididty values.
3. An Amazon Kinesis Firehose stream that sends the incoming MQTT messages into an Amazon S3 bucket.

A block diagram of the flow is present in ExtraCredit.png 

References
-------------------------------------------------
1.https://github.com/adafruit/Adafruit_Python_DHT.git

2.https://www.tutorialspoint.com/pyqt/pyqt_basic_widgets.htm

3.https://pythonspot.com/en/pyqt4-gui-tutorial/

4.https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview

5.https://github.com/aws/aws-iot-device-sdk-python

6.http://boto3.readthedocs.io/en/latest/guide/sqs.html

7.AWS Documentation

8.For graphing : https://www.youtube.com/watch?v=Wk7CECwebMc
