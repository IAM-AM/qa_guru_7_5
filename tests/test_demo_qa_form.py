from selene import browser, command, have
from selenium.webdriver import Keys
import os


def test_student_sign_up():
    browser.open('automation-practice-form')

    browser.element('#firstName').type('Jack')
    browser.element('#lastName').type('Sparrow')
    browser.element('#userEmail').type('Jack@pirate.com')
    browser.element('#userNumber').type('+9901234567890')

    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
    browser.element('select[class="react-datepicker__year-select"]').click().element(
        'option[value="1900"]').click()
    browser.element('select[class="react-datepicker__month-select"]').click().element(
        'option[value="5"]').click()
    browser.element('div[class="react-datepicker__day react-datepicker__day--020"]').click()


    browser.element('#subjectsInput').type('Economics').press_tab()
    browser.element('label[for="hobbies-checkbox-2"]').click()


