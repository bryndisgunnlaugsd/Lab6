from injector import inject

from core.interfaces.sms_gateway import ISmsGateway
from core.interfaces.subscription_repository import ISubscriptionRepository
from core.models.subscription import Subscription


class SubscriptionService:
    @inject
    def __init__(self, repository: ISubscriptionRepository, sms_gateway: ISmsGateway):
        self.__repository = repository
        self.__sms_gateway = sms_gateway

    def get_all(self) -> list[Subscription]:
        return self.__repository.get_all()

    def create_subscription(self, subscription: Subscription) -> None:
        self.__repository.create_subscription(subscription)
        self.__sms_gateway.send_sms(subscription.user.phone_number, "You have been subscribed!")