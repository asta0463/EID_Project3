#!/usr/bin/python
#References: http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-tutorials.html and https://boto3.readthedocs.io/en/latest/index.html

import sys 
import time 
import datetime 
import PyQt4 
from PyQt4 import QtCore, QtGui,uic 
from P3 import Ui_MainWindow        

#Importing modules for IOT client
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import boto3
from boto3.session import Session
import logging

#importing required modules to plot graph
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

#Lists to maintain the values fetched from the SQS queue
AvgT=[]     
MaxT=[]     
MinT=[]
LatestT=[]
AvgH=[]
MaxH=[]
MinH=[]
LatestH=[]

class MyMainWindow(QtGui.QMainWindow):
    """main class that contains all the methods required for the Client side GUI""" 
 
    def __init__(self, parent=None):
        """constructor of class"""
	QtGui.QWidget.__init__(self, parent)
	self.ui = Ui_MainWindow()
	self.ui.setupUi(self)
	
	#connecting the push buttons to methods
	self.ui.request_button.clicked.connect(self.Start)  
	self.ui.Humgraph_button.clicked.connect(self.HumGraph)
	self.ui.Tempgraph_button.clicked.connect(self.TempGraph)
	self.ui.figure=plt.figure(figsize=(15,5))
	self.ui.canvas=FigureCanvas(self.ui.figure)
	self.ui.gridLayout.addWidget(self.ui.canvas,1,0,1,2)
       
        
    def TempGraph(self):
        """graph plotting Referenced from a youtube video :https://www.youtube.com/watch?v=Wk7CECwebMc"""
 	plt.cla()
	ax=self.ui.figure.add_subplot(111)
	x1=[i for i in range(len(AvgT))]  #value count on x axis
	x2=[i for i in range(len(MaxT))]
	x3=[i for i in range(len(MinT))]
	x4=[i for i in range(len(LatestT))]
	y1=AvgT     #temperature list values on y axis
	y2=MaxT
        y3=MinT
        y4=LatestT
	ax.plot(x1,y1,'b.-')
	ax.plot(x2,y2,'r.-')
	ax.plot(x3,y3,'y.-')
	ax.plot(x4,y4,'g.-')
	ax.set_title('Temperature')
	self.ui.canvas.draw()

    def HumGraph(self):
        """graph plotting Referenced from a youtube video :https://www.youtube.com/watch?v=Wk7CECwebMc"""
        plt.cla()
        ax=self.ui.figure.add_subplot(111)
        x1=[i for i in range(len(AvgH))]  #value count on x axis
	x2=[i for i in range(len(MaxH))]
	x3=[i for i in range(len(MinH))]
	x4=[i for i in range(len(LatestH))]
        y1=AvgH     #humidity list values on y axis
	y2=MaxH
        y3=MinH
        y4=LatestH
	ax.plot(x1,y1,'b.-')
	ax.plot(x2,y2,'r.-')
	ax.plot(x3,y3,'y.-')
	ax.plot(x4,y4,'g.-')				
        ax.set_title('Humidity')
        self.ui.canvas.draw()
    	
    def Start(self):
        """this method gets the messages from the SQS queue and populates a list that pops up"""
	listWidget=QtGui.QListWidget()
	listWidget.setWindowTitle("List of Values")
	
        #Set up the Host URL and Certificates/Keys
        host = "a1ah5fy1h4v4k9.iot.us-east-1.amazonaws.com"
        rootCAPath = "/home/pi/Desktop/EID_Project3/EID_Project3/Certificates/VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem"
        certificatePath = "/home/pi/Desktop/EID_Project3/EID_Project3/Certificates/57ca76974a-certificate.pem.crt"
        privateKeyPath = "/home/pi/Desktop/EID_Project3/EID_Project3/Certificates/57ca76974a-private.pem.key"
        clientId = 'iotconsole-1510025171163-0'
        topic = 'P3'

        # Configure logging
        logger = logging.getLogger("AWSIoTPythonSDK.core")
        logger.setLevel(logging.DEBUG)
        streamHandler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        streamHandler.setFormatter(formatter)
        logger.addHandler(streamHandler)

        # Initialize AWSIoTMQTTClient
        myAWSIoTMQTTClient = None
        myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
        myAWSIoTMQTTClient.configureEndpoint(host,8883)
        myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

        # AWSIoTMQTTClient connection configuration
        myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
        myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
        myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
        myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

        # Create the Boto3 Session
        session = Session(
            aws_access_key_id='AKIAIBMHYZLYB4EEOWUQ',
            aws_secret_access_key='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',
            region_name='us-east-1',
        )
        client = session.client('sqs')

        # Get the Queue URL
        response = client.get_queue_url(
            QueueName='P3_2'
        )
        url = response['QueueUrl']

        count=0
        #Fetch the messages one by one 
        while count<30:
            messages = client.receive_message(
                QueueUrl='https://sqs.us-east-1.amazonaws.com/499557241041/P3_2',
                AttributeNames=['All'],
                MaxNumberOfMessages=1,
                VisibilityTimeout=60,
                WaitTimeSeconds=5
                )
            try:
                m = messages['Messages'][0]
                body= m['Body']
                count=count+1   #Increment the count if successful in fetching the message body
                att= m['Attributes']
                timestamp=datetime.datetime.fromtimestamp(float(att['SentTimestamp'])/1000).strftime('%Y-%m-%d %H:%M:%S')
                #Fetch the timestamp for the first and last fetched message respectively
                if count==1:
                    start='Start Timestamp: '+timestamp
                elif count==30:
                    end='End Timestamp: '+timestamp
                    self.ui.text_window.setText(start+'\n'+end)
                #Load the message body in JSON format for parsing 
                d=json.loads(body)
                #Append each parsed value in the message body into the appropriate lists
                AvgT.append(d['AvgT'])
                MinT.append(d['MinT'])
                MaxT.append(d['MaxT'])
                LatestT.append(d['LatestT'])
                AvgH.append(d['AvgH'])
                MinH.append(d['MinH'])
                MaxH.append(d['MaxH'])
                LatestH.append(d['LatestH'])
                #Display the list on the Client Side widget
                item=QtGui.QListWidgetItem("AvgT: %f , MinT: %f , MaxT: %f , LatestT: %f , AvgH: %f , MinH: %f , MaxH: %f , LatestH: %f, Timestamp: %s" % (d['AvgT'], d['MinT'], d['MaxT'], d['LatestT'], d['AvgH'], d['MinH'], d['MaxH'], d['LatestH'], timestamp))
                listWidget.addItem(item)
            except KeyError :
                #This exception is caught if there is an error in fetching any of the values from the SQS message, or if there's an error in fetching the message body itself
                if count==0:
                    self.ui.text_window.setText('Sorry, no messages in the SQS queue')
                else:
                    #Display the end timestamp and indicate how many values were successfully fetched from the queue (since <30 in this case)
                    end='End Timestamp: '+timestamp
                    self.ui.text_window.setText(start+'\n'+end+ '\nOnly '+str(count)+'values in the SQS queue')
                break

	listWidget.show()
	listWidget.exec_()

#instantiating the above class
app=QtGui.QApplication(sys.argv)
myapp=MyMainWindow()
myapp.show()
sys.exit(app.exec_())
