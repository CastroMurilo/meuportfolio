import pyautogui as pa
import time

# Define o FAILSAFE como True, o que significa que mover o mouse para o canto superior esquerdo irá gerar uma exceção e interromper o programa.
pa.FAILSAFE = True

# Define a pausa entre as funções do PyAutoGUI como 1 segundo.
pa.PAUSE = 1

# Pressiona as teclas Win+R para abrir a caixa de diálogo Executar.
pa.hotkey("win", "r")

# Digita a URL do perfil do LinkedIn na caixa de diálogo Executar e pressiona Enter.
pa.typewrite(" https://www.linkedin.com/in/murilorosacastro \n")

# Aguarda 5 segundos para permitir o carregamento da página do LinkedIn.
time.sleep(5)

# Clica com o botão direito na imagem "portfolio.png" na tela (com um nível de confiança de 0.8) e exibe o menu de contexto para a localização clicada com o botão direito.
pa.rightClick(pa.locateCenterOnScreen("img\\portfolio.png", confidence=0.8), duration=1)

# Clica na imagem "abrir.png" na tela (com um nível de confiança de 0.8) para abrir a opção do menu de contexto.
pa.click(pa.locateCenterOnScreen("img\\abrir.png", confidence=0.8), duration=1)

# Aguarda 1 segundo.
time.sleep(1)

# Clica na imagem "seguir.png" na tela (com um nível de confiança de 0.8).
pa.click(pa.locateCenterOnScreen("img\\seguir.png", confidence=0.8), duration=1)

# Exibe um alerta com a mensagem, título e texto do botão especificados.
pa.alert(text="Este é meu portfólio", title="Aviso do sistema", button="OK")
