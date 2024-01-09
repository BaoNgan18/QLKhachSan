from wtforms import SelectField, FileField
from wtforms.validators import InputRequired

from app import app, db, dao
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from app.models import Category, Room, UserRoleEnum
from flask_login import logout_user, current_user
from flask import redirect, request
from wtforms import SelectField, FileField
from wtforms.validators import InputRequired


class AdminIndex(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


admin = Admin(app=app, name='QUAN LY KHACH SAN', template_mode='bootstrap4', index_view=AdminIndex())


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class RoomView(AuthenticatedAdmin):
    column_list = ['id', 'name', 'category']
    column_searchable_list = ['name']
    column_filters = ['name', 'category_id']
    column_exclude_list = ['image']
    column_labels = {
        'id': 'Mã phòng',
        'name': 'Tên phòng',
        'category': 'Tên loại phòng'
    }
    can_export = True
    can_view_details = True
    can_edit = True
    details_modal = True
    edit_modal = True


class CategoryView(AuthenticatedAdmin):
    column_list = ['id', 'name', 'description', 'price']
    column_searchable_list = ['name']
    column_filters = ['name']
    can_export = True
    can_view_details = True
    can_edit = True


class StatsView(AuthenticatedUser):
    @expose("/")
    def index(self):
        # kw = request.args.get("kw")
        return self.render('admin/stats.html')
                           # stats=dao.revenue_stats(kw),
                           # month_stats=dao.revenue_stats_by_month())


class LogoutView(AuthenticatedUser):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/admin')


admin.add_view(CategoryView(Category, db.session, name='Danh mục'))
admin.add_view(RoomView(Room, db.session, name='Phòng'))
admin.add_view(StatsView(name='Thống kê báo cáo'))
admin.add_view(LogoutView(name='Đăng xuất'))
