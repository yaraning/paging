from django.utils.safestring import mark_safe
class Pagination:

    def __init__(self, page_now, total_data,url, per_data=10, max_show=11):
        try:
            self.page_now = int(page_now)
            if self.page_now < 1:
                self.page_now = 1
        except Exception as e:
            self.page_now = 1
        self.url = url
        #每页显示的数据量
        self.per_data = per_data
        # 总数据量
        self.total_data = total_data
        # 总页数
        self.page_num, more = divmod(self.total_data, self.per_data)
        if more:
            self.page_num += 1
        # 一次最多显示页数
        self.max_show = max_show
    @property
    def start(self):
        return (self.page_now - 1) * self.per_data

    @property
    def end(self):
        return self.page_now * self.per_data

    @property
    def page_html(self):

        half = self.max_show // 2
        #起始页
        start_page = self.page_now - half
        #终止页
        end_page = self.page_now + half

        if self.page_num <= self.max_show:
            start_page = 1
            end_page = self.page_num
        elif start_page < 1:
            start_page = 1
            end_page = self.max_show
        elif end_page > self.page_num:
            end_page = self.page_num
            start_page = self.page_num - self.max_show + 1

        li_list = []
        if self.page_now == 1:
            li_list.append('<li class="disabled"><a>上一页</a></li>')
        else:
            self.url['page'] = self.page_now - 1
            li_list.append('<li><a href="?{}">上一页</a></li>'.format(self.url.urlencode()))
        for num in range(start_page, end_page + 1):
            self.url['page'] = num
            if num == self.page_now:
                li_list.append('<li class="active"><a href="?{}">{}</a></li>'.format(self.url.urlencode(), num))
            else:
                li_list.append('<li><a href="?{}">{}</a></li>'.format(self.url.urlencode(), num))

        if self.page_now == self.page_num:
            li_list.append('<li class="disabled"><a>下一页</a></li>')
        else:
            self.url['page'] = self.page_now + 1
            li_list.append('<li><a href="?{}">下一页</a></li>'.format(self.url.urlencode()))

        li_list = ''.join(li_list)
        return mark_safe(li_list)


