import urllib.request
import requests
import os
from bs4 import BeautifulSoup
import docx
def getweburl(mainurl):

        reporturls=[]
        url = mainurl
        # 建立请求对象
        request = urllib.request.Request(url)
        # 加入请求头
        request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36')
        # 获取请求
        code = urllib.request.urlopen(request)
        # 得到html代码
        html = code.read().decode('utf-8')
        # 将html的标签转成对象（方便后面的操作）
    
        soup = BeautifulSoup(html,'html.parser')
        page=soup.find_all("div", {"class":{"box-list"}})
        page=page[-1]        
        links = page.select("a")
        
        for each in links:
                data=each.get('href')
                reporturls.append("http://www.cjh.com.cn//"+data)
        return reporturls
def store():
        COUNT=0
        if os.path.exists('images'):
                print();
        else:
                os.mkdir('images')
        doc=docx.Document()#创建一个Document对象

        for iurl in imgsrcl:
                COUNT=COUNT+1;
                filepath=os.getcwd()
                imagename=filepath+"\\images\\"+title+"_"+str(COUNT)+".jpg"
                docname=filepath+"\\images\\"+title+".docx"
                urllib.request.urlretrieve(iurl,imagename)
                doc.add_picture(imagename)
        doc.save(docname)#保存文档
        
def getimgurl(reporturl):
	url = reporturl
	# 建立请求对象
	request = urllib.request.Request(url)
	# 加入请求头
	request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36')
	# 获取请求
	code = urllib.request.urlopen(request)
	# 得到html代码
	html = code.read().decode('utf-8')
	# 将html的标签转成对象（方便后面的操作）
	
	soup = BeautifulSoup(html,'html.parser')
	
	#寻找parent
	parent = soup.find(name="div", attrs={"class" :"content_1 article"})
	
	imgsrcl=[]
	#找到所有的li
	lis = parent.find_all('p')
	title=parent.find('h3').text
	for each in lis:
		if each.find('img'):
			src = each.find('img').attrs['src']#读取字典的src
			imgscr='http://www.cjh.com.cn'+src
			imgsrcl.append(imgscr)#添加到总的列表
	return imgsrcl,title

	


if __name__ == '__main__':
    for i in range(1,4):
            mainurl="http://www.cjh.com.cn/swyb_syqbg.html?pageno="+str(i);
            reurl=getweburl(mainurl)
            for iurl in reurl:
                    
                    imgsrcl,title=getimgurl(iurl)
                    store()

