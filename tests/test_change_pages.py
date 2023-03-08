from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from elements import TestLocators

# тест перехода в Личный кабинет по клику на кнопку "Личный кабинет"
def test_login_using_personal_account_button(driver):

    driver.get("https://stellarburgers.nomoreparties.site")
    login = 'Irina_Kuzmina_7_555@ya.ru'
    password = '3160900'

# клик по кн. "Личный кабинет"
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
# ожидание кликабельности кнопки
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.BUTTON_LOGIN_LOGIN_PAGE)))

# заполнение полей входа
    driver.find_element(*TestLocators.FIELD_REGISTRATION_NAME).send_keys(login)
    driver.find_element(*TestLocators.FIELD_REGISTRATION_LOGIN).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_LOGIN_LOGIN_PAGE).click()

# ожидание что зашли в лк
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.BUTTON_CHECKOUT_ACCOUNT)))
# клик по кн. "Личный кабинет"
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
# проверка кликабельности кнопки
    assert expected_conditions.element_to_be_clickable(TestLocators.BUTTON_SAVE_IN_PERS_ACC)
    driver.quit()


# тест перехода из Личного кабинета в конструктор по кнопке "Конструктор"
def test_move_from_personal_account_to_constructor_using_constructor_button(driver):

    driver.get("https://stellarburgers.nomoreparties.site")
    login = 'Irina_Kuzmina_7_555@ya.ru'
    password = '3160900'

# клик по кн. "Личный кабинет"
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
# ожидание кликабельности кнопки
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.BUTTON_LOGIN_LOGIN_PAGE)))

# заполнение полей входа
    driver.find_element(*TestLocators.FIELD_REGISTRATION_NAME).send_keys(login)
    driver.find_element(*TestLocators.FIELD_REGISTRATION_LOGIN).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_LOGIN_LOGIN_PAGE).click()

# ожидание что зашли в лк
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.BUTTON_CHECKOUT_ACCOUNT)))
# клик по кн. "Личный кабинет"
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
# ожидание кликабельности кнопки
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.BUTTON_SAVE_IN_PERS_ACC)))

# клик на кнопку "Конструктор"
    driver.find_element(*TestLocators.LINK_CONSTRUCTOR).click()
# ожидание кликабельности кнопки
    assert expected_conditions.element_to_be_clickable((TestLocators.BUTTON_CHECKOUT_ACCOUNT))
    driver.quit()

# тест перехода из личного кабинета в конструктор по клику на логотип Stellar Burgers
def test_move_from_personal_account_to_constructor_using_logo(driver):

    driver.get("https://stellarburgers.nomoreparties.site")
    login = 'Irina_Kuzmina_7_555@ya.ru'
    password = '3160900'

# клик по кн. "Личный кабинет"
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
# ожидание кликабельности кнопки
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.BUTTON_LOGIN_LOGIN_PAGE)))

# заполнение полей входа
    driver.find_element(*TestLocators.FIELD_REGISTRATION_NAME).send_keys(login)
    driver.find_element(*TestLocators.FIELD_REGISTRATION_LOGIN).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_LOGIN_LOGIN_PAGE).click()

# ожидание что зашли в лк
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.BUTTON_CHECKOUT_ACCOUNT)))
# клик по кн. "Личный кабинет"
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
# ожидание кликабельности кнопки
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.BUTTON_SAVE_IN_PERS_ACC)))

# клик на кнопку "Конструктор"
    driver.find_element(*TestLocators.LOGO_STELLAR_BURGERS).click()
# ожидание кликабельности кнопки
    assert expected_conditions.element_to_be_clickable((TestLocators.BUTTON_CHECKOUT_ACCOUNT))
    driver.quit()