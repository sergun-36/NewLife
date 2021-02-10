#try:
from handling_curr import handling_curr_request
from for_telegram_api import give_answer, wait_answer, get_user, get_first_message
from test_logic import testing


def select_handling_answer(message, user):
	message=message.lower()
	if message.find("курс")>=0:
		answer_message=handling_curr_request(user, message)
		return answer_message
		
	"""
	if message.find("тест")>=0:
		answer_message=testing("telegram")
		return answer_message
	""" 

	if message.find("exit")>=0:
		return "Bye, bye .Я отключился"
			
	return message
	
"""
def run_bot():
	is_working=True
	while is_working:
		wait_answer()
		message=get_first_message()

		if select_handling_answer(message)!=None:
			is_working=False
		
	
		
if __name__=="__main__":
	run_bot()
"""



# except ImportError as ex:
# 	print(f" Обнаружено исключение импорта\n {ex}")

