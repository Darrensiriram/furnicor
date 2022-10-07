
from typing import List

from model.user import User
from model.employee import Employee

def createTableView(columns: List[str], rows:List[List[str]]):
    columnSize = 0
    for column in columns:
        if len(column) > columnSize:
            size = len(column)

    tableFormat = ''

    for(i,size) in enumerate(columns):
        size = len(columns)

        for row in rows:
            length = (row[i])
            if length > size:
                size = length
        tableFormat += '{:<'  + str(size + 5) + '}'

    print(tableFormat.format(*columns))

    for row in rows:
        print(tableFormat.format(*row))


def ShowUsers(users: List[User]):
    columns = ['ID','Username', 'Role', 'Created at' ]
    rows = []

    for user in users:
        columns.append([
            user.id,
            user.username,
            user.role,
            user.created_at
        ])
    createTableView(columns, rows)

def ShowEmployee(employees: List[Employee]):
    columns = ['ID', 'First name', 'Last name',
               'Street name', 'House number', 'Postal Code', 'City',
               'Email',
               'Phone',
               'Created at']
    row = []

    for employee in employees:
        columns.append([
            employee.id,
            employee.first_name,
            employee.last_name,
            f'{employee.street_name} {employee.house_number}',
            employee.postalCode,
            employee.city,
            employee.email,
            employee.phone,
            employee.created_at,
        ])
    createTableView(columns,row)

# def showLogs(logs: List[Log], userId: int ):
#     columns = ['ID', 'User', 'Created at', 'Description']
#     rows = []
#
#     for log in logs:
#         user = none
#         if log.user:
#             user = f'{log.user.id} {log.user.username}'
#
#         rows.append([
#             log.id,
#             'Null' if user is None else user,
#             log.created_at,
#             log.message,
#         ])