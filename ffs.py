import os
import sqlite3

from actions.backupAction import BackupAction
from actions.createMemberAction import CreateMemberAction
from actions.createUserAction import CreateUserAction
from actions.deleteMemberAction import DeleteMemberAction
from actions.deleteUserAction import DeleteUserAction
from actions.loginAction import LoginAction
from actions.logoutAction import LogoutAction
from actions.quitAction import QuitAction
from actions.restoreBackupAction import RestoreBackupAction
from actions.searchMemberAction import SearchMemberAction
from actions.searchUserAction import SearchUserAction
from actions.setTmpPasswordAction import SetTmpPasswordAction
from actions.updateMemberAction import UpdateMemberAction
from actions.updatePasswordAction import UpdatePasswordAction
from actions.updateUserAction import UpdateUserAction
from actions.viewLogsAction import ViewLogsAction
from actions.viewMemberAction import ViewMemberAction
from actions.viewUserAction import ViewUserAction

from interface.Interface import Interface

from cipher.ceaserEncryption import CeasarEncryption

from helpers.passwordHasher import PasswordHasher

from databaseActions.logActions import LogActions
from databaseActions.memberActions import MemberActions
from databaseActions.userActions import UserActions

from services.backupService import BackUpService
from services.logService import LogService
from services.memberService import MemberService
from services.sessionService import SessionService
from services.userService import UserService

if __name__ == '__main__':

    encryption = CeasarEncryption("test!")
    connection = sqlite3.Connection('database/furnicor.db')
    session = SessionService()
    app = Interface('Furnicor System')

    userActions = UserActions(connection,encryption)
    logAction = LogActions(connection,encryption,userActions)
    logService = LogService(session, logAction)

    app.createActions('See logs', ViewLogsAction(session, logService))
    userService = UserService(userActions, PasswordHasher(), session, logService)

    app.createActions('Quit', QuitAction())
    app.createActions('Login',LoginAction(session,logService, userService))

    app.startApplication()
