class Selectors:
    # Login check element
    LOGIN_CHECK_ELEMENT = "#gnav-main-container > div > div > div.css-9qge8r.e37uo190 > div.css-chsy6r.e37uo190 > div.css-1ble2gn.eu4oa1w0 > a"

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

    # Job search settings
    KEYWORDS_SEARCH_INPUT = "#text-input-what"
    LOCATION_SEARCH_INPUT = "#text-input-where"
    JOB_SEARCH_BUTTON = "#jobsearch > button"

    DATE_POSTED_DROPDOWN_MENU = "#filter-dateposted"
    DATE_POSTED_DROPDOWN_OPTION1 = "#filter-dateposted-menu > li:nth-child(1) > a" # Last 24 hours
    DATE_POSTED_DROPDOWN_OPTION2 = "#filter-dateposted-menu > li:nth-child(2) > a" 
    DATE_POSTED_DROPDOWN_OPTION3 = "#filter-dateposted-menu > li:nth-child(3) > a"
    DATE_POSTED_DROPDOWN_OPTION4 = "#filter-dateposted-menu > li:nth-child(4) > a"
    DATE_POSTED_DROPDOWN_OPTIONS = [DATE_POSTED_DROPDOWN_OPTION1, DATE_POSTED_DROPDOWN_OPTION2, 
                                    DATE_POSTED_DROPDOWN_OPTION3, DATE_POSTED_DROPDOWN_OPTION4]

    DISTANCE_DROPDOWN_MENU = "#filter-radius"
    DISTANCE_DROPDOWN_OPTION1 = "#filter-radius-menu > li:nth-child(1) > a"
    DISTANCE_DROPDOWN_OPTION2 = "#filter-radius-menu > li:nth-child(2) > a" # Within 5 kilometres
    DISTANCE_DROPDOWN_OPTION3 = "#filter-radius-menu > li:nth-child(3) > a"
    DISTANCE_DROPDOWN_OPTION4 = "#filter-radius-menu > li:nth-child(4) > a"
    DISTANCE_DROPDOWN_OPTION5 = "#filter-radius-menu > li:nth-child(5) > a"
    DISTANCE_DROPDOWN_OPTION6 = "#filter-radius-menu > li:nth-child(6) > a"
    DISTANCE_DROPDOWN_OPTION7 = "#filter-radius-menu > li:nth-child(7) > a"
    DISTANCE_DROPDOWN_OPTION8 = "#filter-radius-menu > li:nth-child(8) > a"
    DISTANCE_DROPDOWN_OPTIONS = [DISTANCE_DROPDOWN_OPTION1, DISTANCE_DROPDOWN_OPTION2, DISTANCE_DROPDOWN_OPTION3,
                                 DISTANCE_DROPDOWN_OPTION4, DISTANCE_DROPDOWN_OPTION5, DISTANCE_DROPDOWN_OPTION6,
                                 DISTANCE_DROPDOWN_OPTION7, DISTANCE_DROPDOWN_OPTION8]

    JOB_TYPE_DROPDOWN_MENU = "#filter-jobtype"
    JOB_TYPE_DROPDOWN_OPTION1 = "#filter-jobtype-menu > li:nth-child(1) > a"
    JOB_TYPE_DROPDOWN_OPTION2 = "#filter-jobtype-menu > li:nth-child(2) > a"
    JOB_TYPE_DROPDOWN_OPTION3 = "#filter-jobtype-menu > li:nth-child(3) > a"
    JOB_TYPE_DROPDOWN_OPTION4 = "#filter-jobtype-menu > li:nth-child(4) > a"
    JOB_TYPE_DROPDOWN_OPTION5 = "#filter-jobtype-menu > li:nth-child(5) > a"
    JOB_TYPE_DROPDOWN_OPTION6 = "#filter-jobtype-menu > li:nth-child(6) > a"
    JOB_TYPE_DROPDOWN_OPTION7 = "#filter-jobtype-menu > li:nth-child(7) > a"
    JOB_TYPE_DROPDOWN_OPTION8 = "#filter-jobtype-menu > li:nth-child(8) > a"
    JOB_TYPE_DROPDOWN_OPTION9 = "#filter-jobtype-menu > li:nth-child(9) > a"
    JOB_TYPE_DROPDOWN_OPTIONS = [JOB_TYPE_DROPDOWN_OPTION1, JOB_TYPE_DROPDOWN_OPTION2, JOB_TYPE_DROPDOWN_OPTION3,
                                 JOB_TYPE_DROPDOWN_OPTION4, JOB_TYPE_DROPDOWN_OPTION5, JOB_TYPE_DROPDOWN_OPTION6,
                                 JOB_TYPE_DROPDOWN_OPTION7, JOB_TYPE_DROPDOWN_OPTION8, JOB_TYPE_DROPDOWN_OPTION9]

    # Job alert popup
    JOB_ALERT_POPUP = "#mosaic-desktopserpjapopup"
    JOB_ALERT_POPUP_CLOSE = "#mosaic-desktopserpjapopup > div.css-otmc9o.eu4oa1w0 > button > svg"

    # Job list navigation
    JOB_SEARCH_LEFT_PANE = "#jobsearch-JapanPage > div > div > div.css-hyhnne.e37uo190 > div.jobsearch-LeftPane"