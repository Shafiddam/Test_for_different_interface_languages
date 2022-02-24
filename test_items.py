from selenium.webdriver.common.by import By


def test_can_add_product_to_basket(browser):
    """
    Тест, что страница товара на сайте содержит кнопку добавления в корзину.
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"), "BUTTON ADD TO BASKET IS NOT PRESENTED..."

