from django.db import models
from datetime import timedelta


class Funcionarios(models.Model):
    codigo_funcionario = models.BigAutoField(primary_key=True)
    nome_completo = models.CharField(max_length=45)
    horario_entrada = models.DateTimeField(null=False, blank=False)
    horario_saida = models.DateTimeField(null=False, blank=False)

    @property
    def horas_extras(self):
        horas_trabalhadas = self.horario_saida - self.horario_entrada
        HORAS_NORMAIS = 8.8
        if horas_trabalhadas > HORAS_NORMAIS:
            return horas_trabalhadas - HORAS_NORMAIS
        return timedelta(hours=0)

    def testar_horario(self):
        if self.horario_entrada >= self.horario_saida:
            return False
        return True

    def __str__(self) -> str:
        return self.nome_completo
