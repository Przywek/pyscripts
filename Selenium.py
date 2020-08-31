from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time, logging
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
logger = logging.getLogger('MyL_configurator')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('MYL_logs.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)
browser = webdriver.Firefox(executable_path=r'C:\\work\\Selenium\\geckodriver.exe')
browser.maximize_window()
browser.get('http://mypos/')
data = input("Wprowadź date do konfiguracji: ")
mpk = []
with open("C:\\work\\pythonscripts\\mpk.txt",'r') as f:
    for line in f:
        mpk1 = line.replace("\n", "")
        mpk.append(mpk1)

def login(username, company, password):
    usr = browser.find_element_by_id('usr')
    usr.send_keys(username)
    cpny = browser.find_element_by_id('cpny')
    cpny.send_keys(company)
    pas = browser.find_element_by_id('pwd')
    pas.send_keys(password)
    log = browser.find_element_by_id('Login')
    log.click()


def org_struc_loc(mpk, zone):
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('sideMenu'))
    tab = browser.find_element_by_id('10')
    tab.click()
    portal = browser.find_element_by_link_text('Portal')
    portal.click()
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    time.sleep(4)
    Org_str = browser.find_elements_by_id('Cat3')
    toggle = Org_str[1].find_elements_by_css_selector('td')
    toggle[1].click()
    loc = browser.find_element_by_link_text('Locations')
    loc.click()
    time.sleep(8)
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    loc_mpk = browser.find_element_by_id('selectedOrgLvlRef')
    loc_mpk.send_keys(mpk)
    edit = browser.find_element_by_id('editSubmit')
    edit.click()
    time.sleep(5)
    time_zone = Select(browser.find_element_by_id('timeZoneID'))
    time_zone.select_by_value(str(zone))
    Eel = browser.find_element_by_id('enableConfigurationMode1').is_displayed()
    if Eel == True:
        name = browser.find_element_by_id('orgLevelName').get_attribute('value')
        logger.info("tu bylo zaklikane wszystko; " + name)
        return name
    else:
        browser.find_element_by_id('enableEnterpriseLabor').click()
        browser.find_element_by_id('enableConfigurationMode1').click()
        name = browser.find_element_by_id('orgLevelName').get_attribute('value')
        browser.find_element_by_id('saveSubmit').click()
        logger.info("Tu nie bylo wszystko zaklikane; " + name)
        time.sleep(1)
        obj = browser.switch_to_alert()
        obj.accept()
        return name


def location_configuration(name, data):
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('sideMenu'))
    tab = browser.find_element_by_id('8')
    tab.click()
    tab.click()
    payroll_prep = browser.find_element_by_link_text('Payroll Prepr.')
    payroll_prep.click()
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    time.sleep(3)
    admin = browser.find_element_by_id('20')
    das = admin.find_elements_by_css_selector('td')
    das[0].click()
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    time.sleep(1)
    loc_con = browser.find_element_by_id('32')
    loc = loc_con.find_elements_by_css_selector('td')
    loc[0].click()
    time.sleep(10)
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    form = browser.find_element_by_name('entLocLaborRuleForm')
    table = form.find_elements_by_class_name('embeddedTable100')
    rest = table[1].find_elements_by_css_selector('li')
    while True:
        try:
            for ele in rest[575:]:
                if ele.text == name:
                    ele.find_element_by_css_selector('input').click()
                    break
                else:
                    continue
        except StaleElementReferenceException:
            break
    time.sleep(6)
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    form = browser.find_element_by_name('entLocLaborRuleForm')
    P_R_check = form.find_element_by_id('entPayRuleUpdated')
    P_R_check.click()
    P_R_data = form.find_element_by_id('entPayRuleEffectiveFrom')
    P_R_data.clear()
    P_R_data.send_keys(data)
    P_R_sel = Select(form.find_element_by_id('entPayRuleID'))
    P_R_sel.select_by_value('276264740')
    save = browser.find_element_by_id('Save')
    save.click()
    time.sleep(6)
    obj = browser.switch_to_alert()
    obj.accept()
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    form = browser.find_element_by_name('entLocLaborRuleForm')
    p_p_check = form.find_element_by_id('payPeriodCalendarUpdated')
    p_p_check.click()
    p_p_data = form.find_element_by_id('payPeriodCalendarEffectiveFrom')
    p_p_data.clear()
    p_p_data.send_keys(data)
    p_p_sel = Select(form.find_element_by_id('payPeriodCalendarID'))
    p_p_sel.select_by_value('276264601')
    save = browser.find_element_by_id('Save')
    save.click()
    time.sleep(10)
    obj = browser.switch_to_alert()
    obj.accept()
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    form = browser.find_element_by_name('entLocLaborRuleForm')
    w_t_check = form.find_element_by_id('entWageTipLawUpdated')
    w_t_check.click()
    w_t_data = form.find_element_by_id('entWageTipLawEffectiveFrom')
    w_t_data.clear()
    w_t_data.send_keys(data)
    w_t_sel = Select(form.find_element_by_id('entWageTipLawID'))
    w_t_sel.select_by_value('2901')
    save = browser.find_element_by_id('Save')
    save.click()
    time.sleep(10)
    obj = browser.switch_to_alert()
    obj.accept()
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    form = browser.find_element_by_name('entLocLaborRuleForm')
    c_l_check = form.find_element_by_id('entChildLaborLawUpdated')
    c_l_check.click()
    c_l_data = form.find_element_by_id('entChildLaborLawEffectiveFrom')
    c_l_data.clear()
    c_l_data.send_keys(data)
    c_l_sel = Select(form.find_element_by_id('entChildLaborLawID'))
    c_l_sel.select_by_value('1034')
    save = browser.find_element_by_id('Save')
    save.click()
    time.sleep(7)
    obj = browser.switch_to_alert()
    obj.accept()
    browser.switch_to_default_content()


def location_assignment(name):
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('sideMenu'))
    tab = browser.find_element_by_id('8')
    tab.click()
    tab.click()
    payroll_prep = browser.find_element_by_link_text('Payroll Prepr.')
    payroll_prep.click()
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    time.sleep(8)
    admin = browser.find_element_by_id('20')
    das = admin.find_elements_by_css_selector('td')
    das[0].click()
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    time.sleep(1)
    loc_con = browser.find_element_by_id('31')
    loc = loc_con.find_elements_by_css_selector('td')
    loc[0].click()
    time.sleep(8)
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    form = browser.find_element_by_name('entLocationAssignmentForm')
    table = form.find_elements_by_class_name('embeddedTable100')
    rest = table[1].find_elements_by_css_selector('li')
    while True:
        try:
            for ele in rest[575:]:
                if ele.text == name:
                    ele.find_element_by_css_selector('input').click()
                    break
                else:
                    continue
        except StaleElementReferenceException:
            break
    time.sleep(2)
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    form = browser.find_element_by_name('entLocationAssignmentForm')
    Select(form.find_element_by_id('entWorkRuleID')).select_by_value('276274550')
    Select(form.find_element_by_id('laborWeekStartDay')).select_by_value('3')
    Select(form.find_element_by_id('forecastWeekStartDay')).select_by_value('3')
    Select(form.find_element_by_id('laborShareLevelID')).select_by_value('119902')
    Select(form.find_element_by_id('scheduleWeekStartDay')).select_by_value('3')
    Select(form.find_element_by_id('startBusinessDayFixedPeriod')).select_by_value('15')
    Select(form.find_element_by_id('startLaborHour')).select_by_value('3')
    Select(form.find_element_by_id('startLaborHourGraceMinutes')).select_by_value('15')
    Select(form.find_element_by_id('entStoreHoursID')).select_by_value('11187')
    save = browser.find_element_by_id('Save')
    save.click()
    time.sleep(1)
    obj = browser.switch_to_alert()
    obj.accept()
    browser.switch_to_default_content()


def break_rules(data, name):
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('sideMenu'))
    tab = browser.find_element_by_id('8')
    tab.click()
    tab.click()
    payroll_prep = browser.find_element_by_link_text('Payroll Prepr.')
    payroll_prep.click()
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    time.sleep(5)
    admin = browser.find_element_by_id('20')
    das = admin.find_elements_by_css_selector('td')
    das[0].click()
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    time.sleep(1)
    loc_con = browser.find_element_by_id('29')
    loc = loc_con.find_elements_by_css_selector('td')
    loc[0].click()
    time.sleep(15)
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))

    form = browser.find_element_by_name('entLocationBreakRuleForm')
    table = form.find_elements_by_class_name('embeddedTable100')
    rest = table[1].find_elements_by_css_selector('li')
    while True:
        try:
            for ele in rest[575:]:
                if ele.text == name:
                    ele.find_element_by_css_selector('input').click()
                    break
                else:
                    continue
        except StaleElementReferenceException:
            break
    time.sleep(6)
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))

    form = browser.find_element_by_name('entLocationBreakRuleForm')
    form.find_element_by_id("Add Break Rule").click()
    form.find_element_by_id("Add Break Rule").click()
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    time.sleep(2)
    form = browser.find_element_by_name('entLocationBreakRuleForm')
    Select(form.find_element_by_id('addedAssignmentList[0].recordID')).select_by_value('55901147')
    Select(form.find_element_by_id('addedAssignmentList[1].recordID')).select_by_value('55901152')
    form.find_element_by_id('addedAssignmentList[0].effectiveFromDateFormatted').send_keys(data)
    form.find_element_by_id('addedAssignmentList[1].effectiveFromDateFormatted').send_keys(data)
    form = browser.find_element_by_name('entLocationBreakRuleForm')
    form.find_element_by_id("Add Minor Break Rule").click()
    Select(form.find_element_by_id('addedAssignmentList[2].recordID')).select_by_value('276264660')
    form.find_element_by_id('addedAssignmentList[2].effectiveFromDateFormatted').send_keys(data)
    save = browser.find_element_by_id('Save')
    save.click()
    time.sleep(10)
    obj = browser.switch_to_alert()
    obj.accept()
    time.sleep(2)
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    form = browser.find_element_by_name('entLocationBreakRuleForm')
    form.find_element_by_id("Add Minor Break Rule").click()
    Select(form.find_element_by_id('addedAssignmentList[0].recordID')).select_by_value('276264661')
    form.find_element_by_id('addedAssignmentList[0].effectiveFromDateFormatted').send_keys(data)
    save = browser.find_element_by_id('Save')
    save.click()
    time.sleep(7)
    obj = browser.switch_to_alert()
    obj.accept()
    browser.switch_to_default_content()
    time.sleep(1)
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    time.sleep(1)
    form = browser.find_element_by_name('entLocationBreakRuleForm')
    form.find_element_by_id('link1').click()
    form = browser.find_element_by_name('entLocationBreakRuleForm')
    bk = form.find_element_by_id('promptForBreak')
    pbk = form.find_element_by_id('authReqdLateInPaidBreak')
    ubk = form.find_element_by_id('authReqdLateInUnpaidBreak')
    if bk.get_property('checked') != True:
        bk.click()
        if pbk.get_property('checked') != True:
            pbk.click()
            if ubk.get_property('checked') != True:
                ubk.click()
    browser.switch_to_default_content()
    time.sleep(1)
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    save = browser.find_element_by_id('Save')
    save.click()
    time.sleep(15)
    obj = browser.switch_to_alert()
    obj.accept()
    browser.switch_to_default_content()


def P_R_location_assigment(data, name):
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('sideMenu'))
    tab = browser.find_element_by_id('8')
    tab.click()
    tab.click()
    payroll_prep = browser.find_element_by_link_text('Payroll Prepr.')
    payroll_prep.click()
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    time.sleep(5)
    admin = browser.find_element_by_id('20')
    das = admin.find_elements_by_css_selector('td')
    das[0].click()
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    time.sleep(1)
    loc_con = browser.find_element_by_id('26')
    loc = loc_con.find_elements_by_css_selector('td')
    loc[0].click()
    time.sleep(4)
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    form = browser.find_element_by_name('premiumPayLocationAssignmentForm')
    table = form.find_elements_by_class_name('embeddedTable100')
    rest = table[1].find_elements_by_css_selector('li')
    while True:
        try:
            for ele in rest[575:]:
                if ele.text == name:
                    ele.find_element_by_css_selector('input').click()
                    break
                else:
                    continue
        except StaleElementReferenceException:
            break
    time.sleep(2)
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    form = browser.find_element_by_name('premiumPayLocationAssignmentForm')
    Select(form.find_element_by_id('jobCodeID')).select_by_value('1872')
    Select(form.find_element_by_id('premiumPayRuleID')).select_by_value('10653847')
    form.find_element_by_id('effectiveFrom').send_keys(data)
    browser.find_element_by_id('Save').click()
    time.sleep(1)
    while True:
        try:
            WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            obj = browser.switch_to_alert()
            obj.accept()
            break
        except TimeoutException:
            break
    browser.switch_to_default_content()
    time.sleep(1)
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    form = browser.find_element_by_name('premiumPayLocationAssignmentForm')
    Select(form.find_element_by_id('jobCodeID')).select_by_value('1035')
    Select(form.find_element_by_id('premiumPayRuleID')).select_by_value('10653847')
    form.find_element_by_id('effectiveFrom').clear()
    form.find_element_by_id('effectiveFrom').send_keys(data)
    browser.find_element_by_id('Save').click()
    time.sleep(1)
    while True:
        try:
            WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            obj = browser.switch_to_alert()
            obj.accept()
            break
        except TimeoutException:
            break
    browser.switch_to_default_content()
    time.sleep(1)
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    form = browser.find_element_by_name('premiumPayLocationAssignmentForm')
    Select(form.find_element_by_id('jobCodeID')).select_by_value('1117')
    Select(form.find_element_by_id('premiumPayRuleID')).select_by_value('10653847')
    form.find_element_by_id('effectiveFrom').clear()
    form.find_element_by_id('effectiveFrom').send_keys(data)
    browser.find_element_by_id('Save').click()
    time.sleep(1)
    while True:
        try:
            WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            obj = browser.switch_to_alert()
            obj.accept()
            break
        except TimeoutException:
            break
    browser.switch_to_default_content()
    time.sleep(1)
    browser.switch_to.frame(browser.find_element_by_id('myPage'))


def forecasting_location_administration(name):
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('sideMenu'))
    tab = browser.find_element_by_id('8')
    tab.click()
    tab.click()
    forecasting = browser.find_element_by_link_text('Forecasting Administration')
    forecasting.click()
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    time.sleep(5)
    admin = browser.find_element_by_id('0')
    das = admin.find_elements_by_css_selector('td')
    das[0].click()
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    time.sleep(1)
    loc_con = browser.find_element_by_id('5')
    loc = loc_con.find_elements_by_css_selector('td')
    loc[0].click()
    time.sleep(6)
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    form = browser.find_element_by_name('entLocationAssignmentForm')
    table = form.find_elements_by_class_name('embeddedTable100')
    rest = table[1].find_elements_by_css_selector('li')
    while True:
        try:
            for ele in rest[575:]:
                if ele.text == name:
                    ele.find_element_by_css_selector('input').click()
                    break
                else:
                    continue
        except StaleElementReferenceException:
            break
    time.sleep(5)
    browser.switch_to_default_content()
    browser.switch_to.frame(browser.find_element_by_id('myPage'))
    time.sleep(1)
    form = browser.find_element_by_name('entLocationAssignmentForm')
    Select(form.find_element_by_id('laborWeekStartDay')).select_by_value('3')
    Select(form.find_element_by_id('forecastWeekStartDay')).select_by_value('3')
    Select(form.find_element_by_id('startBusinessDayFixedPeriod')).select_by_value('15')
    Select(form.find_element_by_id('startLaborHour')).select_by_value('3')
    save = browser.find_element_by_id('Save')
    save.click()
    time.sleep(8)
    obj = browser.switch_to_alert()
    obj.accept()
    browser.switch_to_default_content()


login(username, 'dell', password)
for x in mpk:
    logger.info("Zaczynam konfigurowac; " + x)
    y = str(x)
    name = org_struc_loc(y, 861)
    logger.info("Struktura skonfigurowana; " + x)
    location_configuration(name, data)
    logger.info("Konfiguracja lokacji skonfigurowana; " + x)
    location_assignment(name)
    logger.info("Konfiguracja przypisana lokacji skonfigurowana; " + x)
    break_rules(data, name)
    logger.info("Reguly przerw skonfigurowane w ; " + x)
    P_R_location_assigment(data, name)
    logger.info("Konfiguracja przypisana lokacji P_R skonfigurowana; " + x)
    forecasting_location_administration(name)
    logger.info("Zakonczono konfiguracje; " + x)
browser.close()
