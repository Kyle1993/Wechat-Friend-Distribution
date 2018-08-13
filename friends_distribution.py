from wxpy import *
import argparse
import generate_map
import generate_fig

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser()
parser.add_argument("-map", type=str2bool, nargs='?',const=True, default=True,help='show friends loaction distribution map')
parser.add_argument("-fig", type=str2bool, nargs='?',const=True, default=True,help='show friends gender distribution fig')

args = parser.parse_args()
# print(args.map,args.fig)


# print('Please scan this QR code')
bot = Bot()

friends = bot.friends()

total = 0
male = 0
female = 0
out_of_china = 0
out_of_world = 0

provinces = {
	'北京':0,
	'天津':0,
	'上海':0,
	'重庆':0,
	'河北':0,
	'山西':0,
	'辽宁':0,
	'吉林':0,
	'黑龙江':0,
	'江苏':0,
	'浙江':0,
	'安徽':0,
	'福建':0,
	'江西':0,
	'山东':0,
	'河南':0,
	'湖北':0,
	'湖南':0,
	'广东':0,
	'海南':0,
	'四川':0,
	'贵州':0,
	'云南':0,
	'陕西':0,
	'甘肃':0,
	'青海':0,
	'台湾':0,
	'内蒙古':0,
	'广西':0,
	'西藏':0,
	'宁夏':0,
	'新疆':0,
	'香港':0,
	'澳门':0,
}

for f in friends:
	total += 1
	if f.province in provinces.keys():
		provinces[f.province] += 1
	elif f.province is None or f.province == '':
		out_of_world += 1
	else:
		out_of_china += 1

	if f.sex == 1:
		male += 1
	elif f.sex == 2:
		female += 1


sort_data = sorted(provinces.items(),key=lambda x:x[1])
most_friends_num = sort_data[-1][1]
least_friends_num = sort_data[0][1]
most_friends_str = ''
least_friends_str = ''

for k,v in provinces.items():
	if v == most_friends_num:
		most_friends_str += (k+',')
	elif v == least_friends_num:
		least_friends_str += (k+',')

# send friends distribution msg
friends_str = '您一共有 {} 名好友，其中国内 {} 名，国外 {} 名，未知地区 {} 名。\n您在 {} 好友最多，有 {} 名；\n您在 {} 好友最少，有 {} 名。'.format(total,(total-out_of_china-out_of_world),out_of_china,out_of_world,most_friends_str[:-1],most_friends_num,least_friends_str[:-1],least_friends_num)
bot.file_helper.send(friends_str)
print(friends_str)

# send friends distribution figure 
if args.map:
	generate_map.generate_map(provinces)
	bot.file_helper.send_image('map.png')

# send friends gender distribution mag
friends_gender_str = '您一共有 {} 名好友，其中男生 {} 名，女生 {} 名。'.format(total,male,female)
bot.file_helper.send(friends_gender_str)
print(friends_gender_str)

# send friends gender distribution figure
if args.fig:
	generate_fig.generate_fig({'Male':male,'Female':female,'Unknow':total-male-female})
	bot.file_helper.send_image('fig.png')


bot.logout()