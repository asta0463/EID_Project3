'use strict';

console.log('Loading function');
var AWS = require("aws-sdk");

exports.handler = (event, context, callback) => {
    //console.log('Received event:', JSON.stringify(event, null, 2));
    //console.log('Current temperature  =', typeof(event.Temperature)); 
    //console.log('Current Humidity =', event.Humidity);
    console.log('Count =', event.Count);
    var t=parseFloat(event.Temperature);
    //console.log('Temp type :', typeof(t));
    
    var h=parseFloat(event.Humidity);
    var count=parseFloat(event.Count);
    //console.log('count type: ', typeof(count));
    var avg_temp;
    var max_temp;
    var min_temp;
    var latest_temp;
    var one;
    var message;
    var body;
    var avg_temp1;
    var max_temp1;
    var min_temp1;
    var avgtempn;
    var avg_tempm;
    var avg_hum;
    var max_hum;
    var min_hum;
    var latest_hum;
    var avg_hum1;
    var max_hum1;
    var min_hum1;
    var avghumn;
    var avg_humm;
    var queueURL1= "https://sqs.us-east-1.amazonaws.com/499557241041/P3_QUEUE";  //intermediate Q
    var queueURL2= "https://sqs.us-east-1.amazonaws.com/499557241041/P3_2";
    var sqs1 = new AWS.SQS();  ////intermediate Q
    var sqs2 = new AWS.SQS();  //main
    if(event.Count==1){
        avg_temp=t;
        max_temp=t;
        min_temp=t;
        avg_hum=h;
        max_hum=h;
        min_hum=h;
        
    
    var myObj = { 
        "AvgT":avg_temp, 
        "MaxT":max_temp,
        "MinT":min_temp, 
        "LatestT":t,
        "AvgH":avg_hum, 
        "MaxH":max_hum,
        "MinH":min_hum, 
        "LatestH":h,
        
    };
    var msg = JSON.stringify(myObj);
    console.log("Message to send: " + msg);
    var params = {
    DelaySeconds: 0,
    MessageAttributes: {
                       "CountVal":  {
                                    DataType: "String",
                                    StringValue:event.Count 
                               },
                        },
    MessageBody: msg,
    QueueUrl: "https://sqs.us-east-1.amazonaws.com/499557241041/P3_QUEUE"  //intermediate queue
    };
    sqs1.sendMessage(params, function(err, data) {
        if (err) {
            console.log("Error sending msg to P3_Q", err);
        } else {
            console.log("Success -data sent to P3_Q",msg);
        }
    });
    var params5 = {
    DelaySeconds: 0,
    MessageAttributes: {
                        "CountVal": {
                                    DataType: "String",
                                    StringValue:event.Count 
                                },
                   
                        },
    MessageBody: msg,
    QueueUrl: "https://sqs.us-east-1.amazonaws.com/499557241041/P3_2"
    };
    sqs2.sendMessage(params5, function(err, data) {
        if (err) {
            console.log("Error sending data to P3", err);
        } else {
            console.log("Success -data sent to P3 ", msg);
        }
});

}
else if(event.Count>1){
    var params2 = {
    AttributeNames: [
    "SentTimestamp"
 ],
 MaxNumberOfMessages: 1,
 MessageAttributeNames: [
    "All"
 ],
 QueueUrl: queueURL1,
 VisibilityTimeout: 0,
 WaitTimeSeconds: 0
};

sqs1.receiveMessage(params2, function(err, data) {
  if (err) {
    console.log("Receive Error", err);
  } else {
          console.log("msg extracted",data.Messages[0]);
          message = data.Messages[0];
          body = JSON.parse(message.Body);
          console.log("msg extracted is",body);
        avg_temp1=body.AvgT;
        max_temp1=body.MaxT;
        min_temp1=body.MinT;
        avg_hum1=body.AvgH;
        max_hum1=body.MaxH;
        min_hum1=body.MinH;
        //latest_temp1=body.Latest;
        //console.log("avg type is",typeof(avg_temp1));
        console.log("ext avg",avg_temp1);
        console.log("ext max",max_temp1);
        //console.log("max is",typeof(max_temp1));
        
        avg_tempm;
        one=1;
        avg_tempm=avg_temp1*(count-one);
        
        //console.log("middle avg is",typeof(avg_tempm));
        //console.log("middle avg is",avg_tempm);

        avgtempn=avg_tempm+t;
        //console.log("middle middle",avgtempn);
        //console.log("type of",typeof(avgtempn));
        avg_temp=avgtempn/count;
        console.log("avg is",avg_temp);
        //console.log("avg type",typeof(avg_temp));
        if(t>max_temp1){
            max_temp=t;
        }else{
            max_temp=max_temp1;
        }
        if(t<min_temp1){
            min_temp=t;
        }else{
            min_temp=min_temp1;
        }
        
        
        avg_humm=avg_hum1*(count-one);
        
        //console.log("middle hum is",typeof(avg_humm));
        //console.log("middle hum is",avg_humm);
        avghumn=avg_humm+h;
        //console.log("middle middle",avghumn);
        //console.log("type of",typeof(avghumn));
        avg_hum=avghumn/count;
        console.log("avg is",avg_hum);
        //console.log("avg type",typeof(avg_hum));
        if(h>max_hum1){
            max_hum=h;
        }else{
            max_hum=max_hum1;
        }
        if(h<min_hum1){
            min_hum=h;
        }else{
            min_hum=min_hum1;
        }
        var myObj2 = { 
            "AvgT":avg_temp, 
            "MaxT":max_temp,
            "MinT":min_temp, 
            "LatestT":t,
            "AvgH":avg_hum, 
            "MaxH":max_hum,
            "MinH":min_hum, 
            "LatestH":h
        };
        
        var msg2 = JSON.stringify(myObj2);
        var params3 = {
        DelaySeconds: 0,
        MessageAttributes: {
                            "CountVal": {
                                        DataType: "String",
                                        StringValue:event.Count 
                                    },
                           },
        MessageBody: msg2,
        QueueUrl: "https://sqs.us-east-1.amazonaws.com/499557241041/P3_2"
        };
        sqs2.sendMessage(params3, function(err, data) {
            if (err) {
                console.log("Error", err);
            } else {
                console.log("Success -data send to P3 ", msg2);
            }
        });
        var params4 = {
        DelaySeconds: 0,
        MessageAttributes: {
                            "CountVal": {
                                        DataType: "String",
                                        StringValue:event.Count 
                                    },
                      
                            },
        MessageBody: msg2,
        QueueUrl: "https://sqs.us-east-1.amazonaws.com/499557241041/P3_QUEUE"
        };
        var deleteParams = {
        QueueUrl: queueURL1,
        ReceiptHandle: data.Messages[0].ReceiptHandle
        };
        sqs1.deleteMessage(deleteParams, function(err, data) {
            if (err) {
                console.log("Delete Error", err);
            } else {
                console.log("Message Deleted", data);
            }
        });
        sqs1.sendMessage(params4, function(err, data) {
            if (err) {
                console.log("Error", err);
            } else {
                console.log("Success data sent to P3_Q", msg2);
            }
        });
    }
});
}
};
