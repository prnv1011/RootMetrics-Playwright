from pages.help_page import HelpPage
from pages.overall_summary_page import OverallSummaryPage


def test_help_functionality(page, valid_login):
    overall_summary_page = OverallSummaryPage(page)
    help_page = HelpPage(page)
    overall_summary_page.handle_welcome_popup()
    overall_summary_page.click_user_menu()
    help_page.click_help()
    help_links = [
        (help_page.award_view_summary_btn, help_page.summary_title),
        (help_page.access_export_btn, help_page.access_export_title),
        (help_page.operator_btn, help_page.operator_title),
        (help_page.market_btn, help_page.market_title),
        (help_page.defining_points_btn, help_page.defining_points_title),
        (help_page.rootscore_and_ranks_btn, help_page.rootscore_and_ranks_title),
        (help_page.point_analysis_btn, help_page.point_analysis_title),
        (help_page.metrics_btn, help_page.metrics_title),
        (help_page.measuring_btn, help_page.measuring_title),
        (help_page.charts_btn, help_page.charts_title),
        (help_page.figures_btn, help_page.figures_title),
        (help_page.comparability_btn, help_page.comparability_title),
        (help_page.terms_btn, help_page.terms_title)
    ]
    for button, title in help_links:
        help_page.verify_help_page(button, title)


from pages.help_page import HelpPage
from pages.overall_summary_page import OverallSummaryPage


def test_help_functionality(page, valid_login):
    overall_summary_page = OverallSummaryPage(page)
    help_page = HelpPage(page)
    overall_summary_page.handle_welcome_popup()
    overall_summary_page.click_user_menu()
    help_page.click_help()
    help_links = [
        (help_page.award_view_summary_btn, help_page.summary_title),
        (help_page.access_export_btn, help_page.access_export_title),
        (help_page.operator_btn, help_page.operator_title),
        (help_page.market_btn, help_page.market_title),
        (help_page.defining_points_btn, help_page.defining_points_title),
        (help_page.rootscore_and_ranks_btn, help_page.rootscore_and_ranks_title),
        (help_page.point_analysis_btn, help_page.point_analysis_title),
        (help_page.metrics_btn, help_page.metrics_title),
        (help_page.measuring_btn, help_page.measuring_title),
        (help_page.charts_btn, help_page.charts_title),
        (help_page.figures_btn, help_page.figures_title),
        (help_page.comparability_btn, help_page.comparability_title),
        (help_page.terms_btn, help_page.terms_title)
    ]
    for button, title in help_links:
        help_page.verify_help_page(button, title)
