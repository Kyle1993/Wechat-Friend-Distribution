import matplotlib as mpl
import matplotlib.pyplot as plt

def generate_fig(data,show=False):
	plt.figure(figsize=(6,8)) #调节图形大小
	labels = ['Male','Female','Unknow'] #定义标签
	sizes = [data[l] for l in labels]
	colors = ['skyblue','dodgerblue','lightgray'] #每块颜色定义
	explode = (0,0,0) #将某一块分割出来，值越大分割出的间隙越大
	patches,text1,text2 = plt.pie(sizes,
	                      explode=explode,
	                      labels=labels,
	                      colors=colors,
	                      autopct = '%3.2f%%', #数值保留固定小数位
	                      shadow = False, #无阴影设置
	                      startangle =90, #逆时针起始角度设置
	                      pctdistance = 0.6) #数值距圆心半径倍数距离
	#patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
	# x，y轴刻度设置一致，保证饼图为圆形
	plt.title('Friends Gender Distribution',fontsize = 24)	
	plt.axis('equal')
	plt.savefig("fig.png")
	if show:
		plt.show()

if __name__ == '__main__':
	data = {'Male':10,'Female':2,'Unknow':1}
	generate_fig(data,True)