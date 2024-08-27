from metrica.models import AccessLogsModel
for r in AccessLogsModel.objects.all(): print(r.ip_address)
