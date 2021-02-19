# Appium_code

## 十五、简单封装方法

### 原自动化代码：
```python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestContactAddMember:
    def setup(self):
        caps = {"platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": "com.tencent.wework.launch.WwMainActivity",
                "noReset": "true",
                "skipDeviceInitialization": "true",
                "unicodeKeyBoard": "true",
                "resetKeyBoard": "true"}

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_add_member(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/en5' and @text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        memberName = self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b7n' and @text ='姓名　']/..//*[@text='必填']")
        memberName.send_keys('xiaohua3')

        memberPhone = self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b7n' and @text ='手机　']/..//*[@text='必填']")
        memberPhone.send_keys('15809993300')

        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/aj_").click()
        sleep(1)

        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")

```

### （一）搭建框架
1.先编写启动app 的模块文件：
```python
from Appium.wework.pages.main import Main


class App:
    def start(self):
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main()
```

2.编写main文件（企业微信主页）：
```python
from Appium.wework.pages.addressList import AddressList


class Main:
    def goto_message(self):
        pass

    def goto_address_list(self):
        return AddressList()

    def goto_work_bench(self):
        pass

    def goto_profile(self):
        pass
```

3.编写address_list（通讯录主页）文件：
```python
from Appium.wework.pages.manual_invitet import ManualInvite


class AddressList:
    def add_member(self):
        return ManualInvite()

    def my_client(self):
        pass
```

4.编写manual_invitet（添加成员主页）文件：
```python
class ManualInvite:
    def add_member_by_menul(self):
        from Appium.wework.pages.contact_add import ContactAdd
        return  ContactAdd()

    def get_toast(self):
        pass
```

5.编写contact_add（手动输入功能页）文件：
```python
class ContactAdd:
    def input_name(self):
        return self

    def input_phone_number(self):
        return self

    def click_save(self):
        from Appium.wework.pages.manual_invitet import ManualInvite
        return ManualInvite()
```

注：此处由于手动添加成员完成后会自动返回上一页，所以是这两个页面互相调的，导入包的时候需要在原地导入。

6.根据步骤创建测试用例：
```python
from Appium.wework.pages.app import App


class TestAdderss:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_add_contact(self):
        self.main.goto_address_list().add_member().
        add_member_by_menul().input_name().
        input_phone_number().click_save()
```

## （二）在框架中进行填充
1.先创建一个base_page文件，存放公共方法（__init__）方法

```python
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver):
        self._driver = driver
```

2.将自动化步骤拆解到对应模块中，并集成BasePage

1）app模块：
```python
class App:
    def start(self):
        caps = {"platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": "com.tencent.wework.launch.WwMainActivity",
                "noReset": "true",
                "skipDeviceInitialization": "true",
                "unicodeKeyBoard": "true",
                "resetKeyBoard": "true"}

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def main(self) -> Main:
        return Main(self.driver)
```

2）main模块：
```python
class Main(BasePage):
    def goto_message(self):
        pass

    def goto_address_list(self):
        self._driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/en5' and @text='通讯录']").click()
        return AddressList(self._driver)
```

3）address_list模块：
```python
class AddressList(BasePage):
    def add_member(self):
        self._driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return ManualInvite(self._driver)

    def my_client(self):
        pass
```

4）manual_invitet模块：
```python
class ManualInvite(BasePage):
    def add_member_by_menul(self):
        from Appium.wework.pages.contact_add import ContactAdd
        self._driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return  ContactAdd(self._driver)

    def get_toast(self):
        toast = self._driver.find_element(MobileBy.XPATH, "//*[@class='android.widgt.Toast']").text
        return toast
```

5）contact_add模块：
```python
class ContactAdd(BasePage):
    def input_name(self):
        memberName = self._driver.find_element(MobileBy.XPATH,
                                              "//*[@resource-id='com.tencent.wework:id/b7n' and @text ='姓名　']/..//*[@text='必填']")
        memberName.send_keys('xiaohua3')
        return self

    def input_phone_number(self):
        memberPhone = self._driver.find_element(MobileBy.XPATH,
                                               "//*[@resource-id='com.tencent.wework:id/b7n' and @text ='手机　']/..//*[@text='必填']")
        memberPhone.send_keys('15809993300')
        return self

    def click_save(self):
        from Appium.wework.pages.manual_invitet import ManualInvite
        self._driver.find_element(MobileBy.ID, "com.tencent.wework:id/aj_").click()
        return ManualInvite(self._driver)
```


6）test_address 测试用例修改：
```python
class TestAdderss:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_add_contact(self):
        add_contact =self.main.goto_address_list().add_member().add_member_by_menul().\
            input_name().input_phone_number().click_save()

        add_contact.get_toast()

        assert '成功' in add_contact.get_toast()
```

## （三）优化代码
1.在app模块中判断driver是否存在，如果没有则初始化，如果已存在，则直接启动：
```python
class App:
    def start(self):
        if self.driver == None:
            caps = {"platformName": "android",
                    "deviceName": "127.0.0.1:7555",
                    "appPackage": "com.tencent.wework",
                    "appActivity": "com.tencent.wework.launch.WwMainActivity",
                    "noReset": "true",
                    "skipDeviceInitialization": "true",
                    "unicodeKeyBoard": "true",
                    "resetKeyBoard": "true",
                    "skipServerInstallation":True,
                    "skipDeviceInintialization":True
                    }

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
```

注：launch_app()是appium自己封装的一个功能，可直接启动app。

2.封装find方法

1）在base_page中封装find方法
```python
class BasePage:
    _black_list = [
        (By.XPATH, "//*[@text='确认']"),
        (By.XPATH, "//*[@text='下次再说']"),
        (By.XPATH, "//*[@text='确定']")
    ]

    def __init__(self, driver: WebDriver=None):
        self._driver = driver

    def find(self, locator, value: str = None):
        element: WebElement
        try:
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator, value)
            return element
        except:
            for ele in self._black_list:
                ele_list = self._driver.find_elements(*ele)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    return self.find(locator, value)
```

2）在其他所有文件中将 self._driver.find_element 进行替换。

3.以上代码有个问题，如果找不到元素，会一直等到隐式等待结束为止，才弹出找不到的信息，需优化。修改base_page文件：
```python
class BasePage:
    _black_list = [
        (By.XPATH, "//*[@text='确认']"),
        (By.XPATH, "//*[@text='下次再说']"),
        (By.XPATH, "//*[@text='确定']")
    ]

    _max_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver=None):
        self._driver = driver

    def find(self, locator, value: str = None):
        element: WebElement
        try:
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator, value)

            self._error_num =0
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            self._driver.implicitly_wait(1)
            if self._error_num > self._max_num:
                raise e
            self._error_num = +1
           
            for ele in self._black_list:
                ele_list = self._driver.find_elements(*ele)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    return self.find(locator, value)
        
            raise e
```

## （四）增加日志
1.在base_page中增加日志信息
```python
class BasePage:
    logging.basicConfig(level=logging.info)
    _black_list = [
        (By.XPATH, "//*[@text='确认']"),
        (By.XPATH, "//*[@text='下次再说']"),
        (By.XPATH, "//*[@text='确定']")
    ]

    _max_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver=None):
        self._driver = driver

    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        element: WebElement
        try:
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator, value)

            self._error_num =0
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            self._driver.implicitly_wait(1)
            if self._error_num > self._max_num:
                raise e
            self._error_num = +1


            for ele in self._black_list:
                ele_list = self._driver.find_elements(*ele)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    return self.find(locator, value)

            raise e

```
