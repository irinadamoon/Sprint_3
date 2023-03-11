from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from elements import TestLocators

# переход "Булки" -> "Соусы"

def test_page_transition_breads_sauses(driver):

    driver.get("https://stellarburgers.nomoreparties.site")

# клик по вкладке "Соусы"
    driver.find_element(*TestLocators.LINK_SAUCES).click()

# ожидание загрузки списка карточек
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LIST_OF_CARDS)))

# скролл до нижней карточки
    element = driver.find_element(*TestLocators.LAST_SAUCES_CARD)
    driver.execute_script("arguments[0].scrollIntoView();", element)

    assert expected_conditions.visibility_of_element_located((TestLocators.LAST_SAUCES_CARD_IMG))



# переход "Соусы" -> "Начинки"
def test_page_transition_sauses_inputs(driver):

    driver.get("https://stellarburgers.nomoreparties.site")

# клик по вкладке 'Соусы'
    driver.find_element(*TestLocators.LINK_SAUCES).click()
# клик по вкладке "Начинки"
    driver.find_element(*TestLocators.LINK_INPUTS).click()

# ожидание загрузки списка карточек
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LIST_OF_CARDS)))
# скролл до нижней карточки
    element = driver.find_element(*TestLocators.LAST_INPUTS_CARD)
    driver.execute_script("arguments[0].scrollIntoView();", element)

    assert expected_conditions.visibility_of_element_located((TestLocators.LAST_INPUT_CARD_IMG))




# переход "Начинки" -> "Булки"
def test_page_transition_inputs_breads(driver):

    driver.get("https://stellarburgers.nomoreparties.site")

# клик по вкладке "Начинки"
    driver.find_element(*TestLocators.LINK_INPUTS).click()
# клик по вкладке 'Булки'
    driver.find_element(*TestLocators.LINK_BREADS).click()

# ожидание загрузки списка карточек
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LIST_OF_CARDS)))
# скролл до нижней карточки
    element = driver.find_element(*TestLocators.LAST_BREAD_CARD)
    driver.execute_script("arguments[0].scrollIntoView();", element)

    assert expected_conditions.visibility_of_element_located((TestLocators.LAST_BREAD_CARD_IMG))
