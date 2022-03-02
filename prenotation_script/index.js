import 'https://gosafety.web.app/APP/lib/device-uuid.js'

var uuid = new DeviceUUID().get();
var du = new DeviceUUID().parse();
var dua = [
    du.language,
    du.platform,
    du.os,
    du.cpuCores,
    du.isAuthoritative,
    du.silkAccelerated,
    du.isKindleFire,
    du.isDesktop,
    du.isMobile,
    du.isTablet,
    du.isWindows,
    du.isLinux,
    du.isLinux64,
    du.isMac,
    du.isiPad,
    du.isiPhone,
    du.isiPod,
    du.isSmartTV,
    du.pixelDepth,
    du.isTouchScreen
];
var uuid2 = du.hashMD5(dua.join(':'));
document.querySelector('#token').textContent = uuid + uuid2

let a = 'ciao'

export default a