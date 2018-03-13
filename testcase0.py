# Test Case ID = ID_000
# Test Case Description: Verificar se o Título do Site é "Perfil Médico".
#autor: paulomachado

browser = webdriver.Firefox(executable_path='/home/paulo/Downloads/geckodriver')
browser.get('http://med-profile.apps.intmed.com.br')

assert 'Perfil Médico' in browser.title
