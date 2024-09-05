import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i+1}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    man_1 = asyncio.create_task(start_strongman('Pasha', 3))
    man_2 = asyncio.create_task(start_strongman('Denis', 4))
    man_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await man_1
    await man_2
    await man_3

asyncio.run(start_tournament())
