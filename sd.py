#! python 3

# this newbie code, searchs copied title at pubmed, finds exact title if there is more than 1 result and brings 5 most similar articles.
# you can select similar article web page at start if you want to see more similar articles than 5.
# if you select continue you can see article titles and abstracts.
# from there, you can select download or go to article web page.
# some free article web sites contents different pdf files aside articles. so its good to check to see if the pdf is OK.
# some web sites' pdf link ends with /pdf. this little, only searchs .pdf.
# last resort is sci-hub. that module was very helpful.
# advices are our god.

import sys, os
from bs4 import BeautifulSoup as Soup       # pip install beatifulsoup4
from pyperclip import paste                 # pip install pyperclip
from urllib.parse import urlparse, urljoin
from requests import get                    # pip install requests
from requests.exceptions import RequestException
from webbrowser import open as OP
import scidownl.scihub as sci               # pip install scidownl

F_data, F_abstract, L_list, Link, PDFlink = '','','','',''

class Sd:

  def res(self):
    try:
      r = get(self, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 YaBrowser/19.7.3.172 Yowser/2.5 Safari/537.36'})
      r.raise_for_status()
      return r
    except RequestException as err:
      print (err)
      os.system('pause')

  def search(self): # term search results as pmid
    T = f'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={self}[Title]&retmax=100'
    Tr = Sd.res(T)
    Ts = Soup(Tr.text,'html.parser')
    return Ts

  def fetch(self): # id search results as title, abstract etc.
    I = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={self}&retmode=xml'
    Ir = Sd.res(I)
    Is = Soup(Ir.text,'html.parser')
    return Is

  def link(self): # brings similar articles' ids
    L = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&db=pubmed&id={self}&cmd=neighbor_score'
    Lr = Sd.res(L)
    Ls = Soup(Lr.text,'html.parser')
    return Ls

  def similar(self): # opens similar articles web page
    Si = f'https://www.ncbi.nlm.nih.gov/pubmed?linkname=pubmed_pubmed&from_uid={self}'
    OP(Si)

  def pubmed(self): # opens article's web page
    P = f'https://www.ncbi.nlm.nih.gov/pubmed/{self}'
    OP(P)

  def download(self): # downloads selected similar title
    D = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&id={self}&cmd=prlinks'
    
    def pmc(Id): # converts pmid to pmcid and looks for free pmc article
      PMCd = f'https://www.ncbi.nlm.nih.gov/pmc/articles/pmid/{Id}/'
      return PMCd

    def getpdf(link): # downloads only one pdf file.
      re_pdflink = Sd.res(link)
      if not re_pdflink.ok:
        return
      parse_url = urlparse(re_pdflink.url)
      baseurl = f'{parse_url.scheme}://{parse_url.netloc}'
      PDF = Soup(re_pdflink.text,'html.parser')
      for i in PDF.find_all('a', href=True):
        if i['href'].lower().endswith('.pdf'):
          global PDFlink
          PDFlink = i['href']
          res = Sd.res(urljoin(baseurl,PDFlink))
          PDFfile = open(self + '.pdf', 'wb')
          PDFfile.write(res.content)
          PDFfile.close()
          print('Download has been completed')
          os.system('pause')
          break
      
    re_dlink = Sd.res(D) # initial try
    try:
      Dlink = Soup(re_dlink.text,'html.parser').select_one('Url').text
      getpdf(Dlink)
    except AttributeError:
      pass
    
    if PDFlink=='': # second try if there's no free article web site
      print('trying for free pmc')
      link = pmc(self)
      try:
        getpdf(link)
      except:
        pass
      
    if os.path.exists(self + '.pdf') == False: # third try if there's no free pmc option
      print('trying for sci-hub')
      try:
        DOI = Sd.fetch(self).find('articleid', idtype='doi').text
        scid = sci.SciHub(DOI,self).download(choose_scihub_url_index=3)
      except Exception as ex:
        print('Error has ocured' + str(ex))
        pass
      os.system('pause')
    print()
  
  def sd(self): 

    # process copied article title
    if self == '':
      print('No title copied')
      input ('press Enter to make new search')
      Sd.sd(paste())
    Ctitle = self.strip().replace('\n', ' ').replace('\r','').lower()
    title = Ctitle.split(' ',100)
    unwanted = ['and','to','with','not','in','the','of','by','a','an','for','on','from','among'] # they distrupt search
    [title.remove(i) for i in unwanted if i in title]
    [title.remove(i) for i in unwanted if i in title]
    title = (' ').join(title).replace('\'','').replace(',','').replace(':','').replace(' ','[Title]+')
  
    global Link, F_abstract, F_data, L_list

    # brings search results as article title
    S_list = Sd.search(title).select('Id')

    if len(S_list) == 0:
      print('No result for '+paste())
      nores = input('Press Enter to exit or make new search(n): ')
      if nores == 'n':
        Sd.sd(paste())
      else:
        sys.exit()

    S_list = [i.get_text() for i in S_list]
    id_string = (',').join(map(str,S_list))
    F_data = Sd.fetch(id_string).select('ArticleTitle')

    # compare search results with copied article title
    for j in F_data:
      AT = str(j.get_text()).strip('.?')
      if AT.lower() == Ctitle:
        Link = S_list[F_data.index(j)]
        break

    # brings 5 most similar articles's ids, titles and abstracts
    L_list = Sd.link(Link).find('linkname', text='pubmed_pubmed_five').find_all_next('id', limit=5)
    L_list = [i.get_text() for i in L_list]
    id_string = (',').join(map(str,L_list))
    Fetch = Sd.fetch(id_string)
    F_data = Fetch.select('ArticleTitle')
    F_abstract = Fetch.find_all('abstract')
    F_abstract = [i.get_text() for i in F_abstract]

if not os.path.exists('pdffiles'):
  os.makedirs('pdffiles')
  os.chdir('pdffiles')

Sd.sd(paste())

while True:
  fork = input('Open in web, See similar 5 results(w/s): ')
  print()
  if fork == 'w':
    Sd.similar(Link)
    new = input('''To search another press 'y' or press Enter to continue: ''')
    print()
    if new == 'y':
      Sd.sd(paste())

  while fork == 's' or new == '':
    for j in F_data:
      AT = j.get_text()
      print(F_data.index(j)+1, end=' - ')
      print(AT)
    print()

    answer = input('Select one, new search(n),exit(x): ')
    if answer == 'x':
      sys.exit()
    elif answer == 'n':
      Sd.sd(paste())
    else:
      print(F_abstract[int(answer)-1])
      ask = input('open in web, download, return to list, exit(w/d/r/x): ')
      print()

      if ask == 'w':
        Sd.pubmed(L_list[int(answer)-1])
        new = input('''To search another press 'y' or press Enter to return: ''')
        print()
        Sd.sd(paste()) if new =='y' else None
      elif ask == 'd':
        Sd.download(L_list[int(answer)-1])
      elif ask == 'r':
        pass
      elif ask == 'x':
        sys.exit()