import re, praw, json, requests, fuzzy_match
from collections import deque
from time import sleep
import qAndA_backup as q1
import qAndA as q2

# This dictionary is in the form {"re pattern":lambda: "answer %d"%(optional_funtion_call)}

r = praw.Reddit("Keeping an eye on DogecoinAnswersBot by /u/Thirdegree")

def _login():
	USERNAME = raw_input("Username?\n> ")
	PASSWORD = raw_input("Password?\n> ")
	r.login(USERNAME, PASSWORD)
	return USERNAME

done = deque(maxlen=300)


def fuzzy_correct(body):
	correctedBody = map(fuzzy_match.correct, body.split())
	return " ".join(correctedBody)
	
def get_values(first, second):
	if second.upper()=='USD':
		t = requests.get("https://api.vaultofsatoshi.com/public/ticker?order_currency=%s&payment_currency=%s"%(first, second))
		j = json.loads(t.text)
		if j['status']=="success":
			return j['data']['closing_price']['value']
		else:
			return "Lookup failed."
	else:
		t = requests.get("http://www.cryptocoincharts.info/v2/api/tradingPair/%s_%s"%(first, second))
		j = json.loads(t.text)
		if j['id']:
			return j['price']


def find_matches(body):
	patterns = {}
	for pattern in q.qAndA:
		match = re.search(pattern, body)
		if match:
			patterns[pattern]=match.group()
	return patterns

def get_reply(body):
	fuzzyCorrected = fuzzy_correct(body)
	patterns = find_matches(body)
	print body
	if not patterns: 
		patterns = find_matches(fuzzyCorrected)
	reply = ""
	for i in patterns:
		print i
		reply += "> %s\n\n%s\n\n%s\n\n"%(patterns[i], q.qAndA[i](), q.qAndA['signature']())
	return reply

def main():
	comments = r.get_comments(q.subreddits, limit=100)
	for post in comments:
		rep = get_reply(post.body)
		if rep and post.id not in done and post.author.name!=USERNAME:
			done.append(post.id)
			post.reply(rep)
			sleep(2)
	sleep(10)

def check_scores():
	me = r.get_redditor(USERNAME)
	comments = me.get_comments(limit = 100)
	for post in comments:
		#print post.score
		if post.score<=(-1):
			r.send_message("Thirdegree", "Post deleted for low score", post.body)
			post.delete()
			sleep(2)
	sleep(2)


if __name__ == '__main__':
	Trying = True
	while Trying:
		try:
			USERNAME = _login()
			Trying = False
		except praw.errors.InvalidUserPass:
			print "Invalid Username/password, please try again."
	running = True
	while running:
		if 'q' in vars():
			del(q.qAndA)
		print "del"
		try:
			q = reload(q2)
			print "r1"
		except Exception as e:
			if q == q2:
				r.send_message("Thirdegree", "Problem loading main qAndA modual", e)
			q = reload(q1)
			print e, "r2"
			sleep(2)
		try:
			check_scores()
			for i in xrange(3):
				main()
		except praw.errors.RateLimitExceeded:
			print "Rate limit exceeded, sleeping 10 min"
			sleep(590)
		except KeyboardInterrupt:
			running = False
		except Exception as e:
			print e, "outer"
			sleep(50)

