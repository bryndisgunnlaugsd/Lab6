from contextlib import AbstractContextManager
from typing import Callable

from injector import inject
from sqlalchemy.orm import Session

from core.interfaces.user_repository import IUserRepository
from core.models.user import User


class UserRepository(IUserRepository):
    @inject
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.__session_factory = session_factory

    def get_all(self) -> list[User]:
        with self.__session_factory() as session:
            return session.query(User).all()

    def create_user(self, user: User) -> None:
        with self.__session_factory() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
