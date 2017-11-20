# coding=utf-8
# lovelinxue
# theFileFunction: 
# -*- coding: utf-8 -*-

class htmlOutputer(object):

    def __init__(self):
        self.dataArray = []

    def collect_data(self, new_data):
        if new_data is None:
            print 'output中的collect_data参数为空'
            return
        self.dataArray.append(new_data)


    def output_html(self):
        fout = open('output.html','w')

        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.dataArray:
            fout.write('<tr>')
            #默认是ascii编码，需要转码为utf-8
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['content'].encode('utf-8'))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()