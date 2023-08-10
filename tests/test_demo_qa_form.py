from selene import be, have, browser


def test_student_sign_up():
    browser.open('automation-practice-form')

    browser.element('#firstName').type('Jack')
    browser.element('#lastName').type('Sparrow')
    browser.element('#userEmail').type('Jack@pirate.com')

    browser.element('#gender-radio-1').with_(timeout=browser.config.timeout * 1.5).click()
