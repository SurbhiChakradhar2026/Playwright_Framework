class vertical:
    def __init__(self,page):
       self.page=page
       #Verticals mouse hover
       self.ver=page.locator('(//a[text()="Verticals"])[1]')
       #inside verticals options trading 
       self.trade=page.locator('//strong[text()="Trading"]')
       
       #inside trading tanding options 
       self.trade_1=page.locator('(//a[text()="Stock Trading"])[1]')
       self.trade_2=page.locator('(//a[text()="Paper Trading"])[1]')
       self.trade_3=page.locator('(//a[text()="CFD Trading"])[1]')
       self.trade_4=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
       self.trade_5=page.locator('(//a[text()="Algo Trading"])[1]')
       self.trade_6=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
       self.trade_7=page.locator('(//a[text()="Web Portal Trading"])[1]')
       self.trade_list = [self.trade_1,self.trade_2,self.trade_3,self.trade_4,self.trade_5,self.trade_6,self.trade_7]
       #inside trading Retails and Ecommerce
       self.re=page.locator('//strong[text()="Retail and Ecommerce"]')
       #Retails and Ecommerce suboptions
       self.re_1=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
       self.re_2=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
       self.re_list=[self.re_1,self.re_2]
       #Healthcare
       self.hc=page.locator('//strong[text()="Healthcare"]')
       self.hc_1=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
       self.hc_2=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
       self.hc_list=[self.hc_1,self.hc_2]

       #fintech
       self.fin= page.locator('//strong[text()="Fintech"]')
       self.fin_1=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
       self.fin_2=page.locator('(//a[text()="Crypto"])[1]')
       self.fin_list=[self.fin_1,self.fin_2]
       #custom app
       self.cust=page.locator('//strong[text()="Custom App"]')
       self.cust_1=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
       self.cust_2=page.locator('(//a[text()="HRM Development"])[1]')
       self.cust_3=page.locator('(//a[text()="Travel"])[1]')
       self.cust_4=page.locator('(//a[text()="Dating App Development"])[1]')
       self.cust_5=page.locator('(//a[text()="CRM Development USA"])[1]')
       self.cust_6=page.locator('(//a[text()="CRM Development"])[1]')
       self.cust_7=page.locator('(//a[text()="ERP App Development"])[1]')
       self.cust_8=page.locator('(//a[text()="E-Learning"])[1]')
       self.cust_9=page.locator('(//a[text()="Real Estate"])[1]')
       self.Cust_list=[self.cust_1,self.cust_2,self.cust_3,self.cust_4,self.cust_5,self.cust_6,self.cust_7,self.cust_8,self.cust_9]

    #Methods for all options in verticals 
    #    
    def trading_options(self):
        for i in self.trade_list:
            self.ver.hover()
            self.trade.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def retail_ecommerce_options(self):
        for i in self.re_list:
            self.ver.hover()
            self.re.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def healthcare_options(self):
        for i in self.hc_list:
            self.ver.hover()
            self.hc.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def fintech_options(self):
        for i in self.fin_list:
            self.ver.hover()
            self.fin.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def custom_app_options(self):
        for i in self.Cust_list:
            self.ver.hover()
            self.cust.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
