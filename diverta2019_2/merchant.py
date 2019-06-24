initial_nuts = int(input())

a_gold, a_silver, a_bronze = map(int, input().split(' '))
b_gold, b_silver, b_bronze = map(int, input().split(' '))

gold_to_nuts = max(a_gold, b_gold)
silver_to_nuts = max(a_silver, b_silver)
bronze_to_nuts = max(a_bronze, b_bronze)

nuts = [
    [(g, s, ( (initial_nuts - g * min(a_gold, b_gold) - s * min(a_silver, b_silver)) // min(a_bronze, b_bronze))
         for s in range(0, ((initial_nuts - g * min(a_gold, b_gold)) // min(a_silver, b_silver))+1)] for g in range(0, (initial_nuts // min(a_gold, b_gold))+1)]