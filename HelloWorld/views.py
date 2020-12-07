from django.http import HttpResponse

from HelloWorld import models

from django.db.models import Avg, Max, Min, Count, Sum


def hello(request):
    return HttpResponse("Hello World!")


def add_book(request):
    # book = models.Book(title="菜鸟教程",price=300,publish="菜鸟出版社",pub_date="2008-8-8")
    books = models.Book.objects.create(title="菜鸟教程", price=300, publish="菜鸟出版社", pub_date="2008-8-8")
    # books = models.Book.objects.create(title="github教程",price=200,publish="http://www.github.com",pub_date="2010-10-10")
    # books = models.Book.objects.all()

    # for i in books:
    #     print(i.title)
    print(books, type(books))
    # book.save()
    return HttpResponse("<p>数据添加成功！</p>")
    # return HttpResponse("<p>查找成功！</p>")


def search_book(request):
    # books = models.Book.objects.all()
    # books = models.Book.objects.filter(publish='菜鸟出版社', price=300)
    books = models.Book.objects.exclude(publish='菜鸟出版社', price=300)

    for i in books:
        print(i.title)

    print(books, type(books))

    return HttpResponse("<p>查找数据成功！</p>")


def delete_book(request):
    books = models.Book.objects.filter(pk__in=[11, 12]).delete()
    # books = models.Book.objects.filter(pk__in=[2]).first().delete()

    return HttpResponse(books)


def modify_book(request):
    # books = models.Book.objects.filter(pk=3).first()
    books = models.Book.objects.filter(pk__in=[15, 16]).update(price=888)

    # books.title = 'github教程'
    #
    # books.save()

    return HttpResponse(books)


def add_books(request):
    pub_obj = models.Publish.objects.filter(pk=1).first()

    pk = pub_obj.pk

    # book = models.Books.objects.create(title="菜鸟教程", price=200, pub_date="2010-10-10", publish=pub_obj)
    book = models.Books.objects.create(title="冲灵剑法", price=100, pub_date="2004-04-04", publish_id=pk)

    print(book, type(book))

    return HttpResponse(book)


def caculate_book(request):
    # res = models.Book.objects.aggregate(Avg("price"))
    res = models.Book.objects.aggregate(c=Count("id"), max=Max("price"), min=Min("price"))
    print(res, type(res))

    return HttpResponse("ok")

def index(request):
    print("index视图...")
    return HttpResponse("ok")
