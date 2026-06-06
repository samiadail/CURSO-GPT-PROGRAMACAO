# É converter 1780704002 (timestamp) para um formato de horas legível

from datetime import datetime

# Variavel TimeStamp
time_stamp = 1780704002
# Data atualizada
data_atualizada = datetime.fromtimestamp(time_stamp)

print(data_atualizada)