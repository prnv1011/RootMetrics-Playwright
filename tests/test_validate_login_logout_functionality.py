from pages.overall_summary_page import OverallSummaryPage


def test_login_logout_flow(valid_login):
    overall_summary_page = OverallSummaryPage(valid_login)
    overall_summary_page.verify_summary_page_title()
    overall_summary_page.handle_welcome_popup()
    overall_summary_page.click_user_menu()
    overall_summary_page.click_logout()
    overall_summary_page.verify_login_page_title()


from pages.overall_summary_page import OverallSummaryPage


def test_login_logout_flow(valid_login):
    overall_summary_page = OverallSummaryPage(valid_login)
    overall_summary_page.verify_summary_page_title()
    overall_summary_page.handle_welcome_popup()
    overall_summary_page.click_user_menu()
    overall_summary_page.click_logout()
    overall_summary_page.verify_login_page_title()
