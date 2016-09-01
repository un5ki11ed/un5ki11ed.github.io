import os
import sys

def u(x):
  return x.decode('utf-8')

def save_file(data, file):
  out = data.encode('utf-8')
  open(file, 'wb').write(out)

def generate_addons_file():
  addons = os.listdir('.')
  addons_xml = u('<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<addons>\n')
  
  for addon in addons:
    #skip files, .git and .svn folders
    if( not os.path.isdir(addon) or addon == ".svn" or addon == ".git"): continue
    _path = os.path.join(addon, 'addon.xml')
    
    #read xml
    xml = open(_path, 'r').read()
    #remove first line/encoding line
    offset = xml.find(os.linesep)+1
    xml = xml[offset:]
    
    #add to result
    addons_xml += u(xml.rstrip() + os.linesep + os.linesep)
    
  #clean and add closing tag
  addons_xml = addons_xml.strip() + os.linesep + u('</addons>') + os.linesep
  save_file(addons_xml, 'addons.xml')

def generate_addons_md5():
  #generate checksum
  try:
    import md5
    checksum = md5.new(open('addons.xml', 'r').read()).hexdigest()
  except ImportError:
    import hashlib
    checksum = hashlib.md5(open('addons.xml', 'r', encoding='UTF-8').read()).hexdigest()
  #save checksum to file
  save_file(checksum, 'addons.xml.md5')

if (__name__ == "__main__"):
  generate_addons_file()
  generate_addons_md5()
