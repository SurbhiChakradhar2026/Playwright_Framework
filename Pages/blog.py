class Blog:
    def __init__(self,page):
        self.page=page
        self.blog=page.locator('(//a[text()="Blog"])[1]')
        self.ad=page.locator('(//a[text()="App Development"])[1]')
        self.wd=page.locator('(//a[text()="Web Development"])[1]')
        self.sd=page.locator('(//a[text()="Software Development"])[1]')
        self.digim=page.locator('(//a[text()="Digital Marketing"])[1]')
        self.emailm=page.locator('(//a[text()="Email Marketing"])[1]')
        self.blog_ai=page.locator('//a[@href="/blog/category/artificial-intelligence/"]')
        self.uiux=page.locator('(//a[text()="UI UX Design"])[1]')
        
        self.blog_cat=[self.ad,self.wd,self.sd,self.digim,self.emailm,self.blog_ai,self.uiux]
    def blog_options(self):
        for i in self.blog_cat:
            self.blog.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
       

     
    
        

      