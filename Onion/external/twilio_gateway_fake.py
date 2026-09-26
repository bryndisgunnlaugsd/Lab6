from core.interfaces.sms_gateway import ISmsGateway


class TwilioGatewayFake(ISmsGateway):

    def send_sms(self, phone_number: str, message: str) -> None:
        print(f'Email to {phone_number} sent with message: {message}')