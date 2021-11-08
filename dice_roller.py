def main():
    import random
    results = {}

    number_of_players = int(input('What is a number of players?'))
    for i in range(number_of_players):
        name = input('Give a player\'s name')
        results[name] = {'total': 0, 'rolls': []}
                            
    dice_rolls = int(input('How many times will each playes roll a dice?'))                            
    for key in results:
        dice_sum = 0
        for i in range(0,dice_rolls):
            roll = random.randint(1,6)
            results[key]['rolls'].append(roll)
            dice_sum += roll
        results[key]['total'] = dice_sum
    sort_results = sorted(results.items(), key=lambda x: x[1]['total'], reverse=True)
    print(f'Results {results}')
    print(f'The winner is {sort_results[0][0]} ! Congrat ! ')

if __name__== "__main__":
    main()