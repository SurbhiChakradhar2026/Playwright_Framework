class Portfolio:
    def __init__(self,page):
        self.page=page
        self.protfolio=page.locator('//a[text()="Portfolio"]')
        self.viewmore1=page.locator('(//a[text()="View More"])[1]')
        self.viewmore2=page.locator('(//a[text()="View More"])[2]')
        self.viewmore3=page.locator('(//a[text()="View More"])[3]')
        self.viewmore4=page.locator('(//a[text()="View More"])[4]')
        #self.viewmore5=page.locator('(//a[text()="View More"])[5]')
        self.viewmore6=page.locator('(//a[text()="View More"])[6]')

        self.viewMore_list = [self.viewmore1,self.viewmore2,self.viewmore3,self.viewmore4,self.viewmore6]

    def viewMore_click(self):
          
        self.protfolio.click()
        for i in self.viewMore_list:
            i.click()
            with self.page.context.expect_page() as new_page_info:
                new_tab = new_page_info.value
                new_tab.wait_for_load_state("load")
                new_tab.close()

            