from xml.dom import minidom
import fitz  # работает
import re

root = minidom.Document()   #создаем хмл-файл. Есть еще другие библиотеки, типо ElementryTree
tei = root.createElement("TEI")
root.appendChild(tei)
teiheader = root.createElement("teiHeader")
tei.appendChild(teiheader)

filedesc = root.createElement("fileDesc")
teiheader.appendChild(filedesc)

titlestmt = root.createElement("titleStmt")
filedesc.appendChild(titlestmt)

title1 = root.createElement("title")
titlestmt.appendChild(title1)
body = root.createElement("body")
title1.appendChild(body)

div = root.createElement("div")
body.appendChild(div)

doc = fitz.Document("/home/zhenya/PycharmProjects/project1/tdoc.pdf")
page_count = doc.pageCount
i = 2
text_l = []
while i < page_count:
    text = doc.loadPage(i)
    page = root.createElement("pb")
    div.appendChild(page)
    page.appendChild(root.createTextNode(str(i)))
    if i == 2:
        title_of_the_book = root.createElement("title_of_the_book")
        div.appendChild(title_of_the_book)
        title_of_the_book.appendChild(root.createTextNode(text.getText("text").replace('\n', ' ')))
    elif i == 3:
        ch = root.createElement("characteristics")
        div.appendChild(ch)
        ch.appendChild(root.createTextNode(text.getText("text").splitlines()[0] + ' ' + text.getText("text").splitlines()[1]))
        ep = root.createElement("epigraph")
        div.appendChild(ep)
        ep.appendChild(root.createTextNode(text.getText("text").splitlines()[2] + ' ' + text.getText("text").splitlines()[3] + ' ' + text.getText("text").splitlines()[4] ))
    elif i == 4:
        typ = root.createElement("typographie_and_year")
        div.appendChild(typ)
        typ.appendChild(root.createTextNode(text.getText("text").replace('\n', ' ')))
    elif i == 5:
        cen = root.createElement("pechat_and_censors")
        div.appendChild(cen)
        cen.appendChild(root.createTextNode(text.getText("text").replace('\n', ' ')))
    elif 5 < i < 1054:
        razd = root.createElement("razdely")
        div.appendChild(razd)
        razd.appendChild(root.createTextNode(str(text.getText("text").split('\n')[0:2])))
        p = root.createElement("pure_text")
        div.appendChild(p)
        p.appendChild(root.createTextNode(text.getText("text").replace('\n', ' ')))
    elif 1053 < i < 1056:
        p = root.createElement("pure_text")
        div.appendChild(p)
        p.appendChild(root.createTextNode(text.getText("text").replace('\n', ' ')))
    elif i == 1057:
        razd = root.createElement("razdely")
        div.appendChild(razd)
        razd.appendChild(root.createTextNode(str(text.getText("text").split('\n')[0:5])))
        p = root.createElement("pure_text")
        div.appendChild(p)
        p.appendChild(root.createTextNode(text.getText("text").replace('\n', ' ')))
    elif i > 1057:
        p = root.createElement("pure_text")
        div.appendChild(p)
        p.appendChild(root.createTextNode(text.getText("text").replace('\n', ' ')))
    i += 1
xml_str = root.toprettyxml('\t')
save_path = ("new_t.xml")
with open(save_path, "w", encoding="utf-8") as f:
    f.write(xml_str)