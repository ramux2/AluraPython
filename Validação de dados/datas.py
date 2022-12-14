from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def mes_cadastro(self):
        meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        mes_cadastrado = self.momento_cadastro.month
        return meses[mes_cadastrado - 1]

    def semana_cadastrada(self):
        dias_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]

    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y   %H:%M")

        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastrado = (datetime.today())