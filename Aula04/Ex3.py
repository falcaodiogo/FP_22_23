#Não pode criar, editar nem carregar conteúdo … Sem armazenamento suficiente. Obtenha já mais armazenamento ou remova ficheiros do Drive, Google Fotos ou Gmail.
# This program generates 20 terms of a sequence by a recurrence relation.

Un = 100
contador = 0
while Un > 0:
    contador += 1
    print("Termo", contador, ", Un=", Un)
    Un = 1.01*Un - 1.01 