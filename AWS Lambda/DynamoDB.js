'use strict';

console.log('Loading function');
var AWS = require("aws-sdk");


// Create the DynamoDB service object
var ddb = new AWS.DynamoDB({apiVersion: '2012-10-08'});


exports.handler = (event, context, callback) => {
    console.log('Received event:', JSON.stringify(event, null, 2));
    console.log('Current temperature  =', typeof(event.Temperature)); 
    console.log('Current Humidity =', event.Humidity);
    console.log('Count =', event.Count);
    var t=parseFloat(event.Temperature);
    //console.log('Temp type :', typeof(t));
    var h=parseFloat(event.Humidity);
    var count=parseFloat(event.Count);

    ddb.listTables(function(err, data) {
      console.log(JSON.stringify(data, null, '  '));
    });
var paramsdb = {
  TableName: 'TempHum',
  Item: {
    'COUNT' : {S:event.Count},
    'TEMPERATURE': {S: event.Temperature},
    'HUMIDITY' : {S: event.Humidity}
  }
};


ddb.putItem(paramsdb, function(err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success-added", data);
  }
});
};