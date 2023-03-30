from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tool


# Create your views here.
class IndexView(LoginRequiredMixin, ListView):
    model = Tool
    template_name = "tool/index.html"
    context_object_name = "tool_items"
    paginate_by = 5
    login_url = '/admin/login'

    def get_context_data(self, **kwargs):
        """
        """

        # 首先获得父类生成的传递给模板的字典。
        context = super().get_context_data(**kwargs)

        # 父类生成的字典中已有 paginator、page_obj、is_paginated 这三个模板变量，
        # paginator 是 Paginator 的一个实例，
        # page_obj 是 Page 的一个实例，
        # is_paginated 是一个布尔变量，用于指示是否已分页。
        # 例如如果规定每页 10 个数据，而本身只有 5 个数据，其实就用不着分页，此时 is_paginated=False。
        # 由于 context 是一个字典，所以调用 get 方法从中取出某个键对应的值。
        # paginator = context.get("paginator")
        # page = context.get("page_obj")
        # is_paginated = context.get("is_paginated")
        #
        # # 调用自己写的 pagination_data 方法获得显示分页导航条需要的数据，见下方。
        # pagination_data = self.pagination_data(paginator, page, is_paginated)
        #
        # # 将分页导航条的模板变量更新到 context 中，注意 pagination_data 方法返回的也是一个字典。
        # context.update(pagination_data)

        # 将更新后的 context 返回，以便 ListView 使用这个字典中的模板变量去渲染模板。
        # 注意此时 context 字典中已有了显示分页导航条所需的数据。
        return context
