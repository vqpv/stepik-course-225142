coins = int(input())

match coins:
    case coins if coins > 1000:
        print("Герой может купить замок.")
    case coins if 500 <= coins <= 1000:
        print("Герой может купить армию.")
    case coins if coins < 500:
        print("Герой может купить несколько предметов или артефактов.")
