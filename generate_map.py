
import math

def tanh(x):
	return (math.e**x-math.e**(-x))/(math.e**x+math.e**(-x))


def generate_map(data,show=False):
	import matplotlib as mpl
	import matplotlib.pyplot as plt
	from mpl_toolkits.basemap import Basemap
	from matplotlib.patches import Polygon
	from matplotlib import cm

	# add HKG,OMA to GuangDong
	data['广东'] += (data['香港']+data['澳门'])

	# get color cmp
	color_cmp = plt.get_cmap('Blues') 

	# normalize data
	total = sum(list(data.values()))
	for k in data.keys():
		c = (data[k]/total)*15
		c = tanh(c)
		data[k] = (c,color_cmp(c))

	# generate figure
	plt.figure(figsize=(8,6))
	m = Basemap(llcrnrlon= 81,llcrnrlat=13,urcrnrlon=144,urcrnrlat=52,projection='poly',lon_0 = 116.65,lat_0 = 40.02)
	m.readshapefile("CHN_adm1",'provinces',drawbounds=True)
	m.readshapefile('gadm36_TWN_0','taiwan',drawbounds=True)

	ax = plt.gca()
	#大陆地区进行上色
	for i, shapedict in enumerate(m.provinces_info):
		p = shapedict['NL_NAME_1'].split('|')
		s = p[1] if len(p)>1 else p[0]
		
		if s =='黑龍江省':
			s = '黑龙江'
		s = s.replace('自治区','')
		s = s.replace('壮族','')
		s = s.replace('回族','')
		s = s.replace('维吾尔','')
		ax.add_patch(Polygon(m.provinces[i],color = data[s][1]))
	#台湾地区进行上色
	for i, shapedict in enumerate(m.taiwan):
		ax.add_patch(Polygon(shapedict, color=data['台湾'][1]))

	plt.axis("off")  #关闭坐标轴
	plt.title('Friends Location Distribution',fontsize = 24)
	plt.savefig("map.png")
	if show:
		plt.show()

if __name__ == '__main__':
	data = {'香港':0, '澳门':0, '海南': 2, '江西': 30, '山东': 7, '广东': 207, '天津': 2, '河南': 3, '湖北': 5, '青海': 1, '西藏': 1, '湖南': 12, '江苏': 6, '上海': 18, '河北': 1, '广西': 5, '贵州': 2, '宁夏': 1, '山西': 6, '北京': 30, '重庆': 2, '四川': 13, '云南': 14, '浙江': 11, '陕西': 3, '台湾': 0, '黑龙江': 1, '辽宁': 11, '吉林': 2, '安徽': 1, '新疆': 0, '内蒙古': 1, '福建': 6, '甘肃': 0}
	generate_map(data,show=True)