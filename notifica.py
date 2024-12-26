from winotify import Notification
notificacao = Notification(app_id="Bom dia", title="Esta notificao é para ir para o diario oficial")
notificacao.add_actions(label="aprenda mais", launch="http://www.rondonopolis.mt.gov.br/diario-oficial/")

notificacao.show()
