
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from elements import TestLocators
import generators

# Тест на возможность регистрации
def test_registration_possibility(driver):

    driver.get("https://stellarburgers.nomoreparties.site")

# клик по кн. "Войти в аккаунт"
    driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN_PAGE).click()
# ожидание линка "Зарегистрироваться"
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.LINK_REG_IN_REGISTRATION_FORM))

# клик по линку "Зарегистрироваться"
    driver.find_element(*TestLocators.LINK_REG_IN_REGISTRATION_FORM).click()
# ожидание загрузки формы регистрации (кнопки "Зарегистрироваться")
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_REG_IN_REGISTRATION_FORM))

# заполнение полей формы регистрации
    name = generators.gen_name()
    login = generators.gen_login()
    password = generators.gen_password()
    driver.find_element(*TestLocators.FIELD_REGISTRATION_NAME).send_keys(name)
    driver.find_element(*TestLocators.FIELD_REGISTRATION_LOGIN).send_keys(login)
    driver.find_element(*TestLocators.FIELD_REGISTRATION_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_REG_IN_REGISTRATION_FORM).click()
# ожидание загрузки
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGIN_LOGIN_PAGE))

# заполнение полей входа
    driver.find_element(*TestLocators.FIELD_REGISTRATION_NAME).send_keys(login)
    driver.find_element(*TestLocators.FIELD_REGISTRATION_LOGIN).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_LOGIN_LOGIN_PAGE).click()
# проверка что зашли в лк
    assert expected_conditions.element_to_be_clickable(TestLocators.BUTTON_CHECKOUT_ACCOUNT)
    driver.quit()


# Тест на некорректный пароль (есть ошибкв)
def test_incorrect_len5_password_misstake_message(driver):

    driver.get("https://stellarburgers.nomoreparties.site")

# клик по кн. "Войти в аккаунт"
    driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN_PAGE).click()
# ожидание линка "Зарегистрироваться"
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.LINK_REG_IN_REGISTRATION_FORM))

# клик по линку "Зарегистрироваться"
    driver.find_element(*TestLocators.LINK_REG_IN_REGISTRATION_FORM).click()
# ожидание загрузки формы регистрации (кнопки "Зарегистрироваться")
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_REG_IN_REGISTRATION_FORM))

# заполнение полей формы регистрации
    name = generators.gen_name()
    login = generators.gen_login()
    driver.find_element(*TestLocators.FIELD_REGISTRATION_NAME).send_keys(name)
    driver.find_element(*TestLocators.FIELD_REGISTRATION_LOGIN).send_keys(login)
    driver.find_element(*TestLocators.FIELD_REGISTRATION_PASSWORD).send_keys('55555')
    driver.find_element(*TestLocators.BUTTON_REG_IN_REGISTRATION_FORM).click()
# проверка наличия ошибки
    assert driver.find_element(*TestLocators.ERROR_INCORRECT_PASSWORD)
    driver.quit()
