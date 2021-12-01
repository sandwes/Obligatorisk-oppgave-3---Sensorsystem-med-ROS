// GetRawFototransistorValues.js publiserer og abonnerer av pulse.csv

const amountOfMeasurements = 10;

const timeout = 500; //tid mellom hver måling
const b = require('bonescript');
const inputPin = "P9_40";

var values = [];
var count = 0;

var fs = require('fs');

function main() {
    measure();
}

function measure() {
    values[count++] = b.analogRead(inputPin);

    if (count > amountOfMeasurements)
        writeToFile(values);
    else
        setTimeout(measure, timeout);
}

//Skriver til .csv fil
function writeToFile(values) {
    var text = "";

    for (let i = 0; i < values.length; i++) {
        text += i + "," + values[i] + "\n";
    }
    console.log(text);
    fs.writeFile('./values.csv', text, 'utf8', function (err) {
        if (err) {
            console.log('En feil oppstod, fil enten lagret eller korrupt fil er lagret.');
        }else{
            console.log('Fullført!');
        }
    });
}

main();