from django.shortcuts import render, redirect


# Create your views here.
# 测试
def base(request):
    if request.method == "GET":
        return render(request, 'base/base.html')
# 公司简介
def info(request):
    if request.method == "GET":
        return render(request, 'home/info.html')
# 店铺展示
def show(request):
    if request.method == "GET":
        return render(request, 'home/show.html')
# 人才招聘(商品部)
def goods(request):
    if request.method == "GET":
        return render(request,'hiring/goods.html')

# 人才招聘(营运部)
def manage(request):
    if request.method == "GET":
        return render(request, 'hiring/manage.html')

# 人才招聘(管理部)
def service(request):
    if request.method == "GET":
        return render(request, 'hiring/service.html')
# 联系我们
def contact(request):
    if request.method == "GET":
        return render(request,'home/contact.html')