class Selectors:
    # Logging in
    LOGIN_BUTTON = "#gnav-main-container > div > div > div.css-9qge8r.e37uo190 > div.css-chsy6r.e37uo190 > div.css-1ble2gn.eu4oa1w0 > a"
    EMAIL_INPUT = "#ifl-InputFormField-3"
    EMAIL_CONTINUE_BUTTON = "#emailform > button"
    LOGIN_WITH_PASSWORD_LINK = "#auth-page-google-password-fallback"
    PASSWORD_INPUT = "#ifl-InputFormField-156"
    SIGN_IN_BUTTON = "#loginform > button"

    # hCaptcha check
    LOGIN_BUTTON_HCAPTCHA = "#anchor"
    LOGIN_HCAPTCHA_IFRAME = "#emailform > div.pass-Captcha.css-1lbfmuq.eu4oa1w0 > div > iframe"
    PASSWORD_HCAPTCHA_IFRAME = "#loginform > div.pass-Captcha.css-1lbfmuq.eu4oa1w0 > div:nth-child(1) > iframe"
    HCAPTCHA_CHECKBOX = "#checkbox"

    # Job search
    KEYWORDS_SEARCH_INPUT = "#text-input-what"
    LOCATION_SEARCH_INPUT = "#text-input-where"
    JOB_SEARCH_BUTTON = "#jobsearch > button"

    # Job alert popup
    JOB_ALERT_POPUP = "#mosaic-desktopserpjapopup"
    JOB_ALERT_POPUP_CLOSE = "#mosaic-desktopserpjapopup > div.css-otmc9o.eu4oa1w0 > button > svg"