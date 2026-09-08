class ContactUs:
    def __init__(self,page):
        self.page=page
        self.contact_us=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.textName=page.locator('(//input[@name="name"])[2]')
        self.email=page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.otpbtn=page.locator('(//button[text()="Send OTP"])[2]')
        self.textOtp=page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.companyDetails=page.locator('(//input[@name="company"])[2]')
        self.service=page.locator('(//select[@name="service"])[2]')
        self.phno=page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.msg=page.locator('(//textarea[@placeholder="Message"])[2]')
        # webdevelopment options 
        self.web_dev= page.locator('//a[text()="Web Development"]')
        self.ecom_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]')
        self.cust_web_portal_dev=page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
        self.web_development_list = [self.web_dev,self.ecom_dev,self.cust_web_portal_dev]
    # ecom_arrow=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]')
        self.ecom_arrow=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]')
        self.page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]')
        self.andriodapp_dropdown_arrow=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]')
        self.andriod_app_dev_dropdown=page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
        self.app_dev_dropdown=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')
    # App Development
        self.app_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[1]')
        self.ios_app_dev= page.locator('(//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"])[1]')
        self.apd=page.locator('(//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"])[1]')
        self.hmda=page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.cpad=page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.pwad=page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')
        self.gd=page.locator('//a[@href="https://www.tranktechnologies.com/graphic-design-company"]')
        self.bd=page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.pd=page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.bcd=page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')
        self.appDevelopment_list = [self.app_dev,self.ios_app_dev,self.apd,self.hmda,self.cpad,self.pwad]
        self.uiuxd=page.locator('//a[text()="UI UX Design"]')
        self.mad=page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.rwd=page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.bid=page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')
        self.graphicsDesign_list=[self.gd,self.bd,self.pd,self.bcd,self.uiuxd,self.mad,self.rwd,self.bid]

        #Social media Links
        self.fb=page.locator('//img[@alt="Facebook"]')
        self.lin=page.locator('//img[@alt="LinkedIn"]')
        self.insta=page.locator('(//img[@alt="Instagram"])[1]')
        self.pintrest=page.locator('(//img[@alt="Instagram"])[2]')
        self.tweet=page.locator('//img[@alt="Twitter"]')
        self.youtube=page.locator('//img[@alt="Youtube"]')
        self.quora=page.locator('//img[@alt="Quora"]')
        self.socialMedia_list = [self.fb,self.lin,self.insta,self.pintrest,self.tweet,self.youtube,self.quora]
    def formDetails(self):
        self.contact_us.click()
        self.textName.fill("Surbhi Chakradhar")
        self.email.fill("chakradhar.surbhi@outlook.com")
        self.otpbtn.click()
        self.page.wait_for_timeout(6000)
        self.page.once("dialog", lambda dialog: dialog.accept())
        
        self.textOtp.fill("123456")
        self.companyDetails.fill("Uncodemy")
        self.service.select_option("Graphic Design")
        self.phno.fill("1234567890")
        self.msg.fill("Hello, there is playwright script running")
        
    def webdevelopmentLinks(self):
        for i in self.web_development_list:
            self.contact_us.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def appDevelopment(self):
        for i in self.appDevelopment_list:
            self.contact_us.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def graphichDesign(self):
        for i in self.graphicsDesign_list:
            self.contact_us.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def socialMedia_Links(self):
        self.contact_us.click()
        self.page.wait_for_load_state(state="load")
        for i in self.socialMedia_list:
            with self.page.context.expect_page() as new_page_info:
                i.click()
            new_tab = new_page_info.value
            new_tab.wait_for_load_state("load")
            new_tab.close()