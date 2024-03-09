from main import get_chart
import multiprocessing
import time

global_ticks = []
candles = ''
period = ''
destination = ''

def get_charts_parallel(index):
	t0 = time.time()
	ticker = global_ticks[index]
	get_chart(ticker, candles, period, destination)
	t1 = time.time()
	diff = t1 - t0
	print(f"{t} and {diff}")

def get_many_charts(tickers, cs='1D', pd='1Y', dt='/'):
	if __name__=="__main__":
		t0 = time.time()

		global_ticks = tickers
		candles = cs
		period = pd
		destination = dt

		n = len(global_ticks)
		n_charts = range(n)

		pool = multiprocessing.Pool()

		pool.map(get_charts_parallel, n_charts)

		pool.close()
		pool.join()

		t1 = time.time()
		print(t1 - t0)