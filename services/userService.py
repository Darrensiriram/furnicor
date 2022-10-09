from typing import Any, Dict, List
from model.user import User
from interface.IDatabaseActions import IDatabaseActions
from helpers.passwordHasher import PasswordHasher
from logService import LogService
from sessionService import SessionService


class UserService():
    action: IDatabaseActions[User]
    pwHasher: PasswordHasher
    session: SessionService
    log: LogService

    def __init__(self, action: IDatabaseActions[User], pwHasher: pwHasher, session: session, log: log):
        self.action = action
        self.pwHasher = pwHasher
        self.session = session
        self.log = log
        self.createAdmin()

    def createAdmin(self) -> None:
        try:
            self.action.selectOne(1)
        except:
            [pwHash, salt] = self.pwHasher.hashPw('Admin321!')
            self.action.create(User(
                'superadmin',
                'Super',
                'Admin',
                'super_admin',
                pwHash,
                salt
            ))
            self.log.logInfo('admin account created.')

    def login(self, username: str, password: str) -> bool:

        sql = self.action.where({'username': username})

        if len(sql) == 0:
            self.log.logInfo('Login failed. user not found')
            return False
        user = sql[0]
        validCheck = self.pwHasher.checkHashedPw(password, user.password, user.salt)

        if not validCheck:
            self.log.logInfo('Log in failed. password dont match')
            return False

        self.session.currentUser = user
        self.log.logInfo('User has logged in!')

        return True

    def createUser(self, username: str, first_name: str, last_name: str, role: str, password: str) -> User:
        (pwHash, salt) = self.pwHasher.hashPw(password)
        user = User(username, first_name, last_name, role, pwHash, salt)
        self.action.create(user)
        self.log.logInfo(f'User created: {username}.')
        return user

    def showAllUsers(self) -> List[User]:
        listUsers = self.action.selectAll()
        self.log.logInfo(f'showing all users: total of {len(listUsers)} users')
        return listUsers

    def showAllEditableUsers(self) -> List[User]:
        if self.session.currentUser.role == 'system_adminstrator':
            listEditableUsers = self.action.where({'role': 'advisor'})
            self.log.logInfo(f'showing all users who can be altered. total of {len(listEditableUsers)} users.')
            return listEditableUsers

        if self.session.currentUser.role == 'super_admin':
            return self.showAllUsers()
        self.log.logFraud(f'user is not allowed to edit these users. user: {self.session.currentUser.username}')
        return []

    def search(self, criteria: str)-> List[User]:
        criteria.lower()
        searchResult = []
        users = self.action.selectAll()

        for user in users:
            if criteria in user.first_name.lower():
                searchResult.append(user)
            elif criteria in str(user.id).lower():
                searchResult.append(user)
            elif criteria in user.last_name.lower():
                searchResult.append(user)
            elif criteria in user.role.lower():
                searchResult.append(user)
            elif criteria in user.username.lower():
                searchResult.append(user)
        self.log.logInfo(f'found: {len(searchResult)} users.')
        return searchResult

    def update(self, id: int, updates: Dict[str, Any]) -> User:
        updatedUser = self.action.update(id, updates)
        self.log.logInfo(f'User updated {updatedUser}: {updatedUser}.')
        return updatedUser

    def update_pwd(self, id: int, old_pw: str, new_pw: str) -> None:
        user = self.action.selectOne(id)
        old_pwCheck = self.pwHasher.checkHashedPw(old_pw, user.password, user.salt)

        if old_pwCheck is False:
            self.log.logFraud(f"Tries to update the pwd for the user: {user}")
        (new_hash, new_salt) = self.pwHasher.hashPw(new_pw)
        self.action.update(
            id,
            {'password': new_hash, 'salt': new_salt, 'has_temp_pwd' : 0},
        )
        self.log.logInfo(f'Password has been changed for user: {user}')

    def delete(self, id:int ) -> None:
        user = self.action.selectOne(id)
        self.action.delete(id)
        self.log.logInfo(f"User deleted with name {user.first_name}")

    def setTmpPwd(self, id: int, pwd: str) -> User:
        (pwHash, salt) = self.pwHasher.hashPw(pwd)

        update_user = self.action.update(
            id,
            {'password': pwHash, 'salt':salt, 'has_temp_password': 1}
        )
        self.log.logInfo(f'temp password setted for {update_user}')
        return update_user

    def checkIfUserExits(self, username: str) -> bool:
        sql = self.action.where({'username': username})
        return len(sql) > 0
