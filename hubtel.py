from pyhubtel_sms import SMS, Message

def sms(telephone, message):
	sms = SMS(client_id='dnymazlw', client_secret='hqynfckc')
	message = Message(
			sender='COMPSSA',
			content=message,
			recipient=telephone,
			registered_delivery=True,
	)
	sms.send(message)


