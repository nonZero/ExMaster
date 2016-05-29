from django.shortcuts import render


def list_expenses(request):
    return render(request, 'expenses/expense_list.html', {
        'foo': 'YOYOYOYOYOYOYOYO',
        'bars': [30, 50, 20, 'udi', 'shalom'],
    })