
from typing import List

from model.user import User
from model.member import Member
from model.log import Log

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

def ShowMember(members: List[Member]):
    columns = ['ID', 'First name', 'Last name',
               'Street name', 'House number', 'Postal Code', 'City',
               'Email',
               'Phone',
               'Created at']
    row = []

    for member in members:
        columns.append([
            member.id,
            member.first_name,
            member.last_name,
            f'{member.street_name} {member.house_number}',
            member.postalCode,
            member.city,
            member.email,
            member.phone,
            member.created_at,
        ])
    createTableView(columns,row)

def showLogs(logs: List[Log], userId: int ):
    columns = ['ID', 'User', 'Created at', 'Description']
    rows = []

    for log in logs:
        user = None
        if log.user:
            user = f'{log.user.id} {log.user.username}'

        rows.append([
            log.id,
            'Null' if user is None else user,
            log.created_at,
            log.message,
        ])