import uiautomator2 as u2
import time

now = time.strftime("%Y%m%d %H:%M:%S.", time.localtime())


def QiangYiMiao():
    print(f"{now} 通过USB连接手机")
    device = u2.connect_usb()

    print("停止微信")
    device.app_stop("com.tencent.mm")
    time.sleep(2)

    print("启动微信")
    device.app_start("com.tencent.mm")  # 启动微信
    time.sleep(2)  # 休眠两秒,给手机缓冲时间

    screen_text_list = ["发现", "小程序", "秒苗"]
    for t in screen_text_list:
        print(f"点击 {t} ")
        device(text=t).click()

    print("点击首页")
    device.click(270.0, 2142.0)  # 点击 首页

    print("点击进入抢购页面")
    device.click(890.0, 862.0)
    time.sleep(2)  # 休息2秒，等待页面反应过来

    count = 1
    while True:
        print(f"点击抢购第{count}次")
        device.click(470.0, 2142.0)  # 点击，抢购按钮
        count += 1


QiangYiMiao()
