from kavenegar import *
from urllib.error import HTTPError


def send_sms_whit_template(receptor,tokens:dict, template):
    """
        sending sms that needs template
    """
    try:
        api=KavenegarAPI(
            '4D597A707341464C394F4E7075534D65364364484A61576A2F313054705173594A2F4A474738567A7541413D'
        )
        params={
            'receptor':receptor,
            'template':template,
        }
        for key,value in tokens.items():
            params[key]=value

        response=api.verify_lookup(params)
        print(response)
        return True
    except APIException as e:
        print(e)
        return False
    except HTTPException as e:
        print(e)
        return False


def send_sms_normal(receptor, message):
    try:
        api=KavenegarAPI(
            '4D597A707341464C394F4E7075534D65364364484A61576A2F313054705173594A2F4A474738567A7541413D')
        params_buyer={
            'receptor': receptor,
            'message':message,
            'sender':'09963140715',
        }
        response= api.sms_send(params_buyer)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)