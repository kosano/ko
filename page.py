
class Page:
    def __init__(self,list_count,current_page,page_list_num=10,page_num=7):
        #总条数
        self.list_count = list_count
        #每页显示的数据条数
        self.page_list_num = page_list_num
        #显示的页码
        self.page_num = page_num
        #当前页数
        if current_page<1:
            self.current_page = 1
        elif current_page>self.page_count:
            self.current_page = self.page_count
        else:
            self.current_page = current_page
    

    @property
    def page_count(self):
        p,x = divmod(self.list_count,self.page_list_num)
        if x:
            return p+1
        else:
            return p
    @property
    def start(self):
        """开始条数"""
        return int((self.current_page-1)*self.page_list_num)
        
    @property
    def end(self):
        """结束条数"""
        return int(self.start + self.page_list_num + 1)
        
    @property
    def start_page(self):
        """开始页数"""
        if self.current_page - (self.page_num-1)/2 < 1:
            return 1
        else:
            return int(self.current_page - (self.page_num-1)/2)
            
    @property
    def end_page(self):
        """结束页数"""
        if self.current_page + (self.page_num-1)/2 > self.page_count:
            return self.page_count
        else:
            return int(self.current_page + (self.page_num-1)/2)
    
    def page_str(self,url):
        self.page_html = []
        if self.page_count <= self.page_num:
            for i in range(1,self.page_count+1):
                if i == self.current_page:
                    a_tag = '<a class="active" href="%s?p=%s">%s</a>' % (url,i,i)
                    self.page_html.append(a_tag)
                else:
                    a_tag = '<a href="%s?p=%s">%s</a>' % (url,i,i)
                    self.page_html.append(a_tag)
        else:
            for i in range(self.start_page,self.end_page+1):
                if i == self.current_page:
                    a_tag = '<a class="active" href="%s?p=%s">%s</a>' % (url,i,i)
                    self.page_html.append(a_tag)
                else:
                    a_tag = '<a href="%s?p=%s">%s</a>' % (url,i,i)
                    self.page_html.append(a_tag)

            if self.start_page > 2:
                self.page_html.insert(0,'<a>...</a>')
            if self.start_page - 1 >= 1:
                self.page_html.insert(0,'<a href="%s?p=%s">%s</a>' % (url,1,1))

            
            if self.end_page < self.page_count - 2:
                self.page_html.append('<a>...</a>')
            if self.end_page + 1 == self.page_count -1:
                self.page_html.append('<a href="%s?p=%s">%s</a>' % (url,self.page_count-1,self.page_count-1))
            if self.end_page <= self.page_count - 1:
                self.page_html.append('<a href="%s?p=%s">%s</a>' % (url,self.page_count,self.page_count))

        self.page_html.insert(0,'<a href="%s?p=%s">%s</a>' % (url,1 if self.current_page==1 else self.current_page-1,'上一页'))
        self.page_html.append('<a href="%s?p=%s">%s</a>' % (url,self.page_count if self.current_page==self.page_count else self.current_page+1,'下一页'))

        return self.page_html
            
            


    