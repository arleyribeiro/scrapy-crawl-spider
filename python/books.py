
import wget
url = 'https://link.springer.com/content/pdf/10.1007%2Fb100747.pdf'
filename = wget.detect_filename(url)
print(filename)

filename = wget.download(url)
print(filename)