import uiautomator2 as u2
import datetime
import time

now = time.strftime("%Y-%m-%d %H:%M:%S.", time.localtime())


def logger(msg):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(current_time, msg)


def QiangYiMiao():
    logger("通过USB连接手机")
    device = u2.connect_usb()

    # logger("通过WiFi连接手机")
    # device = u2.connect('192.168.0.106')

    logger("停止微信")
    device.app_stop("com.tencent.mm")
    time.sleep(2)

    logger("启动微信")
    device.app_start("com.tencent.mm")  # 启动微信
    time.sleep(5)  # 休息3秒，等待启动

    logger("点击 发现")
    device.click(682, 2171)
    time.sleep(1)

    logger("点击 小程序")
    device(text="小程序").click()
    time.sleep(1)

    logger("点击 秒苗")
    device(text="秒苗").click()
    time.sleep(5)

    logger("点击首页")
    device.click(270.0, 2142.0)  # 点击 首页
    time.sleep(2)  # 休息1秒，等待页面反应过来

    logger("点击进入抢购页面")
    device.click(890.0, 862.0)
    time.sleep(2)  # 休息2秒，等待页面反应过来

    count = 1
    while True:
        logger(f"点击抢购第{count}次")
        device.click(470.0, 2142.0)  # 点击，抢购按钮
        count += 1


QiangYiMiao()
