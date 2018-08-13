from wxpy import *
import argparse

name_list = ['付豪','郑瑞阳','占汝真','吴逸飞','郑罗敏',]
# name_list = ['占汝真']
bot = Bot()

friends = {}
for name in name_list:
	if name == '占汝真':
		friends[name] = ensure_one(bot.search(name,nick_name='Irita'))
	else:
		friends[name] = ensure_one(bot.search(name))

tuling = Tuling(api_key='5e9fe11469fb490f872cbd268ea0ea64')

for name in name_list:
	friends[name].send(name+"！我想死你了！" )


# 使用图灵机器人自动与指定好友聊天
assert len(list(friends.values())) != 0
@bot.register(list(friends.values()))
def reply_my_friend(msg):
    tuling.do_reply(msg)


# bot.join()
# embed()