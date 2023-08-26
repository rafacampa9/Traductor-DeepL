from selenium.webdriver.support.ui import WebDriverWait


#para condiciones en selenium
from selenium.webdriver.support import expected_conditions as ec

#excepción de timeout en selenium
from selenium.common.exceptions import TimeoutException

#para definir que tipo de búsqueda voy a definir para el elemento
from selenium.webdriver.common.by import By



import time as t


from iniciar_chrome.chromedriver import iniciar_chrome




def lenguaje(lang, lista):
    if lang == 'español': lista.append('es')
    elif lang == 'alemán': lista.append('de')
    elif lang == 'búlgaro': lista.append('bg')
    elif lang == 'checo': lista.append('cs')
    elif lang == 'chino': lista.append('zh')
    elif lang == 'coreano': lista.append('ko')
    elif lang == 'danés': lista.append('da')
    elif lang == 'eslovaco': lista.append('sk')
    elif lang == 'esloveno': lista.append('sl')
    elif lang == 'estonio': lista.append('et')
    elif lang == 'finés': lista.append('fi')
    elif lang == 'francés': lista.append('fr')
    elif lang == 'griego': lista.append('el')
    elif lang == 'húngaro': lista.append('hu')
    elif lang == 'indonesio': lista.append('id')
    elif lang == 'inglés': lista.append('en')
    elif lang == 'italiano': lista.append('it')
    elif lang == 'japonés': lista.append('ja')
    elif lang == 'letón': lista.append('lv')
    elif lang == 'lituano': lista.append('lt')
    elif lang == 'neerlandés': lista.append('nl')
    elif lang == 'noruego': lista.append('nb')
    elif lang == 'polaco': lista.append('pl')
    elif lang == 'portugués': lista.append('pt')
    elif lang == 'rumano': lista.append('ro')
    elif lang == 'ruso': lista.append('ru')
    elif lang == 'sueco': lista.append('sv')
    elif lang == 'turco': lista.append('tr')
    elif lang == 'ucraniano': lista.append('uk')







# ENTRAMOS EN LA WEB DEEPL ########################################################################
def traductor(mensaje, lang, trad):
    
    driver = iniciar_chrome()
    wait = WebDriverWait(driver, 10)
    lista =  []
    lenguaje(lang, lista)
    lenguaje(trad, lista)
    
    lista2 = []
    for m in mensaje:
        if m == ' ': lista2.append('%20')
        elif m == '?': lista2.append("%3F")
        elif m == '/': lista2.append('%5C%2F')
        elif m == '=': lista2.append('%3D')
        elif m == ',': lista2.append('%2C')
        elif m==':': lista2.append('%3A')
        elif m == ';': lista2.append('%3B')
        elif m == '+': lista2.append('%2B')
        elif m == '@': lista2.append('%40')
        elif m == '$': lista2.append('%24')
        elif m == '%': lista2.append('%25')
        elif m == '|': lista2.append('%5C%7C')
        elif m == '"\"': lista2.append('%5C%5C')
        elif m == '^': lista2.append('%5E')
        elif m == '[]': lista2.append('%5B')
        elif m == ']': lista2.append('%5D')
        elif m == '{': lista2.append('%7B')
        elif m == '}': lista2.append('%7D')
        elif m == '`': lista2.append('%60')
        else: lista2.append(m)

    cadena = ''.join(lista2)
    driver.get(
            'https://www.deepl.com/translator#' + lista[0] + '/' + lista[1] + '/' + cadena
            )
    lista = []
    #breakpoint()
    t.sleep(0.5)

    try:
        wait.until(
            ec.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//button[contains(text(),"Aceptar todas las cookies")]')
            )
        ).click()
    except TimeoutException:
        print('No cookies')

    
    try:
        elemento = wait.until(
            ec.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    'd-textarea[aria-labelledby="translation-results-heading"]'
                )
            )
        )
    except TimeoutException:
        print('Tampoco vale')

    answer = elemento.text
    return answer
    
    
            
