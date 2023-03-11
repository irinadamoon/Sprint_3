from selenium.webdriver.common.by import By

class TestLocators:

    BUTTON_LOGIN_MAIN_PAGE = [By.XPATH, "//button[text()='Войти в аккаунт']"]   # кн "Войти в аккаунт" на главной стр
    LINK_REG_IN_REGISTRATION_FORM = [By.LINK_TEXT, "Зарегистрироваться"]   # линк "Зарегистрироваться"
    LINK_LOGIN = [By.LINK_TEXT, "Войти"]    # линк "Войти"
    LINK_RESTORE_PASSWORD = [By.LINK_TEXT, "Восстановить пароль"]   # линк "Восстановить пароль"
    BUTTON_REG_IN_REGISTRATION_FORM = [By.XPATH, "//button[text()='Зарегистрироваться']"]   # кн "зарегистрироваться" в форме регистрации
    FIELD_REGISTRATION_NAME = [By.XPATH, "//fieldset[1]//input"]   # поле ввода имени в форме регистр
    FIELD_REGISTRATION_LOGIN = [By.XPATH, "//fieldset[2]//input"]   # поле ввода имейла в форме регистр
    FIELD_REGISTRATION_PASSWORD = [By.XPATH, "//input[@name='Пароль']"]   # поле ввода пароля в форме регистр
    BUTTON_LOGIN_LOGIN_PAGE = [By.XPATH, "//button[text()='Войти']"]   # кн "Войти" на стр логина
    BUTTON_CHECKOUT_ACCOUNT = [By.XPATH, "//button[contains(text(), 'Оформить заказ')]"]   # кн "Оформить заказ" в лк
    BUTTON_PERSONAL_ACCOUNT = [By.XPATH, "//p[contains(text(), 'Личный')]"]   # кн "Личный кабинет"
    BUTTON_SAVE_IN_PERS_ACC = [By.XPATH, "//button[contains(text(), 'Сохранить')]"]   # кн "Сохранить" в личном кабинете
    BUTTON_LOGOUT_IN_PERS_ACC = [By.XPATH, "//button[contains(text(), 'Выход')]"]   # кн "Выход" в личном кабинете
    LINK_CONSTRUCTOR = [By.LINK_TEXT, "Конструктор"]   # линк "Конструктор"
    LOGO_STELLAR_BURGERS = [By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]"]   # логотип
    ERROR_INCORRECT_PASSWORD = [By.XPATH, "//*[contains(text(), 'Некорректный пароль')]"]   # некорректный пароль
    LINK_SAUCES = [By.XPATH, "//span[contains(text(), 'Соусы')]"]   # линк вкладки "Соусы"
    LIST_OF_CARDS = [By.XPATH, "//ul[@class='BurgerIngredients_ingredients__list__2A-mT']"]   # список карточек
    LAST_SAUCES_CARD = [By.XPATH, "//*[contains(text(), 'Соус с шипами Антарианского плоскоходца')]"]   # последняя карточка соусов
    LAST_SAUCES_CARD_IMG = [By.XPATH, "//img[@alt='Соус с шипами Антарианского плоскоходца']" ]  # изображение последней карточки соусов
    LINK_INPUTS = [By.XPATH, "//span[contains(text(), 'Начинки')]"]   # линк вкладки "Начинки"
    LAST_INPUTS_CARD = [By.XPATH, "//*[contains(text(), 'Сыр с астероидной плесенью')]"]   # последняя карточка начинок
    LAST_INPUT_CARD_IMG = [By.XPATH, "//img[@alt='Сыр с астероидной плесенью']"]   # изображение последней карточки начинок
    LINK_BREADS = [By.XPATH, "//span[contains(text(), 'Булки')]"]   # линк вкладки "Булки"
    LAST_BREAD_CARD = [By.XPATH, "//*[contains(text(), 'Краторная')]"]   # последняя карточка булок
    LAST_BREAD_CARD_IMG = [By.XPATH, "//img[@alt='Краторная булка N-200i']"]   # изображение последней карточки булок
    BUTTON_CONSTRUCTOR = [By.XPATH, "//*[contains(text(), 'Конструктор')]"]   # кн "Конструктор"



# ".//input[@class='text input__textfield text_type_main-default']")[0]   # поле ввода имени в форме регистрации
# ".//input[@class='text input__textfield text_type_main-default']")[1]   # поле ввода мейла в форме регистрации
# ".//input[@class='text input__textfield text_type_main-default' and @type='password']")   # поле ввода пароля в форме регистрации


#LONG_XPATH_FOR FIELDS = ((.//input[@class="text input__textfield text_type_main-default"])[2])') # поле ввода