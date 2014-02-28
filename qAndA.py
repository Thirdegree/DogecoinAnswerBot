#I'm so, so sorry.
#sytactially fine as of 11:21 2/20/2014
import main
qAndA = {
			r"(?i)\+\/u\/dogetipbot ([0-4](\.[0-9]*)*|0*\.[0-9]+) [\w]+":lambda: "The minimum tip for dogetipbot is 5 doge.",
			r"(?i)(How|Where) (can|do) I get flair\?*":lambda: "Upper right hand side of /r/dogecoin you will see the current number of subscribers.  Just below that is \"Show my flair on this subreddit. It looks like:\" make sure the box is checked and click EDIT to pick your flair.",
			r"(?i)What('*s| is) a megaflip\?*":lambda: "Megaflip = minimum tip * random number between 1 and 20\n\nMore bot commands listed [HERE]( http://www.reddit.com/r/ALTcointip/wiki/index#wiki_amount_keywords).  You can tip a cookie, beer, coffee, or even all.",
			r"(?i)(Who|What('*s)*).+satoshi\?*":lambda: "A Satoshi is the smallest measure of a Bitcoin. 1 Satoshi = 0.00000001 BTC (100,000,000 Satoshi = 1 BTC). This is used as a measure to compare the value of 1 dogecoin against bitcoin.\n\n* Current value of 1 dogecoin is %f Satoshi.\n\nFun fact: Satoshi is the first name of the founder of bitcoin."%(float(main.get_values("doge", "btc"))*100000000),
			r"(?i)What('*s| is| does) VOS (mean|stand for)\?*":lambda: "www.VaultOfSatoshi.com this is a place where you can buy and sell dogecoins along with other types of cryptocurrincies like litecoin, bitcoin, and others.",
			r"(?i)What('*s| is) crypto *currency\?*":lambda: "A cryptocurrency is a digital medium of exchange. The first cryptocurrency to begin trading was Bitcoin in 2009. Since then, numerous cryptocurrencies have become availible. Fundamentally, cryptocurrencies are specifications reguarding the use of currency which seek to incorporate principles of cryptography to implement a distributed, decentralized, and secure information economy. When comparing cryptocurrencies to fiat money, the most notable difference is in how no group or individual may accelerate, stunt, or in any other way significantly abuse the production of money. Instead, only a certain amount of cryptocurrency is produced by the eintire cryptocurrency system collectively, at a rate which is bounded by a value both prior defined and publicaly known.\n\nSource: http://en.wikipedia.org/wiki/Cryptocurrency",
			r"(?i)(What|explain).+(halving|halvening)\?*":lambda: "The halvening means, when we are at the 100.000 block block reward will be half of what it's today. Now for every block we \"mine\", we get 0 - 1,000,000 Dogeocoins. After the \"halvening\" we will get 0 - 500,000 per \"mined\" block. So, for every 100,000 blocks we \"mine\", block reward get smaller. In conclusion, this so called \"halvening\" will occur every 100,000 blocks until the block reward are at 0 - 10,000 Dogecoins only. By then we hit that, we will have mined all 100 billion dogecoins there are, so after that an additional 5 billion will be added per year with 0 - 10,000 block reward. That means 5% more doges first year, next year around 4.8% and it keeps lowering for every year. (percentage lowers, not amount of doges which still is 5 billion a year).  Comment submitted by /u/WowSuchMoney Halving chart that includes dates can be seen [HERE]( http://en.wikipedia.org/wiki/Dogecoin#Block_schedule)",
			r"(?i)Who (made|invented) dogecoin\?*":lambda: "Dogecoin was created on December 8th, 2013 by Jackson Palmer (/u/ummjackson)",
			r"(?i)What('*s| is) the minimum I can tip\?*":lambda: "5 doge.",
			r"(?i)(Where|How) .+ buy doge.*\?*":lambda: u"""There are a few ways to buy dogecoin...\n\n
Dogecoin market/exchange\n\n
* [Vault Of Satoshi]( https://www.vaultofsatoshi.com/)\n\n
* [BTER](https://bter.com/trade/doge_btc)\n\n
* [Coinedup](https://coinedup.com/OrderBook?market=DOGE&base=BTC)\n\n
* [Cryptsy](https://www.cryptsy.com/markets/view/132)\n\n
* [COINS-E] (https://www.coins-e.com/exchange/DOGE_BTC/)\n\n
* [Vircurex] (https://vircurex.com/welcome/index?alt=doge&base=btc&locale=en)\n\n
* [Coinex](https://coinex.pw/trade/doge_btc)\n\n
* [Dogemarket](/r/dogemarket)\n\n
* [Stuff for Dogecoin](http://www.stuffcoins.com/doge/)\n\n
* [BTC-8](http://btc-8.com/?DOGE_CNY) *Chinese Exchange ??  ??*\n\n
* [Dogelist](http://www.dogeslist.org) ebay-like trading with Dogecoins\n\n
Pros - The above exchanges typically require an ID and proof of address in order to create an account with them.\n\n
Cons - They will take a few days to authorize you as a customor before you can purchase.\n\n
* /r/dogemarket\n\n
* www.ebay.com\n\n
* /u/SuchTradeBot\n\n
Pros - The above places are very fast and can get you doge TODAY.\n\n
Cons - You will pay a higher premium per doge going this route due to convenience. You are dealingwith an individual person, not a bank/marketplace here. Please beware of conartists on ebay and dogemarket and make sure they have a good history of selling.""",
			r"(?i)Where can I spend.*doge(coins)*\?*":lambda: """There are both brick and mortar stores and online retailers that take doge. \n\n
Online -\n\n
Treats.io\n\n
Moolah.ch\n\n
Local stores -\n\n
Donuts""",
			r"(?i)(How much|Value)[^\?\$]+doge( cost)*\?*":lambda: "Value for doge currently trading at $%s per doge according to www.vaultofsatoshi.com"%(main.get_values('DOGE', 'USD')),
			r"(?i)How (much|many)[^(doge)]+\$1\?*":lambda: "$1 can buy you roughly %d doge (minus trade fees) www.vaultofsatoshi.com."%(1/float(main.get_values("DOGE", "USD"))),
			r"(?i)When did doge.+start\?*":lambda: "Decenber 8^^(th), 2013 is when the coin started.",
			r"(?i)(Who|What) are.+coins backed by\?*":lambda: "Everybody and nobody.  The community buys and sells similar to traditional stock.  No company owns or runs dogecoin.  Dogecoin is traded in marketplaces online and can be used to purchase things online and in some stores.",
			r"(?i)Do the (creators|authors) make money.*\?*":lambda: "No, not unless they own a few dogecoin of their own.",
			r"(?i)Who sets the price of doge(coin)*\?*":lambda: "The community buys and sells dogecoin at online marketplaces. Depending on what people want to buy and sell for is what determins the price, very similar to traditional stocks.",
			r"(?i)Why.+good graphics card\?*": lambda: "The graphics card is where all the computations take place to mine doge. The better the graphics card, the more you can mine.",
			r"(?i)How do.+make.+doge (image|graphic)\?*": lambda: "Start your line off with a minimum of 4 spaces and then start typing text.\n\n    such education\n             much learning\n         many text\n                         wow",
			r"(?i)How much.+in my account\?*": lambda: "Click [Here](http://www.reddit.com/message/compose?to=dogetipbot&subject=history&message=%2Bhistory) to send the bot a message and click send. This will give you a list of: username, number of coins tipped to you, and a time/date stamp of the tip.",
			r"(?i)(How|Where) do I make an account\?*": lambda: "Click [here](http://www.reddit.com/message/compose?to=dogetipbot&subject=register&message=%2Bregister) to send the tip bot a message to register.",
			r"(?i)(How|What|Where).+wallet\?*": lambda: """* [Official desktop wallet](http://dogecoin.com/)\n\n
* [Securing your wallet](http://www.reddit.com/r/dogecoin/comments/1u28m5/psa_stop_using_online_wallets/). [[2]](http://www.reddit.com/r/dogecoin/comments/1u1liu/psa_keeping_your_doge_safe/) [[3]](http://www.reddit.com/r/dogecoin/comments/1tyv4w/how_to_create_an_offline_wallet_for_cold_storage/) [[4]](http://www.reddit.com/r/dogecoin/comments/1td9k8/stepbystep_guide_to_keeping_your_dogecoin_secure/) <-Four posts, very important!\n\n
* [Mobile Wallet (Android)](https://play.google.com/store/apps/details?id=de.langerhans.wallet)\n\n
* [Dogecoin paper wallet generator and instructions](http://dogecoinpaperwallet.net/)\n\n
* [MY DOGE](https://itunes.apple.com/us/app/mydoge/id805178886?mt=8) A way to keep track of your dogecoin wallets (itunes link)""",
			r"(?i)What('*s| is) a faucet\?*": lambda: """A faucet is a place where you go and simply type in your address and it will transfer a few coins to you. Please keep in mind that availability of coins depends on if/when they give out dogecoin for free.\n\n
[Franks list](http://dogebb.com/index.php?topic=185.0)\n\n
[Dogecoin Directory](http://www.doktorrf.com/dogecoin.faucets.html)\n\n
[Dogec0in.com the chat waterbowl](http://dogec0in.com/)\n\n
[Alexanders List](http://freedogecoins.net/)""",
			r"(?i)What subreddits have banned (tip bot|dogetipbot)\?*": lambda: "A lot of subreddits have banned the tipbot because a thread can start to get messy when it is flooded with tips. Please be aware the transactions still go through even if the \"verify\" command does not work in a subreddit.",
			r"(?i)Can I mine on.+laptop\?*": lambda: "It is strongly advised that you do not mine on your laptop due to heat issues that are associated with mining. The video processor will run at very high and constant temperature and it is not a good idea to min on a laptop. [This](http://i.imgur.com/VQ70Wf7.jpg) is what a typical generic setup for mining cryptocurrincies looks like. Video Cards run at a very high temperature so it is best to have an open air setup. Because laptops are very small and enclosed, it is pretty much the worst possible setup for mining. The combination of small parts and very tight space is a recipe for disaster.",
			r"(?i)What do I need to mine\?*": lambda: "A desktop computer of some sort. The higher quality your video card is, the more doge you can mine. A laptop is NOT recommended. Mining on your phone will yield very little results. A typical mining setup will look like [this](http://i.imgur.com/VQ70Wf7.jpg) Other things you will need is a wallet and software to get into a pool to mine. More info on mining can be found at /r/dogemining.",
			r"(?i)How do I mine\?*": lambda: "There are a number of steps involved in mining to get a mining rig up and running. There are two major aspects of mining, the software and the hardware. For the software side I would strongly advise you read the wiki page located in /r/dogemining. http://www.reddit.com/r/dogemining/wiki/index/mining_guide This is a step by step guide to get your software talking to the pools needed to get you mining coins. If you need help building a rig to mine, please post your questions in /r/dogemining. Each mining machine is different and depending on what your budget is will determine what parts you get for your rig. If you reply to this comment, don't expect an answer back from me... I'm a bot.",
			r"(?i)Can I mine on my (phone.*|cell.*|mobile.*)\?*": lambda: "Short answer, no. It requires a lot of computing power that a phone does not have. Technically yes you can mine on your phone but you will not get much at all.",
			r"(?i)What('*s| is) the best pool to join\?*": lambda: """The more people in the pool the more chances of you finding blocks, hence the more chances of making coins. Go to a pool that has a fair amount of people in it andyou'll be fine.\n\n
[Dogecoin Directory](http://www.doktorrf.com/dogecoin/pools.html)\n\n
[Dogepool List](http://dogepool.com)""",
			r"(?i)What('*s| is).+hash( *rate)*\?*": lambda: "Hashrate is how fast your machine mines doge. The higher the number, the better. Higher end video cards will yield higher hashrates.",
			r"(?i)What('*s| is) a good hash( *rate)*\?*": lambda: "The higher the number the better. Each video card is different so the better your video card, the high the hash rate. A really high end video card will run you around $600-$800USD. Paybacks in mining for high end equipment tend to be around 3 months depending on the market.",
			r"(?i)Can you tip someone in a pm\?*": lambda: "No.",
			r"(?i)Can you PM someone a tip\?*": lambda: "No.",
			r"(?i)How do I tip\?*": lambda: "Reply to a comment or a post with the text \"+/u/dogetipbot number doge\" (without the quotes). The minimum you can tip is 5 doge. You can also tip someone in other ways like a cookie or beer. See more info on that [here](http://www.reddit.com/r/ALTcointip/wiki/index#wiki_amount_keywords).",
			r"(?i)What('*s| is) a pool\?*": lambda: """A pool is a group of miners who are working togeather to solve a block so they can get dogecoin.\n\n
[Dogecoin Directory](http://www.doktorrf.com/dogecoin/pools.html)\n\n
[Dogepool List](http://dogepool.com)""",
			r"(?i)What('*s| is) fiat\?*": lambda: """Fiat money has been defined variously as:\n\n
* Any money declared by a government to be legal tender.\n\n
* State-issued money which is neither convertible by law to any other thing, nor fixed in value in terms on any objective standard.\n\n
* Money without intrinsic value that is used as money because of government decree.""",
			r"signature": lambda: "^^Please ^^Report ^^any ^^errors ^^to ^^/r/DogecoinAnswersBot"
}

subreddits = "dogecoin"




