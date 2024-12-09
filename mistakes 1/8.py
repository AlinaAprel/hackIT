#ПОДСЧЕТ ГОЛОСОВ
votes = ["Да", "Нет", "Может быть", 1];
yes_count = 0;
no_count = 0;

for vote in votes:
    if vote == "Да":
        yes_count += 1;
    else if vote == "Нет":
        no_count += 1;

print("Голоса 'Да':", yescount);
print("Голоса 'Нет':", no_count);
