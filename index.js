'require strict';

var Taskrunner = require('./taskrunner_base');

var fs = require('fs');
var webdriverio = require('webdriverio');
var selenium = require('selenium-standalone');
var client = ""; // WebdriverIO client

function main() {
  // DEBUG
  var runner = new Taskrunner("tasks/check_if_apt_payment_due.task");
  runner.run();
}

if (require.main === module) {
  main();
}
