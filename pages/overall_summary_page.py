from playwright.sync_api import expect

from utils.logger import logger


class OverallSummaryPage():
    def __init__(self, page):
        self.page = page
        self.summary_title = "RootInsights"
        self.login_page_title = "Sign In"
        self.user_menu_dropdown = self.page.locator("a.dropdown-toggle").nth(3)
        self.logout_button = self.page.locator("a[ng-click='logout()']").nth(0)
        self.welcome_popup = self.page.locator("div.col-md-offset-2").filter(has_text='Welcome to RootInsights')
        self.welcome_popup_close_button = self.page.locator("div.modal-content:visible").filter(has_text="Welcome to RootInsights").locator("button.close")
        self.carriers_button = self.page.locator('button.carriers')
        self.overall_btn = self.page.locator("a[ng-click='updateScoreType(st)']").nth(0)
        self.reliability_btn = self.page.locator("a[ng-click='updateScoreType(st)']").nth(1)
        self.responsiveness_btn = self.page.locator("a[ng-click='updateScoreType(st)']").nth(2)
        self.speed_btn = self.page.locator("a[ng-click='updateScoreType(st)']").nth(3)
        self.data_btn = self.page.locator("a[ng-click='updateScoreType(st)']").nth(4)
        self.call_btn = self.page.locator("a[ng-click='updateScoreType(st)']").nth(5)
        self.text_btn = self.page.locator("a[ng-click='updateScoreType(st)']").nth(6)
        self.video_btn = self.page.locator("a[ng-click='updateScoreType(st)']").nth(7)
        self.quality_param_title = self.page.locator("h2.ng-binding")
        self.carrier_att = self.page.locator("button.att")
        self.carrier_verizon = self.page.locator("button.verizon")
        self.carrier_tmobile = self.page.locator("button.tmobile")
        self.download_dropdown = self.page.locator('div.download:visible')
        self.export_all_rb = self.page.locator("input#radio-all")
        self.export_view_rb = self.page.locator("input#radio-view")
        self.download_btn = self.page.locator("button.btn-default").filter(has_text="Download")
        self.att_bar = self.page.locator('g.bars').locator('g.att')
        self.tmobile_bar = self.page.locator('g.bars').locator('g.tmobile')
        self.verizon_bar = self.page.locator('g.bars').locator('g.verizon')
        # self.completed_markets_checkbox = self.page.locator("label[for='incomplete-toggle2']").nth(1)
        self.completed_markets_checkbox = self.page.locator("input#incomplete-toggle2").nth(0)
        self.previous = self.page.locator("td.previous-winners")
        self.current = self.page.locator("td.current-winners")

    def click_user_menu(self):
        self.user_menu_dropdown.click()

    def click_logout(self):
        self.logout_button.click()
        logger.info("Logged out successfully")

    def verify_summary_page_title(self):
        expect(self.page).to_have_title(self.summary_title)
        logger.info("Summary title verified")

    def verify_login_page_title(self):
        expect(self.page).to_have_title(self.login_page_title)
        logger.info("Login page title verified")

    def handle_welcome_popup(self):
        #if self.welcome_popup.is_visible():
        self.welcome_popup_close_button.click()

    def click_and_verify_overall(self):
        self.overall_btn.click()
        expect(self.quality_param_title).to_contain_text("Overall Performance")
        logger.info("Clicked on Overall, Title verified successfully")

    def click_and_verify_reliability(self):
        self.reliability_btn.click()
        expect(self.quality_param_title).to_contain_text("Network Reliability")
        logger.info("Clicked on Reliability, Title verified successfully")

    def click_and_verify_responsiveness(self):
        self.responsiveness_btn.click()
        expect(self.quality_param_title).to_contain_text("Responsiveness")
        logger.info("Clicked on Responsiveness, Title verified successfully")

    def click_and_verify_speed(self):
        self.speed_btn.click()
        expect(self.quality_param_title).to_contain_text("Network Speed")
        logger.info("Clicked on Speed, Title verified successfully")

    def click_and_verify_data(self):
        self.data_btn.click()
        expect(self.quality_param_title).to_contain_text("Data Performance")
        logger.info("Clicked on Data, Title verified successfully")

    def click_and_verify_call(self):
        self.call_btn.click()
        expect(self.quality_param_title).to_contain_text("Call Performance")
        logger.info("Clicked on Call, Title verified successfully")

    def click_and_verify_text(self):
        self.text_btn.click()
        expect(self.quality_param_title).to_contain_text("Text Performance")
        logger.info("Clicked on Text, Title verified successfully")

    def click_and_verify_video(self):
        self.video_btn.click()
        expect(self.quality_param_title).to_contain_text("Video Performance")
        logger.info("Clicked on Video, Title verified successfully")

    def verify_att_carrier_presence(self):
        expect(self.carrier_att).to_be_visible()
        logger.info("AT&T carrier is present")

    def verify_tmobile_carrier_presence(self):
        expect(self.carrier_tmobile).to_be_visible()
        logger.info("T-Mobile carrier is present")

    def verify_verizon_carrier_presence(self):
        expect(self.carrier_verizon).to_be_visible()
        logger.info("Verizon carrier is present")

    def click_export_all(self):
        self.export_all_rb.click()

    def click_export_view(self):
        self.export_view_rb.click()

    def click_download_dropdown(self):
        self.download_dropdown.click()

    def download_file(self):
        with self.page.expect_download() as download_info:
            self.download_btn.click()
        download = download_info.value
        logger.info("Successfully downloaded the file")
        return download

    def click_att_carrier(self):
        self.att_bar.click()
        expect(self.att_bar).to_contain_class("clicked")
        expect(self.att_bar.locator("rect.bg")).to_have_css("stroke-width", "1px")
        logger.info("AT&T Bar is highlighted")

    def click_tmobile_carrier(self):
        self.tmobile_bar.click()
        expect(self.tmobile_bar).to_contain_class("clicked")
        expect(self.tmobile_bar.locator("rect.bg")).to_have_css("stroke-width", "1px")
        logger.info("T-Mobile Bar is highlighted")

    def click_verizon_carrier(self):
        self.verizon_bar.click()
        expect(self.verizon_bar).to_contain_class("clicked")
        expect(self.verizon_bar.locator("rect.bg")).to_have_css("stroke-width", "1px")
        logger.info("Verizon Bar is highlighted")

    def click_and_verify_completed_market_checkbox(self):
        if self.completed_markets_checkbox.is_checked():
            pass
        else:
            self.completed_markets_checkbox.click()

    def verify_completed_markets(self):
        rows = self.page.locator("table.main tbody tr")
        for i in range(rows.count()):
            row = rows.nth(i)
            expect(row.locator("td.previous-winners")).not_to_contain_text("Not available")
            expect(row.locator("td.current-winners")).not_to_contain_text("Not available")
