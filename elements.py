from selenium.webdriver.common.by import By

class TestLocators:

    BUTTON_LOGIN_MAIN_PAGE = [By.XPATH, "//button[text()='Войти в аккаунт']"]   # кн "Войти в аккаунт" на главной стр
    LINK_REG_IN_REGISTRATION_FORM = [By.LINK_TEXT, "Зарегистрироваться"]   # линк "Зарегистрироваться"
    LINK_LOGIN = [By.LINK_TEXT, "Войти"]    # линк "Войти"
    LINK_RESTORE_PASSWORD = [By.LINK_TEXT, "Восстановить пароль"]   # линк "Восстановить пароль"
    BUTTON_REG_IN_REGISTRATION_FORM = [By.XPATH, "//button[text()='Зарегистрироваться']"]   # кн "зарегистрироваться" в форме регистрации
    FIELD_REGISTRATION_NAME = [By.XPATH, "//fieldset[1]//input"]   # поле ввода имени в форме регистр
    FIELD_REGISTRATION_LOGIN = [By.XPATH, "//fieldset[2]//input"]   # поле ввода имейла в форме регистр
    FIELD_REGISTRATION_PASSWORD = [By.XPATH, "//fieldset[3]//input"]   # поле ввода пароля в форме регистр
    BUTTON_LOGIN_LOGIN_PAGE = [By.XPATH, "//button[text()='Войти']"]   # кн "Войти" на стр логина
    BUTTON_CHECKOUT_ACCOUNT = [By.XPATH, "//button[contains(text(), 'Оформить заказ')]"]   # кн "Оформить заказ" в лк
    BUTTON_PERSONAL_ACCOUNT = [By.XPATH, "//p[contains(text(), 'Личный')]"]   # кн "Личный кабинет"
    BUTTON_SAVE_IN_PERS_ACC = [By.XPATH, "//button[contains(text(), 'Сохранить')]"]   # кн "Сохранить" в личном кабинете
    BUTTON_LOGOUT_IN_PERS_ACC = [By.XPATH, "//button[contains(text(), 'Выход')]"]   # кн "Выход" в личном кабинете
    LINK_CONSTRUCTOR = [By.LINK_TEXT, "Конструктор"]   # линк "Конструктор"
    LOGO_STELLAR_BURGERS = [By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]"]   # логотип
    ERROR_INCORRECT_PASSWORD = [By.XPATH, "//*[contains(text(), 'Некорректный пароль')]"]   # некорректный пароль
    LINK_SAUCES = [By.XPATH, "//span[contains(text(), 'Соусы')]"]   # линк вкладки "Соусы"
    LIST_OF_SAUCES_CARDS = [By.XPATH, "//section[1]/div[2]/ul[2]"]   # список карточек соусов
    LAST_SAUCES_CARD = [By.XPATH, "//*[contains(text(), 'Соус с шипами Антарианского плоскоходца')]"]   # последняя карточка соусов
    LAST_SAUCES_CARD_IMG = [By.XPATH, "//section[1]/div[2]/ul[2]/a[4]/img" ]  # изображение последней карточки соусов
    LINK_INPUTS = [By.XPATH, "//span[contains(text(), 'Начинки')]"]   # линк вкладки "Начинки"
    LIST_OF_INPUTS_CARDS = [By.XPATH, "//section[1]/div[2]/ul[3]"]   # список карточек начинок
    LAST_INPUTS_CARD = [By.XPATH, "//*[contains(text(), 'Сыр с астероидной плесенью')]"]   # последняя карточка начинок
    LAST_INPUT_CARD_IMG = [By.XPATH, "//section[1]/div[2]/ul[3]/a[9]/img"]   # изображение последней карточки начинок
    LINK_BREADS = [By.XPATH, "//span[contains(text(), 'Булки')]"]   # линк вкладки "Булки"
    LIST_OF_BREADS_CARDS = [By.XPATH, "//section[1]/div[2]/ul[1]"]   # список карточек булок
    LAST_BREAD_CARD = [By.XPATH, "//section[1]/div[2]/ul[1]/a[2]/p"]   # последняя карточка булок
    LAST_BREAD_CARD_IMG = [By.XPATH, "//section[1]/div[2]/ul[1]/a[2]/img"]   # изображение последней карточки булок
    BUTTON_CONSTRUCTOR = [By.XPATH, "//*[contains(text(), 'Конструктор')]"]   # кн "Конструктор"



# ".//input[@class='text input__textfield text_type_main-default']")[0]   # поле ввода имени в форме регистрации
# ".//input[@class='text input__textfield text_type_main-default']")[1]   # поле ввода мейла в форме регистрации
# ".//input[@class='text input__textfield text_type_main-default' and @type='password']")   # поле ввода пароля в форме регистрации


#LONG_XPATH_FOR FIELDS = ((.//input[@class="text input__textfield text_type_main-default"])[2])') # поле ввода