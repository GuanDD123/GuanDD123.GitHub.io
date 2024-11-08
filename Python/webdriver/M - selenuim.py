import selenium
import selenium.webdriver
import selenium.webdriver.common
import selenium.webdriver.remote
import selenium.webdriver.remote.webelement


class Driver:

    def _():
        from selenium.webdriver import Chrome
        driver = Chrome()

        driver.get(url=str)

        driver.close()
        driver.quit()

    def anti_shield(driver: selenium.webdriver.Chrome):
        with open('stealth.min.js', encoding='utf-8') as f:
            driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                'source': f.read()})  # 在页面刚加载的时候执行JavaScript语句

        from undetected_chromedriver import Chrome
        Chrome()

    def info(driver: selenium.webdriver.Chrome):
        driver.title
        driver.current_url

    def content(driver: selenium.webdriver.Chrome):
        driver.page_source

        driver.get_screenshot_as_file(filename=str)
        driver.get_screenshot_as_png()
        driver.get_screenshot_as_base64()

    def window_size(driver: selenium.webdriver.Chrome):
        driver.maximize_window()
        driver.set_window_size(width=int, height=int)

    def refresh_forward_back(driver: selenium.webdriver.Chrome):
        driver.refresh()

        driver.forward()
        driver.back()

    def cookie(driver: selenium.webdriver.Chrome):
        driver.get_cookies()

        driver.add_cookie(cookie_dict=dict)

        driver.delete_cookie(name=str)
        driver.delete_all_cookies()

    def switch_tag_frame(driver: selenium.webdriver.Chrome):
        from selenium.webdriver.remote.webelement import WebElement

        driver.switch_to.frame(frame_reference=WebElement)
        driver.switch_to.parent_frame()

    def switch_window_frame(driver: selenium.webdriver.Chrome):
        driver.execute_script(script='window.open()')  # 打开新标签页

        handle = driver.current_window_handle
        handle_list = driver.window_handles
        driver.switch_to.window(window_name=handle)

    def headless():
        from selenium.webdriver import Chrome, ChromeOptions

        options = ChromeOptions()
        options.add_argument('--headless')
        driver = Chrome(options=options)
        driver.set_window_size(width=int, height=int)

    def webdriver_path():
        from selenium.webdriver import Chrome
        from selenium.webdriver.chrome.service import Service

        service = Service(executable_path=str)
        Chrome(service=service)

    def proxy_public():
        from selenium.webdriver import Chrome, ChromeOptions

        options = ChromeOptions()
        proxy = '127.0.0.1:9743'
        options.add_argument('--proxy-server=http://'+proxy)  # 无认证代理
        Chrome(options=options)

    def proxy_private():
        from selenium.webdriver import Chrome, ChromeOptions
        from zipfile import ZipFile

        ip = '127.0.0.1'
        port = 9743
        username = 'foo'
        password = 'bar'

        manifest_json = '''{
        "version":"1.0.0",
        "manifest_version": 2,
        "name":"Chrome Proxy",
        "permissions": ["proxy","tabs","unlimitedStorage","storage","<all_urls>","webRequest","webRequestBlocking"],
        "background": {"scripts": ["background.js"]}
        }'''
        background_js = '''
        var config = {
            mode: "fixed_servers",
            rules: {
                singleProxy: {
                    scheme: "http",
                    host: "%(ip) s",
                    port: % (port) s
                }
            }
        }

        chrome.proxy.settings.set({ value: config, scope: "regular" }, function () { });

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%(username) s",
                    password: "%(password) s"
                }
            }
        }

        chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            { urls: ["<all_urls>"] },
            ['blocking']
        )
        ''' % {'ip': ip, 'port': port, 'username': username, 'password': password}

        plugin_file = 'proxy_auth_plugin.zip'
        with ZipFile(plugin_file, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_extension(extension=plugin_file)
        Chrome(options=options)


class Element:

    def find_elem(driver: selenium.webdriver.Chrome):
        from selenium.webdriver.common.by import By

        driver.find_element(by=By.CSS_SELECTOR | ..., value=str)
        driver.find_elements(by=By.CSS_SELECTOR | ..., value=str)

    def drop_down_tags():
        from selenium.webdriver.remote.webelement import WebElement
        from selenium.webdriver.support.select import Select
        select = Select(webelement=WebElement)

        select.select_by_index(index=int)
        select.select_by_value(value=str)
        select.select_by_visible_text(text=str)

        select.deselect_all()  # 取消所有选项
        select.options  # 获取所有选项
        select.all_selected_options  # 获取已选中的选项

    def interact(elem: selenium.webdriver.remote.webelement.WebElement):
        from selenium.webdriver.common.keys import Keys

        elem.click()

        elem.clear()
        elem.send_keys(value=str | Keys.ENTER | Keys.BACK_SPACE | Keys.ENTER | ...)
        elem.send_keys(Keys.CONTROL, 'a' | 'x' | 'v')  # 全选、剪切、粘贴

        elem.submit()

    def info(elem: selenium.webdriver.remote.webelement.WebElement):
        elem.size
        elem.location  # 返回该节点在页面中的相对位置

        elem.id
        elem.tag_name
        elem.text
        elem.get_attribute(name=str)

        elem.is_displayed()

    def action_chains(driver: selenium.webdriver.Chrome):
        from selenium.webdriver.remote.webelement import WebElement
        from selenium.webdriver import ActionChains
        actions = ActionChains(driver=driver)

        actions = actions.click(on_element=WebElement)
        actions = actions.click_and_hold(on_element=WebElement)
        actions = actions.double_click(on_element=WebElement)
        actions = actions.context_click(on_element=WebElement)

        actions = actions.drag_and_drop(source=WebElement, target=WebElement)
        actions = actions.move_by_offset(xoffset=int, yoffset=int)
        actions = actions.move_to_element(to_element=WebElement)

        actions.perform()

    def wait(driver: selenium.webdriver.Chrome):
        from selenium.webdriver import Chrome
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By

        driver.implicitly_wait(time_to_wait=float)  # 作用范围是Webdriver对象实例的整个生命周期，即 Webdriver 执行每条命令的超时时间都是如此

        wait = WebDriverWait(driver=Chrome, timeout=float)  # 如果超过这个时间元素依然没被加载，就会抛出异常
        check = EC.visibility_of_element_located((By.CSS_SELECTOR | ..., str['locator']))
        wait.until(method=check)

        def EC_value():
            EC.title_is
            EC.title_contains

            EC.presence_of_element_located
            EC.presence_of_all_elements_located
            EC.visibility_of  # 传入节点对象
            EC.visibility_of_element_located  # 传入定位元组
            EC.invisibility_of_element_located  # 判断某个元素是否不存在于 dom 树或不可见
            EC.element_to_be_clickable  # 判断某个元素是否可见且 enable

            EC.text_to_be_present_in_element
            EC.text_to_be_present_in_element_value

            EC.element_to_be_selected
            EC.element_located_to_be_selected
            EC.element_selection_state_to_be
            EC.element_located_selection_state_to_be

            EC.frame_to_be_available_and_switch_to_it  # 判断该 frame 是否可以切换进去，如果可以，返回 True 并且切换进去
            EC.staleness_of  # 等待某个元素从 dom 树中移除
            EC.alert_is_present  # 判断页面是否存在 alert 框

    def By_class_value():
        from selenium.webdriver.common.by import By

        By.TAG_NAME
        By.CLASS_NAME
        By.ID
        By.NAME
        By.LINK_TEXT
        By.PARTIAL_LINK_TEXT
        By.CSS_SELECTOR
        By.XPATH


def run_javascript(driver: selenium.webdriver.Chrome):
    'window.scrollTo(0, document.body.scrollHeight);'  # 将网页拉到底部
    'document.documentElement.scrollTop=10000;'  # 将网页拉到底部
    'document.documentElement.scrollTop=0;'  # 将网页拉到顶部

    driver.execute_script(script=str)  # 同步方法
    driver.execute_async_script(script=str)  # 异步方法
