xxx = "buy"
sell = 1
hold = 2

def trade(a):
	if a == "buy":
		buy_one()
	if a == 1:
		sell_one()
	if a == 2:
		hold_position()
	else:
		return 0

def buy_one():
	print("买入成功")

def sell_one():
	print("卖出成功")

def hold_position():
	print("仓位不变")

trade("buy")

trade(sell)

trade(hold)
