const os = require('os');

class Util {

    static getOs() {
        // Get the OS platform (e.g., 'darwin', 'win32', 'linux')
        return os.platform();
    }
}

module.exports = Util;