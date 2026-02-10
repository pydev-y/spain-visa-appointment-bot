
import sys, asyncio, random, time
from datetime import datetime, timedelta
import controllers.browser_proxy_nonmultiple as br
import pytz

PKT = pytz.timezone("Asia/Karachi")

def sleep_until_830():
    now = datetime.now(PKT)

    target = now.replace(hour=8, minute=45, second=0, microsecond=0)

    if target <= now:
        target += timedelta(days=1)

    sleep_seconds = (target - now).total_seconds()

    print("Current Pakistan Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("Sleeping until:", target.strftime("%Y-%m-%d %H:%M:%S"))
    print(f"Sleeping for {sleep_seconds/60:.2f} minutes...")

    time.sleep((target - now).total_seconds())



# main.py
if __name__ == "__main__":

	with open("./data/accounts.txt", "r", encoding="utf-8") as f:
	    users = [line.strip().split(':') for line in f if line.strip()]
	    

	with open("./data/proxies.txt", "r", encoding="utf-8") as f:
	    proxies = [line.strip() for line in f if line.strip()]




	# Sleep until 8:30 AM
	sleep_until_830()

	print("✅ Woke up! It's 8:30 AM")

	asyncio.run(br.combined_browsers(proxies,users))
