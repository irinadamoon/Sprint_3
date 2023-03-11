from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from elements import TestLocators

# тест входа по кнопке "Войти в аккаунт" на главной странице
def test_login_from_entry_burron_at_main_page(driver):

    driver.get("https://stellarburgers.nomoreparties.site")
    login = 'Irina_Kuzmina_7_555@ya.ru'
    password = '3160900'

# клик по кн. "Войти в аккаунт"
    driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN_PAGE).click()
# ожидание кликабельности кнопки "Войти"
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGIN_LOGIN_PAGE))

# заполнение полей входа
    driver.find_element(*TestLocators.FIELD_REGISTRATION_NAME).send_keys(login)
    driver.find_element(*TestLocators.FIELD_REGISTRATION_LOGIN).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_LOGIN_LOGIN_PAGE).click()

# ожидание что зашли в лк
    assert expected_conditions.element_to_be_clickable(TestLocators.BUTTON_CHECKOUT_ACCOUNT)


# тест на вход по кнопке "Личный кабинет" в шапке сайта
def test_login_from_personal_account_button_at_top(driver):

    driver.get("https://stellarburgers.nomoreparties.site")
    login = 'Irina_Kuzmina_7_555@ya.ru'
    password = '3160900'

# клик по кн. "Личный кабинет"
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
# ожидание кликабельности кнопки
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGIN_LOGIN_PAGE))

# заполнение полей входа
    driver.find_element(*TestLocators.FIELD_REGISTRATION_NAME).send_keys(login)
    driver.find_element(*TestLocators.FIELD_REGISTRATION_LOGIN).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_LOGIN_LOGIN_PAGE).click()

# ожидание что зашли в лк
    assert expected_conditions.element_to_be_clickable(TestLocators.BUTTON_CHECKOUT_ACCOUNT)



# тест кнопки "Войти" в форме регистрации
def test_button_login_from_registration_form(driver):

    driver.get("https://stellarburgers.nomoreparties.site")
    login = 'Irina_Kuzmina_7_555@ya.ru'
    password = '3160900'

# клик по кн. "Войти в аккаунт"
    driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN_PAGE).click()
# ожидание линка "Зарегистрироваться"
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.LINK_REG_IN_REGISTRATION_FORM))
# клик по линку "Зарегистрироваться"
    driver.find_element(*TestLocators.LINK_REG_IN_REGISTRATION_FORM).click()
# ожидание загрузки формы регистрации (кнопки "Зарегистрироваться")
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_REG_IN_REGISTRATION_FORM))
# клик по линку "Войти"
    driver.find_element(*TestLocators.LINK_LOGIN).click()
# ожидание кликабельности кнопки
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGIN_LOGIN_PAGE))

# заполнение полей входа
    driver.find_element(*TestLocators.FIELD_REGISTRATION_NAME).send_keys(login)
    driver.find_element(*TestLocators.FIELD_REGISTRATION_LOGIN).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_LOGIN_LOGIN_PAGE).click()

# ожидание что зашли в лк
    assert expected_conditions.element_to_be_clickable(TestLocators.BUTTON_CHECKOUT_ACCOUNT)



# тест входа через форму восстановления пароля
def test_login_from_restore_password_form(driver):

    driver.get("https://stellarburgers.nomoreparties.site")
    login = 'Irina_Kuzmina_7_555@ya.ru'
    password = '3160900'

# клик по кн. "Войти в аккаунт"
    driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN_PAGE).click()
# ожидание линка "Восстановить пароль"
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.LINK_RESTORE_PASSWORD))
# клик по линку "Восстановить пароль"
    driver.find_element(*TestLocators.LINK_RESTORE_PASSWORD).click()
# ожидание загрузки линка "Войти"
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.LINK_LOGIN))
# клик по линку "Войти"
    driver.find_element(*TestLocators.LINK_LOGIN).click()
# ожидание загрузки кнопки "Войти"
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGIN_LOGIN_PAGE))

# заполнение полей входа
    driver.find_element(*TestLocators.FIELD_REGISTRATION_NAME).send_keys(login)
    driver.find_element(*TestLocators.FIELD_REGISTRATION_LOGIN).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_LOGIN_LOGIN_PAGE).click()

# ожидание что зашли в лк
    assert expected_conditions.element_to_be_clickable(TestLocators.BUTTON_CHECKOUT_ACCOUNT)



# тест кнопки "Выйти" в личном кабинете
def test_logout_button_from_personal_account(driver):

    driver.get("https://stellarburgers.nomoreparties.site")
    login = 'Irina_Kuzmina_7_555@ya.ru'
    password = '3160900'
# клик по кн. "Войти в аккаунт"
    driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN_PAGE).click()
# ожидание кликабельности кнопки
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGIN_LOGIN_PAGE))

# заполнение полей входа
    driver.find_element(*TestLocators.FIELD_REGISTRATION_NAME).send_keys(login)
    driver.find_element(*TestLocators.FIELD_REGISTRATION_LOGIN).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_LOGIN_LOGIN_PAGE).click()

# ожидание что зашли в лк
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_CHECKOUT_ACCOUNT))
# клик по кн. "Личный кабинет"
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
# ожидание кликабельности кнопки
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_SAVE_IN_PERS_ACC))

# клик по кнопке "Выход"
    driver.find_element(*TestLocators.BUTTON_LOGOUT_IN_PERS_ACC).click()
# ожидание кликабельности кнопки
    assert expected_conditions.element_to_be_clickable(TestLocators.LINK_RESTORE_PASSWORD)

