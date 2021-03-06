const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

let config = require('./package.json');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow(
    {
      title: config.name,
      width: 800,
      height: 600
    });

  mainWindow.loadFile('.login.html');

  mainWindow.openDevTools();

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});