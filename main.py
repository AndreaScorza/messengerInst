import inst_module
import telegram_mess
import rw_to_file as rw


# instantiate the file
file = rw.StringArrayFile('data.txt')

#retrieve messages from instagram
messages = inst_module.getMessages()

# messages = [['PersonA', 'Test']]

for message in messages:
    if (not file.contains(message[0] + message[1])):
        telegram_mess.send_message(message[0] + '\n' + message[1])
        file.append(message[0] + message[1])