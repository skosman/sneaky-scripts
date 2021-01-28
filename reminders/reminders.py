# Take a break reminder
# Sam Kosman
# Date: Jan 2021

import os

def remind(title, subtitle,  message):
	print("Take break")
	t = '-title {!r}'.format(title)
	s = '-subtitle {!r}'.format(subtitle)
	m = '-message {!r}'.format(message)
	os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

if __name__ == "__main__":
	remind(title = 'Take a Break',
       	subtitle = 'Look away 👀',
       	message  = 'Hi, you\'ve stared at the screen for too long. Go for a walk or look outside. Thanks!')
