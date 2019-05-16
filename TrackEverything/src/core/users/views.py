from . import user
from flask import abort, flash, redirect, render_template, url_for, jsonify, request
from flask_login import current_user, login_required
from .forms import UserAssignForm
from src.models.task import Task
from src.models.project import Project
from src.models.user import User
from ..views import is_admin
from bson import ObjectId


# Admin: Show all users
@user.route('/users')
@login_required
def list_users():
    if not is_admin():
        abort(403)
    else:
        users = User.objects.all()
        return render_template('core/users/users.html',
                               users=users, title='Users')


# Admin: change user project/tasks
@user.route('/users/assign/<string:id>', methods=['GET', 'POST'])
@login_required
def assign_user(id):
    if not is_admin() or current_user.pk == ObjectId(id):
        abort(403)
    else:
        user = User.objects(pk=id).first()

        form = UserAssignForm(obj=user)

        # TODO: populate Project & Tasks 
        if request.method == 'POST' and form.validate_on_submit():
            user.project = form.department.data
            user.task = form.role.data
            user.save()
            flash('You have successfully assigned a project and tasks.')

            return redirect(url_for('user.list_users'))

        return render_template('core/users/user.html',
                               user=user, form=form,
                               title='Assign User')


@user.route('/users/ban/<string:id>', methods=['GET', 'POST'])
@login_required
def ban_user(id):
    if not is_admin() or current_user.pk == ObjectId(id):
        abort(403)
    else:
        user = User.objects(pk=id).first()
        user.status = 2
        flash('User banned')

        return redirect(url_for('user.list_users'))
        # TODO: Check mb useless
        return render_template(title="Ban user")
        