import os
import time
from slackclient import SlackClient

BOT_ID = os.environ.get("BOT_ID")

AT_BOT = "<@"+BOT_ID+">:"
EXAMPLE_COMMAND = "do"

def handle_command(command,channel):
        response = "I do not recognize that command"
        if command.startswith(EXAMPLE_COMMAND):
		print "do what"
                response = "Sure... could you please explain what is to be done"
                slack_client.rtm_send_message(channel,reponse)

def parse_slack_output(slack_rtm_output):
        output_list = slack_rtm_output
        print output_list
	if output_list and len(output_list)>0:
                for output in output_list:
                        if 'text' in output and AT_BOT in output['text']:
                                return output['text'].split(AT_BOT)[1].strip().lower(), output['channel']
        return None,None

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
if slack_client.rtm_connect():
	while True:
		command,channel = parse_slack_output(slack_client.rtm_read())
		if command and channel:
			handle_command(command,channel)
		time.sleep(1)
else:
	print "Connection Failed"

