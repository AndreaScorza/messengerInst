import inst_module
import telegram_mess
import rw_to_file as rw


# instantiate the file
file = rw.StringArrayFile('data.txt')

#retrieve messages from instagram
messages = inst_module.getMessages()

# uncomment line below and comment line above to test message on telegram
# messages = [['PersonA', 'Text']]

for message in messages:
    if (not file.contains(message[0] + message[1]) and not file.is_unwanted(message[0])):
        telegram_mess.send_message(message[0] + '\n' + message[1])
        file.append(message[0] + message[1])