from playwright.sync_api import expect

from utils.logger import logger


class HelpPage:
    def __init__(self, page):
        self.page = page
        self.help_dropdown_button = self.page.locator("a[ng-click='showHelp()']:visible")

        self.award_view_summary_btn = self.page.locator("li:has(a[href='#summary'])")
        self.summary_title = self.page.locator("h2#summary").nth(0)

        self.access_export_btn = self.page.locator("li:has(a[href='#file-access-export'])")
        self.access_export_title = self.page.locator("h2#file-access-export")

        self.operator_btn = self.page.locator("li:has(a[href='#operator'])")
        self.operator_title = self.page.locator("h2#operator")

        self.market_btn = self.page.locator("li:has(a[href='#market'])")
        self.market_title = self.page.locator("h2#market")

        self.defining_points_btn = self.page.locator("li:has(a[href='#defining-points'])")
        self.defining_points_title = self.page.locator("h2#defining-points")

        self.rootscore_and_ranks_btn = self.page.locator("li:has(a[href='#rootscore-and-ranks'])")
        self.rootscore_and_ranks_title = self.page.locator("h2#rootscore-and-ranks")

        self.point_analysis_btn = self.page.locator("li:has(a[href='#point-analysis'])")
        self.point_analysis_title = self.page.locator("h2#point-analysis")

        self.metrics_btn = self.page.locator("li:has(a[href='#metrics'])")
        self.metrics_title = self.page.locator("h2#metrics")

        self.measuring_btn = self.page.locator("li:has(a[href='#measuring'])")
        self.measuring_title = self.page.locator("h2#measuring")

        self.charts_btn = self.page.locator("li:has(a[href='#charts'])")
        self.charts_title = self.page.locator("h2#charts")

        self.figures_btn = self.page.locator("li:has(a[href='#figures'])")
        self.figures_title = self.page.locator("h2#figures")

        self.comparability_btn = self.page.locator("li:has(a[href='#comparability'])")
        self.comparability_title = self.page.locator("h2#comparability")

        self.terms_btn = self.page.locator("li:has(a[href='#terms'])")
        self.terms_title = self.page.locator("h2#terms")

    def click_help(self):
        self.help_dropdown_button.click()

    def verify_help_page(self, button, title):
        button.click()
        expect(title).to_be_visible()
        logger.info(f"Clicked {button.inner_text()}, {title.inner_text()} is visible")