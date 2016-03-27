var fs = require('fs');
var webdriverio = require('webdriverio');
var selenium = require('selenium-standalone');

function Taskrunner(taskFile) {
  this.taskFile = taskFile;
  this.client = null;
  this.isReady = false;
}

Taskrunner.prototype = Object.create(Object.prototype);
Taskrunner.constructor = Taskrunner;

Taskrunner.prototype.setup = function(cb) {
  if (this.isReady) return;
  console.log("Selenium is initing...");
  selenium.install({"drivers": "chrome", "logger": (message) => {console.log(message)}}, () => {
    selenium.start({"drivers": "chrome", "logger": (message) => {console.log(message)}}, () => {
      var options = {desiredCapabilities: { browserName: 'chrome' }};
      this.client = webdriverio.remote(options);
      this.isReady = true;
      console.log("Selenium is inited and ready to go!");
      cb.call();
    });
  });
};

Taskrunner.prototype.teardown = function() {
    // TODO: Nothing to teardown yet
};

Taskrunner.prototype.evalData = function(data) {
  eval(data);
};

Taskrunner.prototype.run = function() {
  if (this.taskFile == null) return false;
  var data = "";
  try {
    data = fs.readFileSync(this.taskFile, 'utf8');
  } catch (err) {
    console.error("Error reading provided task file.");
  }

  // Run task
  this.setup(() => {this.evalData(data);});
  this.teardown();

  // TODO
  //var task = new Promise(this.setup, this.setupError)
  //  .then(() => this.evalData(data), this.runtimeError)
  //  .then(this.teardown, this.teardownError);
};

Taskrunner.prototype.setupError = function() {
  console.error("There was an error initing Selenium/WebdriverIO.");
};
  
Taskrunner.prototype.runtimeError = function() {
  console.log("There was an error while running the specified task.");
};

Taskrunner.prototype.teardownError = function() {
  console.error("There was an error completing the task.");
};

module.exports = Taskrunner;
