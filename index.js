var fs = require('fs');
var webdriverio = require('webdriverio');
var selenium = require('selenium-standalone');
var client = ""; // WebdriverIO client

function main() {
  client
    .url("https://milestonecorporate.residentportal.com/resident_portal/?module=authentication&action=view_login")
    .setValue("#email", "seanc@seancotech.com")
    .setValue("#password", "NS141faw")
    .click("#loginVerify")
    .click(".closeLightbox")
    .end();
}

function seleniumPrep() {
  selenium.install(() => {
    selenium.start(() => {
      client = webdriverio.remote();
      client.init().then(() => main());
    });
  });
}

if (require.main === module) {
    seleniumPrep();
}
